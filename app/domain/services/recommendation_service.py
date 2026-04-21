class RecommendationService:

    def __init__(self, model, data, content_model=None):
        self.model = model
        self.data = data
        self.content_model = content_model

    def recommend(self, user_id: int, n: int = 5):
        all_items = self.data['item_id'].unique()
        seen_items = self.data[self.data['user_id'] == user_id]['item_id'].values

        recommendations = []

        for item in all_items:
            if item not in seen_items:
                cf_score = self.model.predict(user_id, item)

                content_score = 0
                if self.content_model:
                    for seen_item in seen_items:
                        content_score += self.content_model.get_similarity(item, seen_item)

                    content_score = content_score / len(seen_items)

                final_score = (0.7 * cf_score) + (0.3 * content_score)


                recommendations.append({
                    "item_id": int(item),
                    "score": float(final_score)
                })

        recommendations.sort(key=lambda x: x["score"], reverse=True)

        return recommendations[:n]