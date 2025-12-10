import pytest
import json
import csv
import sys
import os
from pathlib import Path

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", "..", "src"))

from lab05.json_csv import json_to_csv, csv_to_json


def test_json_to_csv_correct_conversion(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())


def test_csv_to_json_correct_conversion(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"

    with src.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerow({"name": "Alice", "age": "22"})
        writer.writerow({"name": "Bob", "age": "25"})

    csv_to_json(str(src), str(dst))

    result = json.loads(dst.read_text(encoding="utf-8"))

    assert len(result) == 2
    assert set(result[0].keys()) == {"name", "age"}
    assert result[1]["name"] == "Bob"


def test_empty_file_error(tmp_path: Path):
    empty_file = tmp_path / "empty.json"
    output = tmp_path / "out.csv"
    empty_file.write_text("")

    with pytest.raises(ValueError):
        json_to_csv(str(empty_file), str(output))


def test_invalid_json_error(tmp_path: Path):
    bad_file = tmp_path / "bad.json"
    output = tmp_path / "out.csv"
    bad_file.write_text("{invalid json")

    with pytest.raises(ValueError):
        json_to_csv(str(bad_file), str(output))


def test_file_not_found_error():
    with pytest.raises(FileNotFoundError):
        json_to_csv("несуществующий_файл.json", "выход.csv")

    with pytest.raises(FileNotFoundError):
        csv_to_json("несуществующий_файл.csv", "выход.json")
