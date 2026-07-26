def validate_columns(df, required_columns):

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {', '.join(missing_columns)}"
        )

    print("✓ Required columns validated")


def validate_duplicates(df):

    duplicates = df.duplicated().sum()

    print(f"Duplicate rows found: {duplicates}")


def validate_missing_values(df):

    missing = df.isnull().sum()
    missing = missing[missing > 0]

    if missing.empty:
        print("No missing values found.")
    else:
        print("\nMissing values:")
        print(missing)


def validate_data_types(df, expected_dtypes):

    for column, expected in expected_dtypes.items():

        actual = str(df[column].dtype)

        if actual != expected:
            raise ValueError(
                f"{column}: expected {expected}, found {actual}"
            )

    print("✓ Data types validated")


def validate_negative_values(df, numeric_columns):

    for column in numeric_columns:

        negatives = (df[column] < 0).sum()

        print(f"{column}: {negatives} negative values")