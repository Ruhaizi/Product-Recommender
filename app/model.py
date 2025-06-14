import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

class Recommender:
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.user_item_matrix = None
        self.similarity_matrix = None
        self.user_ids = []
        self.product_ids = []

    def load_data(self):
        df = pd.read_csv(self.data_path)
        self.user_item_matrix = df.pivot_table(index='user_id', columns='product_id', values='rating').fillna(0)
        self.user_ids = self.user_item_matrix.index.tolist()
        self.product_ids = self.user_item_matrix.columns.tolist()
        self.similarity_matrix = cosine_similarity(self.user_item_matrix)

    def recommend(self, user_id: int, top_n: int = 5):
        if user_id not in self.user_ids:
            return []

        user_idx = self.user_ids.index(user_id)
        similarity_scores = list(enumerate(self.similarity_matrix[user_idx]))

        # Sort users by similarity score (excluding self)
        similar_users = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:]

        # Get ratings from similar users
        similar_user_indices = [idx for idx, _ in similar_users[:3]]
        recommendations = self.user_item_matrix.iloc[similar_user_indices].mean(axis=0)

        # Remove products the user has already rated
        rated_products = self.user_item_matrix.loc[user_id]
        unrated_products = rated_products[rated_products == 0]
        recommendations = recommendations[unrated_products.index]

        return recommendations.sort_values(ascending=False).head(top_n).index.tolist()
