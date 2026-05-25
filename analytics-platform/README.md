# Real-Time Analytics Platform — Submission Guide

## Project Overview

This project is a full-stack real-time analytics platform built using FastAPI, PostgreSQL, Redis, Celery, WebSockets, and Next.js.

The platform allows organizations to:

* Authenticate securely using JWT
* Create and process events asynchronously
* Store analytics events in PostgreSQL
* Process background jobs using Celery + Redis
* Receive live dashboard updates through WebSockets
* Visualize analytics in a modern Next.js dashboard

---

# Tech Stack

## Backend

* FastAPI
* SQLAlchemy Async
* PostgreSQL
* Redis
* Celery
* JWT Authentication
* WebSockets

## Frontend

* Next.js
* React
* Tailwind CSS
* Axios

## Infrastructure

* Docker Compose
* Redis Queue
* Celery Workers

---

# Architecture

```text
Frontend (Next.js)
        ↓
FastAPI Backend
        ↓
JWT Authentication
        ↓
Redis Queue
        ↓
Celery Worker
        ↓
PostgreSQL
        ↓
WebSocket Broadcast
        ↓
Live Dashboard Updates
```

---

# Features Implemented

## Authentication

* User signup
* User login
* JWT token generation
* Protected APIs

## Event Processing

* Create analytics events
* Store JSON payloads
* Async event queue using Celery
* Redis-based background processing

## Real-Time Features

* WebSocket integration
* Live dashboard updates
* Automatic analytics refresh

## Analytics

* Total event count
* Events grouped by type
* Multi-tenant organization support

## Frontend Dashboard

* Login UI
* JWT token storage
* Analytics dashboard
* Real-time updates
* API integration

---

# Folder Structure

```text
analytics-platform/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── tasks/
│   │   ├── websocket/
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── docker-compose.yml
│
├── frontend/
│   ├── app/
│   ├── lib/
│   ├── package.json
│   └── next.config.ts
│
└── README.md
```

---

# Backend Setup

## 1. Create Virtual Environment

```bash
python -m venv venv
```

## 2. Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Start PostgreSQL + Redis

```bash
docker compose up -d
```

---

# Run Backend

```bash
python -m uvicorn app.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# Run Celery Worker

```bash
python -m celery -A app.core.celery_app worker -Q events --pool=solo --loglevel=info
```

---

# Frontend Setup

## Install Dependencies

```bash
npm install
```

## Run Frontend

```bash
npm run dev
```

Frontend URL:

```text
http://localhost:3000
```

---

# API Endpoints

## Authentication

### Signup

```http
POST /auth/signup
```

### Login

```http
POST /auth/login
```

---

## Events

### Create Event

```http
POST /events
```

Sample Request:

```json
{
  "event_type": "purchase",
  "payload": {
    "amount": 5000
  }
}
```

---

## Analytics

### Summary

```http
GET /analytics/summary
```

### Events By Type

```http
GET /analytics/events-by-type
```

---

# WebSocket Endpoint

```text
ws://127.0.0.1:8000/ws/events
```

---

# Deployment Guide

## Frontend Deployment (Vercel)

1. Push frontend to GitHub
2. Go to Vercel
3. Import GitHub repository
4. Select frontend folder
5. Deploy

---

## Backend Deployment (Render)

1. Push backend to GitHub
2. Create new Web Service in Render
3. Connect repository
4. Add environment variables
5. Deploy

---

# Environment Variables

## Backend

```env
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/analytics
REDIS_URL=redis://localhost:6379/0
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

# Testing Workflow

## 1. Login

* Open frontend login page
* Authenticate using credentials

## 2. Create Event

* Use Swagger API
* Create analytics event

## 3. Verify Live Update

* Dashboard updates automatically
* Event counts refresh in real time

---

# Assessment Deliverables

## GitHub Repository

Add your repository link here:

```text
https://github.com/your-username/analytics-platform
```

---

## Backend Deployment URL

Add your deployed backend URL:

```text
https://your-backend-url.com
```

---

## Frontend Deployment URL

Add your deployed frontend URL:

```text
https://your-frontend-url.vercel.app
```

---

# Future Improvements

* Role-based access control
* Event filtering
* Advanced analytics charts
* Kafka integration
* Kubernetes deployment
* CI/CD pipelines
* Monitoring and logging

---

# Conclusion

This project demonstrates:

* Modern full-stack architecture
* Real-time event processing
* Distributed systems concepts
* Background job processing
* WebSocket communication
* Async backend development
* Secure authentication
* Scalable analytics design

The platform was designed with scalability, modularity, and production-style architecture in mind.
