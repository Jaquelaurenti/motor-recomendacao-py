from surprise import SVD, Dataset, Reader


class SVDRecommender:
    """
    Modelo de recomendação baseado em Matrix Factorization (SVD)
    """

    def __init__(self):
        self.model = SVD()
        self.trained = False

    def train(self, df):
        """
        Treina o modelo com um DataFrame contendo:
        user_id, item_id, rating
        """
        self._validate_dataframe(df)

        reader = Reader(rating_scale=(1, 5))

        data = Dataset.load_from_df(
            df[['user_id', 'item_id', 'rating']],
            reader
        )

        trainset = data.build_full_trainset()

        self.model.fit(trainset)
        self.trained = True

    def predict(self, user_id: int, item_id: int) -> float:
        """
        Prediz a nota que um usuário daria a um item
        """
        if not self.trained:
            raise RuntimeError("Model not trained yet")

        prediction = self.model.predict(user_id, item_id)
        return prediction.est

    def _validate_dataframe(self, df):
        required_columns = {"user_id", "item_id", "rating"}

        missing = required_columns - set(df.columns)
        if missing:
            raise ValueError(f"Missing columns: {missing}")

        if df.empty:
            raise ValueError("Dataset is empty")