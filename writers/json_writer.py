import json
from pathlib import Path
from datetime import datetime


def write_json(data, path: str):
    file_path = Path(path)

    file_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    payload = {
        "metadata": {
            "generated_at": datetime.now().isoformat(),
            "source": "mossoro_transparency",
        },
        "data": data,
    }

    with open(
        file_path,
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            payload,
            file,
            ensure_ascii=False,
            indent=4,
        )