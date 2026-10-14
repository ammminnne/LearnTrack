# LearnTrack — Big Data Analytics Backend

**A distributed Big Data analytics backend for student activity tracking and analytical reporting.**

## Overview

LearnTrack is a Big Data project designed to explore distributed data storage, processing, and analytics in an educational context. It combines Python, Apache Spark, Hadoop HDFS, MongoDB, Docker Compose, and Jenkins to provide an environment for processing student-related data and generating analytical reports.

The project explores a Lambda Architecture approach to distributed data processing, combining data-processing components with scalable storage technologies.

## Key Features

- **Distributed data processing:** Apache Spark with Python.
- **Distributed storage:** Hadoop HDFS.
- **NoSQL database infrastructure:** MongoDB with configuration servers, shards, and a query router.
- **Containerized environment:** Docker Compose for managing the project's services.
- **Automation infrastructure:** Jenkins for exploring continuous integration and automation workflows.
- **Data generation and processing:** Python scripts for generating and processing project data.
- **Analytical reporting:** CSV, JSON, and PDF artifacts associated with the project.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data generation and processing |
| Apache Spark | Distributed data processing |
| Hadoop HDFS | Distributed file storage |
| MongoDB | NoSQL database and sharding infrastructure |
| Docker Compose | Container orchestration |
| Jenkins | Automation and CI/CD environment |
| Git & GitHub | Version control and project hosting |

## Architecture

The project follows a Lambda Architecture approach for Big Data processing.

The main infrastructure components are:

- **Data processing:** Python scripts and Apache Spark.
- **Distributed storage:** Hadoop HDFS.
- **Database layer:** MongoDB configuration server, shard servers, and `mongos` router.
- **Infrastructure management:** Docker Compose.
- **Automation:** Jenkins.

These components provide a foundation for experimenting with distributed data processing and analytical workflows.

> Note: The exact batch-processing, real-time-processing, and serving-layer implementations depend on the corresponding application code and configuration.

## Project Structure

```text
LearnTrack_Project/
├── project_data/          # Project data and shared storage
├── .gitignore             # Git exclusions
├── docker-compose.yaml    # Distributed services configuration
├── generate_data.py       # Data generation script
├── spark_processor.py     # Spark processing script
├── daily_report.csv       # Generated report, if available
├── student_scores.json   # Student-related data, if available
├── bigdata-report .pdf    # Project report
└── README.md              # Project documentation
```

Some generated data files and the `project_data/` directory are excluded from Git through `.gitignore`.

## Prerequisites

Before running the infrastructure, make sure you have:

- Docker Desktop installed and running.
- Docker Compose available through the Docker CLI.
- Git installed.
- Python installed if you want to run the Python scripts locally.

The infrastructure requires sufficient memory and system resources to run Hadoop, Spark, MongoDB, and Jenkins together.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ammminnne/LearnTrack.git
cd LearnTrack
```

### 2. Start the infrastructure

```bash
docker compose up -d
```

Docker Compose will start the services defined in `docker-compose.yaml`.

### 3. Check the running containers

```bash
docker compose ps
```

### 4. Access the service interfaces

Depending on the services that started successfully, the configured local endpoints include:

- **Hadoop NameNode UI:** http://localhost:9870
- **Spark Master UI:** http://localhost:8080
- **MongoDB router:** `localhost:27017`
- **Jenkins:** http://localhost:9090

These endpoints assume the containers are running and the corresponding ports are available.

### 5. Stop the infrastructure

```bash
docker compose down
```

The commands above start and stop the infrastructure. Additional initialization may be required before the MongoDB sharded cluster is fully operational.

## Configuration and Data

The Docker Compose configuration mounts `project_data/` into several containers for shared file access.

The `.gitignore` file excludes generated data and environment-specific files from version control. If you clone this repository, create any required local data directories and supply the necessary input files before running workflows that depend on them.

Do not commit passwords, API keys, database credentials, private datasets, or other sensitive information.

## Future Improvements

Potential areas for further development include:

- Documenting and automating the complete Lambda Architecture workflow.
- Integrating the Spark processing pipeline with HDFS and MongoDB.
- Adding automated tests for data-processing scripts.
- Improving Jenkins pipeline automation.
- Adding architecture diagrams, execution screenshots, and reproducible analytical results.
- Documenting data schemas and report-generation workflows.

## Author

**Mohamed El Amine Zertal**

Computer Science Graduate — Software Engineering and Intelligent Systems

- GitHub: [@ammminnne](https://github.com/ammminnne)
- LinkedIn: [Mohamed El Amine Zertal](https://www.linkedin.com/in/mohamed-el-amine-zertal-2b3196414)

## Contributors

- **Kebab Takieddin**

This project was developed collaboratively as part of a Big Data Analytics project.

---

*LearnTrack — Distributed data processing and analytics for educational data.*
