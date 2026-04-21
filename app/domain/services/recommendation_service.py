class RecommendationService:

    def __init__(self, model, data):
        self.model = model
        self.data = data

    def recommend(self, user_id: int, n: int = 5):
        all_items = self.data['item_id'].unique()

        seen_items = self.data[self.data['user_id'] == user_id]['item_id'].values

        recommendations = []

        for item in all_items:
            if item not in seen_items:
                score = self.model.predict(user_id, item)

                recommendations.append({
                    "item_id": int(item),
                    "score": float(score)
                })

        recommendations.sort(key=lambda x: x["score"], reverse=True)

        return recommendations[:n]