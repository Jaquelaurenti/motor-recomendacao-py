from surprise import Dataset, Reader, SVD, accuracy
from surprise.model_selection import train_test_split, cross_validate

from app.infrastructure.data.dataset_loader import DatasetLoader


def run_evaluation():
    # carregar dados
    loader = DatasetLoader()
    df = loader.load("data/interactions.csv")

    # preparar dataset
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(df[['user_id', 'item_id', 'rating']], reader)

    # modelo
    model = SVD()

    print("\n🔹 Avaliação simples (train/test split):")
    
    # split simples
    trainset, testset = train_test_split(data, test_size=0.2)
    model.fit(trainset)
    predictions = model.test(testset)
    accuracy.rmse(predictions)

    print("\n🔹 Cross Validation (mais confiável):")

    # cross validation
    cross_validate(
        model,
        data,
        measures=['RMSE'],
        cv=3,
        verbose=True
    )


if __name__ == "__main__":
    run_evaluation()