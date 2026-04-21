import pandas as pd


class DatasetLoader:

    REQUIRED_COLUMNS = {"user_id", "item_id", "rating"}

    def load(self, path: str) -> pd.DataFrame:
        df = pd.read_csv(path)
        self._validate(df)
        return df

    def _validate(self, df: pd.DataFrame):
        missing = self.REQUIRED_COLUMNS - set(df.columns)
        if missing:
            raise ValueError(f"Missing columns: {missing}")

        if df.isnull().values.any():
            raise ValueError("Dataset contains null values")