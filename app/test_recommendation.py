from app.infrastructure.data.dataset_loader import DatasetLoader
from app.infrastructure.model.svd_model import SVDRecommender
from app.domain.services.recommendation_service import RecommendationService

# carregar dados
loader = DatasetLoader()
df = loader.load("data/interactions.csv")

# treinar modelo
model = SVDRecommender()
model.train(df)

# criar serviço
service = RecommendationService(model, df)

# gerar recomendação
recommendations = service.recommend(user_id=1, n=3)

print("Recommendations:")
for r in recommendations:
    print(r)