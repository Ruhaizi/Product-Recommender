import streamlit as st
import requests

st.set_page_config(page_title="Spark Product Recommender", layout="centered")

st.title("⚡ Spark-Based Product Recommendation System")

st.markdown("Enter a user ID to get product recommendations from the Spark ALS model.")

user_id = st.number_input("Enter User ID:", min_value=1, step=1)

if st.button("Get Recommendations"):
    try:
        with st.spinner("Fetching recommendations..."):
            response = requests.get(
                "http://127.0.0.1:8001/spark-recommendations", params={"user_id": user_id}
            )
            if response.status_code == 200:
                data = response.json()
                st.success(f"Top Recommendations for User {user_id}:")
                st.json(data["recommended_product_ids"])
            elif response.status_code == 404:
                st.warning("No recommendations found for this user.")
            else:
                st.error(f"Error: {response.status_code}")
    except Exception as e:
        st.error(f"Request failed: {str(e)}")
