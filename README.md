# Full Pod Search

A robust platform that enables users to upload podcasts, processes the audio to extract and segment ideas into searchable clips, and provides full-text search capabilities for all discussed topics and ideas.


This platform leverages cutting-edge machine learning models and a modern tech stack to deliver fast, scalable, and intelligent podcast discovery.

# Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Architecture](#architecture)
5. [Installation](#installation)
6. [Usage](#usage)
7. [API Endpoints](#api-endpoints)
8. [Configuration](#configuration)
9. [Troubleshooting](#troubleshooting)
10. [Contributing](#contributing)
11. [License](#license)


## 1. [Introduction](#introduction)
This application transforms the way users interact with podcasts by providing a platform where they can:

1. Upload podcasts.
2. Automatically transcribe and analyze the content.
3. Segment the audio into smaller, byte-sized clips.
4. Search the entire podcast database by topics, keywords, or ideas.

Designed for podcast enthusiasts, researchers, and media professionals, this platform unlocks new possibilities for podcast discovery and analysis.

## 2. [Features](#features)
- **Podcast Upload:** Upload large audio files with ease.
- **Automatic Transcription:** Converts speech into text using advanced ASR (Automatic Speech Recognition).
- **Intelligent Segmentation:** Breaks podcasts into searchable, topic-based segments.
- **Full-Text Search:** Search across all podcast transcripts for specific ideas or topics.
- **Recommendations:** Suggests related podcasts based on content similarity.
- **Scalable and Modular:** Built with microservices to ensure scalability and maintainability.

## 3. [Tech Stack](#tech-stack)
- **Frontend:**
	- Framework: React
    - Event Handling: React Query
    - Component Library: Shadcn UI
    - State Management: Zustand

- **Backend:**
    - API Gateway: Nginx
    - Endpoints:
       - Go (Fiber Framework)
       - Python (FastAPI for ML Services)

- **Machine Learning:**
    - ASR: Whisper
    - LLM Processing: Advanced text summarization and topic extraction.
    - Embedding: Semantic analysis using state-of-the-art ML models.

- **Storage:**
    - Object Storage: MinIO
    - Relational Database: PostgreSQL
    - Cache: Redis
    - Vector Database: Milvus

- **Message Queue:** RabbitMQ

## 4. [Architecture](#architecture)
<img alt="High-Level Architecture" src="./docs/architecture.png"/>
<img alt="Detailed Architecture" src="./docs/workflow.png"/>


## 5. [Installation](#installation)
### Prerequisites
- Docker and Docker Compose
- Python 3.13+
- Go 1.23+
- Node.js 22.0+

### Steps
1. Clone the repository:
```bash
git clone https://github.com/sagyam/fullpodsearch.git
cd fullpodsearch
```

2. Start the services using Docker Compose:
```bash
docker compose -f ./docker/docker-compose.yml up --build
```

3. Access the application:
- Frontend: http://localhost:3000
- Core API: http://localhost:8000
- ML API: http://localhost:8100
- MinIO: http://localhost:9000
- RabbitMQ: http://localhost:15672

## 6. [Usage](#usage)

## 7. [API Endpoints](#api-endpoints)
- ### Upload Service
- ### Search Service
- ### Recommendations Service
- ### Processing Service

## 8. [Configuration](#configuration)
### Environment Variables
Set the following environment variables in a .env file:
```bash
# Backend
API_GATEWAY_PORT=8000
UPLOAD_SERVICE_PORT=8001
PROCESSING_SERVICE_PORT=8002

# ML Services
ASR_SERVICE_PORT=8003
LLM_SERVICE_PORT=8004

# Storage
POSTGRES_URI=postgresql://user:password@localhost:5432/dbname
REDIS_URI=redis://localhost:6379
MINIO_URI=minio://accesskey:secretkey@localhost:9000
MILVUS_URI=milvus://localhost:19530

```

## 9. [Troubleshooting](#troubleshooting)

- **Service Not Starting:** Ensure Docker is running and all dependencies are installed.
- **Slow Search:** Check if the Vector Database is indexed correctly.
- **Failed Uploads:** Verify MinIO and RabbitMQ are running.

## 10. [Contributing](#contributing)
- Sagyam Thapa: [LinkedIn](https://www.linkedin.com/in/sagyam/)

## 11. [License](#license)
This project is licensed under the MIT License. See the LICENSE file for details.