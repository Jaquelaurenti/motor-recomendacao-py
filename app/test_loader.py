from infrastructure.data.dataset_loader import DatasetLoader

loader = DatasetLoader()
df = loader.load("data/interactions.csv")

print(df.head())