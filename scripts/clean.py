import pandas as pd

def clean_column_names(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ","_")
    )
    return df

def clean_whitespace(df):

    text_columns = ["description", "country"]

    for column in text_columns:
        df[column] = (
            df[column]
            .astype(str)
            .str.strip()
        )

    return df
def clean_text_columns(df):

    text_columns = ["description", "country"]

    for column in text_columns:
        df[column] = (
            df[column]
            .astype(str)
            .str.strip()
            .str.title()
        )

    return df

def clean_numeric_columns(df):
    df["quantity"] = pd.to_numeric(df["quantity"])
    df["unitprice"] = pd.to_numeric(df["unitprice"])

    return df

def remove_cancelled_orders(df):
    df = df[~df["invoiceno"].astype(str).str.startswith("C")]
    return df

def remove_missing_customers(df):
    df =df.dropna(subset=["customerid"])

    return df

def remove_invalid_quantities(df):
    df = df[df["quantity"]>0]
    return df

def remove_invalid_prices(df):
    df = df[df["unitprice"]>0]
    return df

def remove_duplicates(df):

    df = df.drop_duplicates()

    return df