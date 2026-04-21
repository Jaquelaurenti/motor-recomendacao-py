import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

class ContentBasedRecommender:

    def __init__(self, items_df):
        self.items_df = items_df
        self.similarity_matrix = self._build_similarity()

    def _build_similarity(self):
        # one-hot encoding simples
        features = pd.get_dummies(self.items_df['category'])

        similarity = cosine_similarity(features)

        return pd.DataFrame(
            similarity,
            index=self.items_df['item_id'],
            columns=self.items_df['item_id']
        )

    def get_similarity(self, item_a, item_b):
        try:
            return self.similarity_matrix.loc[item_a, item_b]
        except KeyError:
            return 0.0