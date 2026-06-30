from sqlalchemy import create_engine
import pandas as pd

from config.settings import DATABASE_URL

def load_postgres(
    parquet_path: str,
    table_name: str
):

    engine = create_engine(DATABASE_URL)

    df = pd.read_parquet(parquet_path)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )