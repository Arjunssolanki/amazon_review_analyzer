import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Amazon Food Feature Insights Dashboard", layout="wide")

st.title("🍎 Amazon Food Review Feature Breakdown Dashboard")
st.markdown("Real-time sentiment dissemination calculated using containerized **Jev AI Primitives** execution models.")

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "db"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", "secretpass"),
        database=os.getenv("MYSQL_DATABASE", "review_analytics")
    )

# Pull unique product IDs from the database to populate the sidebar dropdown dynamically
def get_unique_products():
    try:
        conn = get_db_connection()
        query = "SELECT DISTINCT product_id FROM topic_scores"
        df = pd.read_sql(query, conn)
        conn.close()
        return ["All Products"] + df["product_id"].tolist()
    except Exception:
        return ["All Products"]

def load_filtered_dataframe(selected_product):
    try:
        conn = get_db_connection()
        if selected_product == "All Products":
            query = "SELECT review_id, product_id, topic_name, star_rating FROM topic_scores"
            df = pd.read_sql(query, conn)
        else:
            query = "SELECT review_id, product_id, topic_name, star_rating FROM topic_scores WHERE product_id = %s"
            df = pd.read_sql(query, conn, params=[selected_product])
        conn.close()
        return df
    except Exception:
        return pd.DataFrame()

# 1. Sidebar Control System Configuration Panel
st.sidebar.header("🎯 Analytics Filters")
product_list = get_unique_products()
selected_prod = st.sidebar.selectbox("Filter by Product ID SKU:", product_list)

# 2. Dynamic Operational Query Execution
df = load_filtered_dataframe(selected_prod)

if df.empty:
    st.warning("⚠️ No database table metrics detected yet. Run the ingestion main pipeline loop.")
else:
    summary = df.groupby("topic_name").agg(
        Average_Rating=("star_rating", "mean"),
        Total_Reviews=("star_rating", "count")
    ).reset_index()

    summary["Average_Rating"] = summary["Average_Rating"].round(1)

    st.subheader(f"📈 Performance Metrics: {selected_prod}")
    cols = st.columns(len(summary))
    for idx, row in summary.iterrows():
        with cols[idx]:
            st.metric(label=row["topic_name"], value=f"{row['Average_Rating']} ★", delta=f"{row['Total_Reviews']} reviews")

    st.subheader("📊 Sentiment Analysis by Food Attribute")
    fig = px.bar(
        summary,
        x="topic_name",
        y="Average_Rating",
        text="Average_Rating",
        color="Average_Rating",
        color_continuous_scale=px.colors.sequential.Reds,
        labels={"topic_name": "Food Metric Topic", "Average_Rating": "Star Rating (1-5)"}
    )
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Total Partition Rows")
    st.sidebar.info(f"Analyzing {len(df)} database records.")
    st.plotly_chart(fig, width="stretch")
