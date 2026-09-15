import pandas as pd
from pathlib import Path


def load_sales_data(input_folder):

    input_folder = Path(input_folder)

    csv_files = list(input_folder.glob("*.csv"))

    if not csv_files:
        raise FileNotFoundError(
            "No CSV files found in the input folder."
        )

    all_data = []

    for file in csv_files:

        print(f"Reading: {file.name}")

        df = pd.read_csv(file)

        df["Source_File"] = file.name

        all_data.append(df)

    combined_df = pd.concat(
        all_data,
        ignore_index=True
    )

    return combined_df


def clean_sales_data(df):

    df = df.copy()

    df["Date"] = pd.to_datetime(
        df["Date"],
        errors="coerce"
    )

    df["Quantity"] = pd.to_numeric(
        df["Quantity"],
        errors="coerce"
    )

    df["Price"] = pd.to_numeric(
        df["Price"],
        errors="coerce"
    )

    df = df.dropna(
        subset=[
            "Date",
            "Customer",
            "Product",
            "Category",
            "Quantity",
            "Price"
        ]
    )

    df["Total"] = (
        df["Quantity"] * df["Price"]
    )

    return df