if __name__ == "__main__":
    try:
        extract_keywords(
            "data/processed/reviews_with_sentiment.csv",
            "data/processed/theme_keywords.csv"
        )
    except FileNotFoundError:
        print("Sentiment output file not found. Please run sentiment analysis first.")
        raise
    except Exception as e:
        print(f"Theme extraction failed: {e}")
        raise