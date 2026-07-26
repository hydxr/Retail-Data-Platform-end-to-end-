import pandas as pd


def calculate_revenue(df):
    df["revenue"] = df["quantity"] * df["unitprice"]
    return df


def create_order_month(df):
    df["order_month"] = df["invoicedate"].dt.month_name()
    return df


def create_order_year(df):
    df["order_year"] = df["invoicedate"].dt.year
    return df


def create_order_day(df):
    df["order_day"] = df["invoicedate"].dt.day_name()
    return df


def create_weekend_flag(df):
    df["is_weekend"] = df["order_day"].isin(["Saturday", "Sunday"])
    return df


def create_high_value_order(df):
    df["high_value_order"] = df["revenue"] >= 1000
    return df


def transform_data(df):

    df = calculate_revenue(df)

    df = create_order_month(df)

    df = create_order_year(df)

    df = create_order_day(df)

    df = create_weekend_flag(df)

    df = create_high_value_order(df)

    return df