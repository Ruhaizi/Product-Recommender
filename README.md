# Real-Time Product Recommendation System

This is a modular product recommendation system that offers both a lightweight implementation using pandas and scikit-learn, and a scalable version powered by PySpark’s ALS algorithm. It supports REST APIs via FastAPI and simulates real-time data ingestion using a mock event stream.

This project is a personal attempt to build a simple but practical product recommendation system from scratch. It started as a way to understand how collaborative filtering works and gradually evolved into a more complete system with both lightweight and scalable implementations.

The system can recommend products to users based on their past behavior, using either basic cosine similarity or Spark’s ALS algorithm. It simulates real-time updates by adding new events to the data, and you can interact with the system through APIs or a small UI built with Streamlit.

Everything runs locally and is built to be easy to test, understand, and improve. It's meant to showcase my ability to combine data processing, backend APIs, and basic ML logic into a working product.


## Tech Stack

- FastAPI – API layer for serving recommendations  
- Scikit-learn – Cosine similarity for user-based filtering  
- PySpark – ALS-based collaborative filtering (scalable version)  
- Pandas – Lightweight CSV manipulation  
- Streamlit – Optional frontend UI  
- Uvicorn – ASGI server  
- CSV files – Used for persistent, mock database  
- Python script – Simulated Kafka-style event injection  

## Features

- Two Recommendation Engines:
  - `/recommendations?user_id=X` – Scikit-learn (cosine similarity)
  - `/spark-recommendations?user_id=X` – PySpark ALS-based (Spark backend)
- Fallback logic for new users (cold start)
- Real-time simulation: Inject new events via `event_processor.py`
- Modular design: Swap models without changing API structure
- Optional UI: Query recommendations using a Streamlit interface

## Setup Instructions

```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
