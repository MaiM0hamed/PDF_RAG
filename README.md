# PDF RAG

A Retrieval-Augmented Generation (RAG) application that enables users to upload PDF documents, process their content, perform semantic search, and generate context-aware answers using Large Language Models (LLMs).

## Features

* PDF Upload & Processing
* Text Extraction
* Chunking & Embeddings
* Semantic Search
* Vector Database Integration
* LLM-powered Question Answering
* FastAPI Backend
* PostgreSQL + PgVector
* Celery Background Processing
* Docker Support
* Monitoring with Prometheus & Grafana

---

## Requirements

* Python 3.10
* Docker & Docker Compose
* PostgreSQL
* Miniconda (Recommended)

---

## System Dependencies

```bash
sudo apt update
sudo apt install libpq-dev gcc python3-dev
```

## Create Conda Environment

```bash
conda create -n PDF_RAG python=3.10
conda activate PDF_RAG
```

## Installation

Clone the repository:

```bash
git clone https://github.com/MaiM0hamed/PDF_RAG.git
cd PDF_RAG
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create environment variables file:

```bash
cp .env.example .env
```

Update your environment variables:

```env
OPENAI_API_KEY=your_api_key
```

---

## Database Migration

```bash
alembic upgrade head
```

---

## Run Docker Services

```bash
cd docker
cp .env.example .env
```

Update the environment variables, then run:

```bash
docker compose up -d
```

---

## Available Services

| Service    | URL                   |
| ---------- | --------------------- |
| FastAPI    | http://localhost:8000 |
| Flower     | http://localhost:5555 |
| Grafana    | http://localhost:3000 |
| Prometheus | http://localhost:9090 |

---

## Run Development Server

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

---

## Run Celery Worker

```bash
python -m celery -A celery_app worker --queues=default,file_processing,data_indexing --loglevel=info
```

## Run Celery Beat

```bash
python -m celery -A celery_app beat --loglevel=info
```

## Run Flower Dashboard

```bash
python -m celery -A celery_app flower --conf=flowerconfig.py
```

Then open:

```text
http://localhost:5555
```

---

## Project Structure

```text
PDF_RAG/
├── api/
├── services/
├── workers/
├── database/
├── vector_db/
├── docker/
├── alembic/
├── assets/
├── main.py
├── requirements.txt
└── README.md
```

---

## License

MIT License © 2026 Mai Mohamed
