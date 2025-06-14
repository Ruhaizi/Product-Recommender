# Real-Time Product Recommendation System

This is a solo-built, FastAPI-based product recommendation system that uses collaborative filtering to suggest relevant products to users. The system includes a simulated event ingestion pipeline to mimic real-time updates using a Python script.

## Tech Stack

- FastAPI (REST API)
- Pandas and Scikit-learn (Collaborative filtering)
- Simulated Kafka-like ingestion (custom Python script)
- CSV file for persistent data storage
- Uvicorn for local deployment

## Features

- `/recommendations?user_id=XYZ` returns the top 5 personalized product recommendations for a given user
- Uses user-user cosine similarity for collaborative filtering
- Includes fallback logic to recommend popular unrated products for cold-start users
- Simulates real-time data ingestion with `event_processor.py`

## Getting Started

### Setup

```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
