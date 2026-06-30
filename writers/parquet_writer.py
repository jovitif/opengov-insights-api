import pandas as pd
from pathlib import Path

def write_parquet(data, path):

    file_path = Path(path)

    file_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df = pd.DataFrame(data)

    df.to_parquet(
        file_path,
        index=False
    )