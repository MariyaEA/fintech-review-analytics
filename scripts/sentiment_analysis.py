if __name__ == "__main__":
    try:
        classify_sentiment(
            "data/processed/cleaned_reviews.csv",
            "data/processed/reviews_with_sentiment.csv"
        )
    except FileNotFoundError:
        print("Cleaned reviews file not found. Please run preprocessing first.")
        raise
    except Exception as e:
        print(f"Sentiment analysis failed: {e}")
        raise