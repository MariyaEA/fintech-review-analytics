import pandas as pd
from transformers import pipeline


def classify_sentiment(input_path, output_path):
    df = pd.read_csv(input_path)

    sentiment_pipeline = pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english"
    )

    labels = []
    scores = []

    for review in df["review"].astype(str):
        result = sentiment_pipeline(review[:512])[0]

        label = result["label"].lower()
        score = result["score"]

        if score < 0.60:
            label = "neutral"

        labels.append(label)
        scores.append(score)

    df["sentiment_label"] = labels
    df["sentiment_score"] = scores

    df.to_csv(output_path, index=False)
    print(f"Sentiment results saved to: {output_path}")
    print(df[["bank", "rating", "sentiment_label", "sentiment_score"]].head())


if __name__ == "__main__":
    classify_sentiment(
        "data/processed/cleaned_reviews.csv",
        "data/processed/reviews_with_sentiment.csv"
    )