from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS
from pyspark.sql.functions import col
import os


class SparkRecommender:
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.spark = SparkSession.builder.appName("ProductRecommender").getOrCreate()
        self.model = None
        self.df = None

    def load_data_and_train(self):
        self.df = self.spark.read.csv(self.data_path, header=True, inferSchema=True)
        self.df = self.df.dropna()

        als = ALS(
            userCol="user_id",
            itemCol="product_id",
            ratingCol="rating",
            maxIter=10,
            regParam=0.1,
            coldStartStrategy="drop",
            nonnegative=True
        )

        self.model = als.fit(self.df)

    def recommend(self, user_id: int, top_n: int = 5):
        user_df = self.spark.createDataFrame([{"user_id": user_id}])
        recommendations = self.model.recommendForUserSubset(user_df, top_n).collect()

        if not recommendations:
            return []

        product_list = recommendations[0]["recommendations"]
        return [row["product_id"] for row in product_list]
