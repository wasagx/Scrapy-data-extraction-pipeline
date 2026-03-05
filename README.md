# 🚀 Scrapy Data Extraction Pipeline

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Scrapy](https://img.shields.io/badge/Scrapy-Web%20Scraping-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?logo=postgresql)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-47A248?logo=mongodb)
![Redis](https://img.shields.io/badge/Redis-Caching-red?logo=redis)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)
![Status](https://img.shields.io/badge/Project-Completed-success)

A **containerized data extraction pipeline** built with **Scrapy**, designed to ingest structured JSON data, process it through **Redis caching**, and persist the results into **PostgreSQL and MongoDB databases**.

The entire pipeline runs inside **Docker containers orchestrated with Docker Compose**, enabling reproducible environments and simplified deployment.

---

# 📌 Project Overview

This project demonstrates a **production-style data engineering pipeline** for structured data ingestion and storage.

The system performs the following steps:

1. Extracts structured data from JSON sources using **Scrapy spiders**
2. Processes the scraped items through **custom data pipelines**
3. Uses **Redis caching** to prevent duplicate processing
4. Stores cleaned and structured data into:
   - **PostgreSQL** (relational database)
   - **MongoDB** (NoSQL database)
5. Exports stored data into CSV format for further analysis

The entire workflow is **fully containerized using Docker** to ensure scalability and portability.

---

# 🏗 Pipeline Architecture

```
JSON Files
    │
    ▼
Scrapy Spider
    │
    ▼
Item Processing Pipeline
    │
 ┌───────────────┬───────────────┐
 ▼               ▼               ▼
Redis Cache   PostgreSQL DB   MongoDB DB
    │               │               │
    └───────────────┴───────────────┘
                    │
                    ▼
               Data Export
                    │
                    ▼
                CSV Files
```

---

# 📂 Project Structure

```
scrapy-data-extraction-pipeline
│
├── docker-compose.yaml
├── Dockerfile
│
├── infra
│   ├── postgresql_connector.py
│   ├── redis_connector.py
│   └── mongodb_connector.py
│
├── jobs_project
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   │
│   └── spiders
│       ├── __init__.py
│       └── json_spider.py
│
├── query.py
├── requirements.txt
└── README.md
```

### Key Components

| Component | Description |
|--------|--------|
| **Scrapy Spider** | Reads JSON files and extracts structured data |
| **Pipelines** | Processes scraped items before storage |
| **Redis Cache** | Prevents duplicate records |
| **PostgreSQL** | Stores structured relational data |
| **MongoDB** | Stores flexible document-based data |
| **Docker** | Containerizes the entire application |
| **Docker Compose** | Orchestrates services |

---

# ⚙️ Setup Instructions

## Prerequisites

Ensure the following tools are installed:

- **Docker**
- **Docker Compose**
- **Python 3.x** (for running scripts locally)

You must also download the JSON files:

```
s01.json
s02.json
```

Place them inside:

```
jobs_project/jobs_project/data/
```

---

# 🛠 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/scrapy-data-extraction-pipeline.git
cd scrapy-data-extraction-pipeline
```

### 2️⃣ Install Python Dependencies (Optional for local testing)

```bash
pip install -r requirements.txt
```

### 3️⃣ Build and Start the Containers

```bash
docker-compose up --build
```

This command will:

- Build the Scrapy container
- Start **PostgreSQL**
- Start **MongoDB**
- Start **Redis**
- Automatically run the **Scrapy spider**

The spider will begin scraping JSON data and storing results in the databases.

---

# 📊 Exporting Data

Data stored in PostgreSQL and MongoDB can be exported to CSV.

### Step 1 — Access Scrapy Container

```bash
docker-compose exec scrapy bash
```

### Step 2 — Run Export Script

```bash
python query.py
```

This will generate:

```
postgres_data.csv
mongo_data.csv
```

These files contain the exported data from the respective databases.

---

# 🔄 Data Pipeline Workflow

### 1️⃣ Data Extraction

The Scrapy spider (`json_spider.py`) reads the JSON data files and parses the content into structured items.

### 2️⃣ Data Processing Pipelines

Three pipelines process the extracted data:

**DatabasePipeline**
- Inserts data into PostgreSQL.

**CachePipeline**
- Uses Redis to check for duplicates before processing.

**MongoPipeline**
- Stores documents in MongoDB.

### 3️⃣ Data Export

The `query.py` script retrieves stored data from PostgreSQL and MongoDB and exports it into CSV files.

---

# 🛠 Technologies Used

| Technology | Purpose |
|--------|--------|
| **Python** | Core programming language |
| **Scrapy** | Web scraping framework |
| **PostgreSQL** | Relational database |
| **MongoDB** | NoSQL database |
| **Redis** | In-memory caching |
| **Docker** | Containerization |
| **Docker Compose** | Service orchestration |

---

# 🚀 Features

✔ Scrapy-based structured data extraction  
✔ Redis caching to prevent duplicate processing  
✔ Multi-database storage (PostgreSQL + MongoDB)  
✔ Fully containerized architecture  
✔ Data export functionality for analysis  

---

# ⭐ Support

If you found this project useful, consider giving it a **star ⭐ on GitHub**.