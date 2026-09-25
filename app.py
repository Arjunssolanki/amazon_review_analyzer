import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Amazon Food Feature Insights Dashboard", layout="wide")

st.title("🍎 Amazon Food Review Feature Breakdown Dashboard")
st.markdown("Real-time sentiment dissemination calculated using containerized **Jev AI Primitives** execution models.")

def load_dashboard_dataframe():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST", "db"),
            user=os.getenv("MYSQL_USER", "root"),
            password=os.getenv("MYSQL_PASSWORD", "secretpass"),
            database=os.getenv("MYSQL_DATABASE", "review_analytics")
        )
        query = "SELECT topic_name, star_rating FROM topic_scores"
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception:
        return pd.DataFrame()

df = load_dashboard_dataframe()

if df.empty:
    st.warning("⚠️ No database table metrics detected yet. Run the ingestion main pipeline loop.")
else:
    summary = df.groupby("topic_name").agg(
        Average_Rating=("star_rating", "mean"),
        Total_Reviews=("star_rating", "count")
    ).reset_index()

    summary["Average_Rating"] = summary["Average_Rating"].round(1)

    st.subheader("📈 Core Food Quality Breakdowns")
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
    st.sidebar.markdown("### Total Processed Rows")
    st.sidebar.info(f"Analyzing {len(df)} database records.")
    st.plotly_chart(fig, width="stretch")
