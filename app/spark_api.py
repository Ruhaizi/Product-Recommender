from fastapi import FastAPI, HTTPException, Query
from spark_model import SparkRecommender

app = FastAPI(title="Spark-Based Product Recommendation System")

# Initialize Spark-based recommender
recommender = SparkRecommender(data_path="data/user_events.csv")
recommender.load_data_and_train()

@app.get("/")
def read_root():
    return {"message": "Spark-based Recommendation System is running!"}

@app.get("/spark-recommendations")
def get_spark_recommendations(user_id: int = Query(..., description="User ID for recommendations")):
    try:
        recommendations = recommender.recommend(user_id=user_id, top_n=5)
        if not recommendations:
            raise HTTPException(status_code=404, detail="No recommendations found for this user.")
        return {"user_id": user_id, "recommended_product_ids": recommendations}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("spark_api:app", host="127.0.0.1", port=8001, reload=False)
