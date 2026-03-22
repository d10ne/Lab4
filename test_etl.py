import pandas as pd
import os

from logistics_etl import clean_logistics_data_from_csv


def test_etl_load_from_csv():
    file_path = "uber-raw-data-apr14.csv"

    # проверка: файл существует
    assert os.path.exists(file_path), "CSV file not found"

    # запуск ETL
    df = clean_logistics_data_from_csv(file_path)

    # ✅ проверка: DataFrame не пустой
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0

    # ✅ проверка: нет полностью пустых строк
    assert not df.isnull().all(axis=1).any()

    # ✅ проверка структуры
    expected_columns = ["Lat", "Lon"]
    for col in expected_columns:
        assert col in df.columns