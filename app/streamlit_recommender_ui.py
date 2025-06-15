import streamlit as st
import requests

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://plus.unsplash.com/premium_photo-1738424351748-0b7486626a15?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    </style>
    """,
    unsafe_allow_html=True
)


st.title("Product Recommendation System")

# Input field for user_id
user_id = st.text_input("Enter User ID:", "")

if st.button("Get Recommendations"):
    if user_id.strip() == "":
        st.warning("Please enter a valid user ID.")
    else:
        try:
            # Call the FastAPI backend
            response = requests.get(f"http://127.0.0.1:8000/recommendations?user_id={user_id}")
            
            if response.status_code == 200:
                recommendations = response.json().get("recommended_product_ids", [])
                if recommendations:
                    st.success(f"Top Recommendations for User {user_id}:")
                    for product_id in recommendations:
                        st.markdown(f"- Product ID: `{product_id}`")
                else:
                    st.info("No recommendations found for this user.")
            else:
                st.error(response.json().get("detail", "An error occurred."))
        except Exception as e:
            st.error(f"Failed to connect to backend: {e}")
