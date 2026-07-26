import pandas as pd 
from scripts.extract import extract_data
from scripts.report import generate_reports

from scripts.logger import setup_logger
from scripts.validate import (
    validate_columns,
    validate_duplicates,
    validate_missing_values,
    validate_data_types,
    validate_negative_values,
)

from scripts.clean import (
    clean_column_names,
    clean_whitespace,
    clean_text_columns,
    clean_numeric_columns,
    remove_cancelled_orders,
    remove_missing_customers,
    remove_invalid_quantities,
    remove_invalid_prices,
    remove_duplicates,
)

from scripts.transform import transform_data

from database.database import (
    create_connection,
    load_data,
    close_connection,
)

logger = setup_logger()


def main():

    logger.info("=" * 60)
    logger.info("ETL Pipeline Started")

    try:
        # ===========================
        # Extract
        # ===========================
        file_path = "data/raw/Online Retail.xlsx"

        df = extract_data(file_path)

        logger.info(f"Extraction completed successfully. Rows extracted: {len(df)}")

        # ===========================
        # Validation
        # ===========================

        required_columns = [
            "InvoiceNo",
            "StockCode",
            "Description",
            "Quantity",
            "InvoiceDate",
            "UnitPrice",
            "CustomerID",
            "Country",
        ]

        expected_dtypes = {
            "InvoiceNo": "object",
            "StockCode": "object",
            "Description": "object",
            "Quantity": "int64",
            "InvoiceDate": "datetime64[ns]",
            "UnitPrice": "float64",
            "CustomerID": "float64",
            "Country": "object",
        }

        validate_columns(df, required_columns)
        validate_duplicates(df)
        validate_missing_values(df)
        validate_data_types(df, expected_dtypes)
        validate_negative_values(df, ["Quantity", "UnitPrice"])

        logger.info("Validation completed successfully.")

        # ===========================
        # Cleaning
        # ===========================

        df = clean_column_names(df)
        df = clean_whitespace(df)
        df = clean_text_columns(df)
        df = clean_numeric_columns(df)

        df = remove_duplicates(df)
        df = remove_cancelled_orders(df)
        df = remove_missing_customers(df)
        df = remove_invalid_quantities(df)
        df = remove_invalid_prices(df)

        logger.info(f"Cleaning completed successfully. Rows after cleaning: {len(df)}")

        # ===========================
        # Transformation
        # ===========================

        df = transform_data(df)

        logger.info("Transformation completed successfully.")

        # ===========================
        # Load
        # ===========================

        logger.info("Connecting to SQLite database.")

        connection = create_connection("database/retail.db")

        load_data(df, connection)
        df.to_csv("data/processed/retail_cleaned.csv",index=False)

        logger.info("Data loaded into SQLite successfully.")

        close_connection(connection)

        logger.info("Database connection closed.")

        logger.info("ETL Pipeline completed successfully.")
        logger.info("=" * 60)

    except Exception as e:
        logger.error(f"ETL Pipeline Failed: {e}", exc_info=True)
        raise


if __name__ == "__main__":
    main()