import pandas as pd
import numpy as np
from google_play_scraper import Sort, reviews_all
import os

# Assuming your config.py exists and has DATA_PATHS dictionary
from config import DATA_PATHS

class PlayStoreScraper:
    def __init__(self):
        pass

    def scrape_reviews(self, app_package, max_reviews=400):
        print(f"\n🔍 Scraping: {app_package} ...")
        try:
            data = reviews_all(
                app_package,
                sleep_milliseconds=0,
                lang="en",
                country="us",
                sort=Sort.NEWEST
            )

            df = pd.DataFrame(data)
            if df.empty:
                print(f"⚠ No reviews found for {app_package}")
                return pd.DataFrame()

            # Keep only the necessary columns
            df = df[["userName", "content", "score", "at"]]

            # Rename columns to match preprocessor
            df = df.rename(columns={
                "userName": "user_name",
                "content": "review_text",
                "score": "rating",
                "at": "review_date"
            })

            # Add placeholder columns
            df["review_id"] = range(1, len(df)+1)
            df["bank_code"] = app_package.upper()
            df["bank_name"] = app_package.upper()
            df["thumbs_up"] = 0
            df["reply_content"] = ""
            df["source"] = "Google Play"

            return df[:max_reviews]

        except Exception as e:
            print(f"❌ Error scraping {app_package}: {e}")
            return pd.DataFrame()

    def scrape_all_banks(self):
        apps = [
            "com.sc.awashpay",
            "com.combanketh.et",
            "com.ahabank.mobilebanking",
            "com.abaybank.abyssinialive",
            "com.oromiamobile.oromiaportal",
        ]

        all_data = []
        for app in apps:
            df = self.scrape_reviews(app, max_reviews=400)
            if not df.empty:
                all_data.append(df)

        if all_data:
            final_df = pd.concat(all_data, ignore_index=True)
            # Save to raw_reviews path for preprocessor
            os.makedirs(os.path.dirname(DATA_PATHS['raw_reviews']), exist_ok=True)
            final_df.to_csv(DATA_PATHS['raw_reviews'], index=False)
            print(f"\n✅ Scraped data saved to {DATA_PATHS['raw_reviews']}")
            return final_df
        else:
            print("⚠ No data scraped for any bank")
            return pd.DataFrame()

def main():
    scraper = PlayStoreScraper()
    df = scraper.scrape_all_banks()
    print(df.head())
    return df

if __name__ == "__main__":
    final_df = main()
