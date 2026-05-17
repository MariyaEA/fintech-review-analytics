from google_play_scraper import reviews, Sort
import pandas as pd


BANK_APPS = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}


def scrape_bank_reviews(app_id, bank_name, count=500):
    """
    Scrape reviews from Google Play Store.
    """

    result, _ = reviews(
        app_id,
        lang="en",
        country="et",
        sort=Sort.NEWEST,
        count=count
    )

    cleaned_reviews = []

    for review in result:
        cleaned_reviews.append({
            "review_id": review["reviewId"],
            "review": review["content"],
            "rating": review["score"],
            "date": review["at"].strftime("%Y-%m-%d"),
            "bank": bank_name,
            "source": "Google Play"
        })

    return pd.DataFrame(cleaned_reviews)


def main():
    all_reviews = []

    for bank_name, app_id in BANK_APPS.items():
        print(f"Scraping reviews for {bank_name}...")

        df = scrape_bank_reviews(app_id, bank_name)

        print(f"Collected {len(df)} reviews for {bank_name}")

        all_reviews.append(df)

    final_df = pd.concat(all_reviews, ignore_index=True)

    print("\nTotal reviews collected:")
    print(final_df.shape)

    # Save raw reviews locally
    final_df.to_csv("data/raw/raw_reviews.csv", index=False)

    print("\nRaw reviews saved successfully.")


if __name__ == "__main__":
    main()