# Fintech Review Analytics

## Project Overview
This project analyzes Google Play Store reviews for three Ethiopian mobile banking applications: Commercial Bank of Ethiopia, Bank of Abyssinia, and Dashen Bank. The goal is to understand customer sentiment, identify recurring user complaints, and generate product improvement recommendations.

## Target Banks
- Commercial Bank of Ethiopia
- Bank of Abyssinia
- Dashen Bank

## Scraping Methodology
Reviews were collected using the `google-play-scraper` Python package. The scraper collects review text, rating, review date, bank name, source, and review ID. The target was at least 400 reviews per bank.

## Data Fields
- review_id
- review
- rating
- date
- bank
- source

## Preprocessing
The preprocessing pipeline removes duplicate reviews using `review_id`, drops rows with missing review text or rating, removes empty reviews, and normalizes review dates to `YYYY-MM-DD`.

## Sentiment Analysis Progress
A sentiment analysis script was implemented using `distilbert-base-uncased-finetuned-sst-2-english`. The output includes `sentiment_label` and `sentiment_score`.

## Thematic Analysis Progress
A TF-IDF keyword extraction script was implemented using scikit-learn to identify important keywords and bigrams for each bank.

## Data Privacy and File Exclusion
Generated CSV files are excluded from GitHub using `.gitignore`. The repository contains scripts and documentation only, not raw or processed data files.

## Limitations
Scraping results may vary depending on Google Play availability, app review volume, network stability, and rate limits.