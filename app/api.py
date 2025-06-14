from fastapi import FastAPI, HTTPException, Query
from model import Recommender

app = FastAPI()

# Initialize recommender
recommender = Recommender(data_path="data/user_events.csv")
recommender.load_data()

@app.get("/")
def read_root():
    return {"message": "Product Recommendation API is running!"}

@app.get("/recommendations")
def get_recommendations(user_id: int = Query(..., description="User ID to get recommendations for")):
    try:
        recommendations = recommender.recommend(user_id=user_id, top_n=5)
        if not recommendations:
            raise HTTPException(status_code=404, detail="No recommendations found for this user.")
        return {"user_id": user_id, "recommended_product_ids": recommendations}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=False)
