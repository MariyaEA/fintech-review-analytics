import os
import pandas as pd
from sqlalchemy import create_engine


def insert_reviews_to_postgres(input_path):
    """
    Insert processed review data into PostgreSQL.
    DATABASE_URL should be stored as an environment variable.
    """

    database_url = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:password@localhost:5432/bank_reviews"
    )

    try:
        df = pd.read_csv(input_path)

        engine = create_engine(database_url)

        df.to_sql(
            "reviews",
            engine,
            if_exists="append",
            index=False
        )

        print("Data inserted successfully into PostgreSQL.")

    except FileNotFoundError:
        print("Processed review file not found. Run sentiment analysis first.")
        raise

    except Exception as e:
        print(f"Database insertion failed: {e}")
        raise


if __name__ == "__main__":
    insert_reviews_to_postgres("data/processed/reviews_with_sentiment.csv")