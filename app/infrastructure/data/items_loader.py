import pandas as pd


class ItemsLoader:

    REQUIRED_COLUMNS = {"item_id", "category"}

    def load(self, path: str) -> pd.DataFrame:
        df = pd.read_csv(path)
        self._validate(df)
        return df

    def _validate(self, df: pd.DataFrame):
        missing = self.REQUIRED_COLUMNS - set(df.columns)
        if missing:
            raise ValueError(f"Missing columns: {missing}")

        if df.empty:
            raise ValueError("Items dataset is empty")