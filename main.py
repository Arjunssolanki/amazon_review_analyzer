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
                database=os.getenv("MYSQL_DATABASE", "review_analytics")
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

    print("Beginning batch analytics pipeline streaming job...")
    for review in reviews[:50]:
        ratings = analyze_review(review["Text"])
        review_id = review["Id"]
        
        for topic_name, star_rating in ratings.items():
            cursor.execute(
                """INSERT INTO topic_scores (review_id, topic_name, star_rating)
                   VALUES (%s, %s, %s)""",
                (review_id, topic_name, star_rating)
            )
        conn.commit()
        print(f"Streamed Record {review_id} smoothly into database metrics.")

    cursor.close()
    conn.close()
    print("Pipeline data streaming operations completed successfully.")

if __name__ == "__main__":
    main()
