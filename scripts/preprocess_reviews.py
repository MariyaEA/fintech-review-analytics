import pandas as pd


def preprocess_reviews(input_path, output_path):
    """
    Clean and preprocess scraped Google Play reviews.
    """

    # Load raw dataset
    df = pd.read_csv(input_path)

    print("Initial dataset shape:", df.shape)

    # Remove duplicate reviews using review_id
    df = df.drop_duplicates(subset="review_id")

    print("After removing duplicates:", df.shape)

    # Remove rows missing review text or rating
    df = df.dropna(subset=["review", "rating"])

    print("After removing missing values:", df.shape)

    # Normalize date format
    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

    # Remove empty review text
    df = df[df["review"].str.strip() != ""]

    print("Final cleaned dataset shape:", df.shape)

    # Save cleaned dataset
    df.to_csv(output_path, index=False)

    print(f"\nCleaned data saved to: {output_path}")


if __name__ == "__main__":
    preprocess_reviews(
        "data/raw/raw_reviews.csv",
        "data/processed/cleaned_reviews.csv"
    )