# Amazon Review Analyzer 🚀

An enterprise-ready, containerized **Natural Language Processing (NLP) & Feature Sentiment Pipeline** that processes unstructured, raw e-commerce product feedback into structured, granular feature-breakdown metrics.

By leveraging **Jev AI (via the TypeSafe SDK)** over a secure proxy bridge, the application evaluates multi-dimensional consumer feedback to construct native **Amazon-style descriptive star ratings** directly inside an isolated container environment.

---

## 📊 Detailed Project Ledger & Summary

### 🎯 Why We Created This Project (Project Objectives)

Online consumer evaluations are heavily saturated with unstructured, free-text feedback. While global ratings give a surface-level impression, they hide specific flaws or highlights regarding individual product features (e.g., a phone with a 5-star display but a 1-star battery).

To extract deep, actionable consumer insights, this project was developed as a high-performance analytics utility designed to:

- Bypass superficial global scores by evaluating distinct, feature-level customer sentiment.
- Streamline messy textual feedback into a deterministic, high-quality data payload schema.
- Demonstrate advanced industry competencies across **Data Engineering**, **AI/ML API Orchestration**, and **System Containerization (Docker)**.

### 🛠️ What We Have Done (Engineering Pipeline Flow)

1. **API Integration & Proxy Architecture:** Implemented a robust architecture utilizing the `typesafe-sdk` to route programmatic primitives through an external proxy layer (`OpenRouter`), allowing token evaluations without local authentication blocks.
2. **Defensive Prompt Design & Categorization Schema:** Structured a dual-layered evaluation framework containing 12 distinct analytical parameters. For each targeted topic, the pipeline queries Jev using:
   - A `Noul` boolean confidence vector to measure topic relevance probability.
   - A `Score` satisfaction evaluation metric based on 5 calibrated behavioral levels.
3. **Data Quality Thresholding:** Designed a strict validation gate that rejects classification noise by dropping feature scores if the topic mention probability falls below a **>= 0.5 confidence threshold**.
4. **Data Aggregation Engine:** Built mathematical calculation scripts to map raw 0–4 token scales into an absolute 1–5 star metric, dynamically tracking running totals and review frequencies per category.
5. **Containerization & Sandbox Execution:** Bundled all computational resources, environment boundaries, and libraries inside a lightweight, reproducible **Docker Linux container layer**.

### 🏆 What We Have Achieved (Results & Business Insights)

- **Granular Sentiment Dissemination:** Successfully processed a batch of 50 sample product reviews from the **Kaggle Amazon Fine Food Reviews** dataset, mapping thousands of unstructured words into an automated dashboard.
- **Deterministic Noise Elimination:** Proved the capability of the thresholding engine by accurately identifying and reporting empty product domains (e.g., flagging _Battery Life_ as `no ratings yet` when no explicit text existed).
- **Enterprise Infrastructure Baseline:** Standardized the workflow into a plug-and-play microservice architecture, allowing seamless integration into downstream streaming systems, cloud data lakes, or interactive dashboards.

---

## 🏛️ Comprehensive Architecture & File Manifest

- **`main.py`** — Orchestrates the entire pipeline; handles CSV reading from the Kaggle dataset, iterates review parsing, calls the analytical service, and renders the terminal visualization dashboard.
- **`analyzer.py`** — Instantiates the authenticated `TypeSafeClient` via proxy configurations, sends parallel queries to Jev, and applies data-filtering logic.
- **`questions.py`** — Configures the underlying tracking criteria matrix, mapping explicit instruction text to custom `Noul` and `Score` structures.
- **`aggregation.py`** — Performs numerical operations to compute running averages and review counts per topic.
- **`Dockerfile`** — Declares structural compilation parameters to build the runtime container image on top of a clean Python environment layer.

---

## 💻 System Configuration & Local Setup

### ⚙️ Prerequisites

Before running the deployment steps, make sure your computer has the following tools installed:

- **Python 3.12**
- **Docker Desktop** (Make sure the application is open and running in the background)

### 📦 1. Clone & Initialize Workspace

Navigate to your active code directory and verify the project footprint structure:

```bash
cd amazon-review-analyzer
```

### 🔑 2. Environmental Variables Configuration

Create a private environmental credentials file in the root folder named exactly **`.env`** and configure your keys:

```text
TYPESAFE_API_KEY=your_openrouter_api_key_here
TYPESAFE_BASE_URL=https://openrouter.ai
```

_(Note: `.env` is intentionally blocked by our `.gitignore` rules to keep your secret API keys secure)._

### 📊 3. Dataset Placement

Ensure your unzipped Kaggle dataset file is saved directly in the project root folder as:

```text
Reviews.csv
```

---

## 🚀 Execution Instructions (Docker Compilation)

Execute these two commands sequentially inside your terminal to build the image and run the application:

### Step A: Compile the Docker Image

```bash
docker build -t amazon-analyzer:v1 .
```

### Step B: Run the Pipeline Container

```bash
docker run --env-file .env amazon-analyzer:v1
```

---

## 📊 Expected Dashboard Output

Upon successful execution, the containerized runtime environment will process the reviews and display the following output directly in your console window:

```text
Review 1: {'Design & Style': 3.7}
Review 2: {}
Review 3: {'Design & Style': 4.4}
...
Review 50: {'Value for Money': 1.1}

4.3 out of 5 stars based on 50 processed ratings
---------------------------------------------
Value for Money    4.5 ★  (10 reviews)
Quality            4.0 ★  (6 reviews)
Performance        4.4 ★  (10 reviews)
Battery Life       no ratings yet
Ease of Use        4.7 ★  (10 reviews)
Design & Style     2.9 ★  (5 reviews)
```
