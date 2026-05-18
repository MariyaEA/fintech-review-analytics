import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


OUTPUT_DIR = "reports/figures"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_data():
    """
    Load processed review and keyword datasets.
    """

    try:
        reviews = pd.read_csv(
            "data/processed/reviews_with_sentiment.csv"
        )

        keywords = pd.read_csv(
            "data/processed/theme_keywords.csv"
        )

        return reviews, keywords

    except FileNotFoundError as e:
        print(f"Required data file missing: {e}")
        raise


def plot_sentiment_distribution(df):
    """
    Generate sentiment distribution by bank.
    """

    plt.figure(figsize=(8, 5))

    sns.countplot(
        data=df,
        x="bank",
        hue="sentiment_label"
    )

    plt.title("Sentiment Distribution by Bank")
    plt.xlabel("Bank")
    plt.ylabel("Number of Reviews")
    plt.legend(title="Sentiment")

    plt.tight_layout()

    plt.savefig(
        f"{OUTPUT_DIR}/sentiment_distribution_by_bank.png",
        dpi=300
    )

    plt.close()


def plot_rating_distribution(df):
    """
    Generate rating distribution by bank.
    """

    plt.figure(figsize=(8, 5))

    sns.countplot(
        data=df,
        x="rating",
        hue="bank"
    )

    plt.title("Rating Distribution by Bank")
    plt.xlabel("Rating")
    plt.ylabel("Number of Reviews")
    plt.legend(title="Bank")

    plt.tight_layout()

    plt.savefig(
        f"{OUTPUT_DIR}/rating_distribution_by_bank.png",
        dpi=300
    )

    plt.close()


def plot_top_keywords(keywords):
    """
    Generate top TF-IDF keyword chart.
    """

    top_keywords = (
        keywords
        .sort_values("tfidf_score", ascending=False)
        .head(15)
    )

    plt.figure(figsize=(9, 6))

    sns.barplot(
        data=top_keywords,
        x="tfidf_score",
        y="keyword",
        hue="bank",
        dodge=False
    )

    plt.title("Top TF-IDF Keywords Across Bank Reviews")
    plt.xlabel("TF-IDF Score")
    plt.ylabel("Keyword")
    plt.legend(title="Bank")

    plt.tight_layout()

    plt.savefig(
        f"{OUTPUT_DIR}/top_tfidf_keywords.png",
        dpi=300
    )

    plt.close()


def main():
    reviews, keywords = load_data()

    plot_sentiment_distribution(reviews)
    plot_rating_distribution(reviews)
    plot_top_keywords(keywords)

    print("Visualizations generated successfully.")


if __name__ == "__main__":

    try:
        main()

    except Exception as e:
        print(f"Visualization generation failed: {e}")
        raise