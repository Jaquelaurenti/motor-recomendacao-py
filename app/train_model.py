from app.infrastructure.data.dataset_loader import DatasetLoader
from app.infrastructure.model.svd_model import SVDRecommender
from app.infrastructure.model.model_persistence import ModelPersistence

loader = DatasetLoader()
df = loader.load("data/interactions.csv")

model = SVDRecommender()
model.train(df)

persistence = ModelPersistence()
persistence.save(model)

print("Model trained and saved ✅")