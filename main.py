import csv
import sys
import os
import time
import mysql.connector
from analyzer import analyze_review

INPUT_FILE = "Reviews.csv"

def get_db_connection():
    for _ in range(10):
        try:
            conn = mysql.connector.connect(
                host=os.getenv("MYSQL_HOST", "db"),
                user=os.getenv("MYSQL_USER", "root"),
                password=os.getenv("MYSQL_PASSWORD", "secretpass"),
                database=os.getenv("MYSQL_DATABASE", "review_analytics"),
                connect_timeout=60  # Extended to handle long-running pipeline connections
            )
            return conn
        except mysql.connector.Error:
            time.sleep(3)
    print("Error: Could not bind to MySQL network database channel wrapper.")
    sys.exit(1)

def main():
    try:
        with open(INPUT_FILE, encoding="utf-8") as f:
            reviews = list(csv.DictReader(f))
    except FileNotFoundError:
        print(f"Error: '{INPUT_FILE}' was not discovered in execution root.")
        sys.exit(1)

    conn = get_db_connection()
    cursor = conn.cursor()

    print("Beginning large batch analytics pipeline streaming job (1,000 Records)...")
    
    # Safely scale the ingestion bounds to the target partition footprint
    sample_reviews = reviews[:1000]
    total_records = len(sample_reviews)

    for index, review in enumerate(sample_reviews, 1):
        ratings = analyze_review(review["Text"])
        review_id = review["Id"]
        product_id = review["ProductId"]
        
        for topic_name, star_rating in ratings.items():
            cursor.execute(
                """INSERT INTO topic_scores (review_id, product_id, topic_name, star_rating)
                   VALUES (%s, %s, %s, %s)""",
                (review_id, product_id, topic_name, star_rating)
            )
        
        # Batch commits to enhance ingestion velocity and relieve disk I/O pressure
        if index % 10 == 0 or index == total_records:
            conn.commit()
            
        # Clean progress telemetry logging to avoid standard output buffer drops
        if index % 50 == 0 or index == total_records:
            print(f"Progress Pipeline: Successfully ingested {index}/{total_records} reviews.")

    cursor.close()
    conn.close()
    print("Pipeline data streaming operations completed successfully.")

if __name__ == "__main__":
    main()
