import pandas as pd

def clean_logistics_data_from_csv(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    return df


if __name__ == "__main__":
    file_path = "uber-raw-data-apr14.csv"

    cleaned_df = clean_logistics_data_from_csv(file_path)

    print(cleaned_df)