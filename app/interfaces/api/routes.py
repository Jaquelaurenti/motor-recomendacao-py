from fastapi import APIRouter
from app.application.use_cases.get_recommendations import GetRecommendations
from app.domain.services.recommendation_service import RecommendationService
from app.infrastructure.data.dataset_loader import DatasetLoader
from app.infrastructure.model.svd_model import SVDRecommender

router = APIRouter()

# 🔥 inicialização (simples por enquanto)
loader = DatasetLoader()
df = loader.load("data/interactions.csv")

model = SVDRecommender()
model.train(df)

service = RecommendationService(model, df)
use_case = GetRecommendations(service)


@router.get("/recommendations/{user_id}")
def get_recommendations(user_id: int):
    results = use_case.execute(user_id)

    return {
        "user_id": user_id,
        "recommendations": results
    }