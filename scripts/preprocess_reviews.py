if __name__ == "__main__":
    try:
        preprocess_reviews(
            "data/raw/raw_reviews.csv",
            "data/processed/cleaned_reviews.csv"
        )
    except FileNotFoundError:
        print("Input file not found. Please run the scraping script first.")
        raise
    except Exception as e:
        print(f"Preprocessing failed: {e}")
        raise