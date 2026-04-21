import pickle
import os


class ModelPersistence:

    def __init__(self, path="models/svd_model.pkl"):
        self.path = path

    def save(self, model):
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        with open(self.path, "wb") as f:
            pickle.dump(model, f)

    def load(self):
        if not os.path.exists(self.path):
            raise FileNotFoundError("Model not found. Train first.")
        
        with open(self.path, "rb") as f:
            return pickle.load(f)