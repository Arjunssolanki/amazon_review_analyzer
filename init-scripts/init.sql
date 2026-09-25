CREATE DATABASE IF NOT EXISTS review_analytics;

USE review_analytics;

CREATE TABLE IF NOT EXISTS topic_scores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    review_id VARCHAR(50),
    topic_name VARCHAR(50),
    star_rating DECIMAL(3, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);