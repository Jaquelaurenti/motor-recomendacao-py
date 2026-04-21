from fastapi import APIRouter

from app.application.use_cases.get_recommendations import GetRecommendations
from app.domain.services.recommendation_service import RecommendationService
from app.infrastructure.data.dataset_loader import DatasetLoader
from app.infrastructure.model.model_persistence import ModelPersistence
from app.domain.services.content_based import ContentBasedRecommender
from app.infrastructure.data.items_loader import ItemsLoader

router = APIRouter()

# 📊 carregar dados (continua necessário)
loader = DatasetLoader()
df = loader.load("data/interactions.csv")

# 🧠 carregar modelo já treinado
persistence = ModelPersistence()
model = persistence.load()   # ✅ aqui está a mudança principal

# 🔗 montar serviço
service = RecommendationService(model, df)
use_case = GetRecommendations(service)


@router.get("/recommendations/{user_id}")
def get_recommendations(user_id: int):
    results = use_case.execute(user_id)

    return {
        "user_id": user_id,
        "recommendations": results
    }
    
items_loader = ItemsLoader()
items_df = items_loader.load("data/items.csv")

content_model = ContentBasedRecommender(items_df)

service = RecommendationService(model, df, content_model)

