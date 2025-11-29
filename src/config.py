
import os
from dotenv import load_dotenv
load_dotenv()
APP_IDS = {
    'CBE': os.getenv('CBE_APP_ID', 'com.combanketh.mobilebanking'),
    'BOA': os.getenv('BOA_APP_ID', 'com.boa.boaMobileBanking'),
    'DASHEN': os.getenv('DASHEN_APP_ID', 'com.cr2.amolelight')

}

# Bank Names Mapping
BANK_NAMES = {
    'CBE': 'Commercial Bank of Ethiopia',
    'BOA': 'Bank of Abysinia',
    'DASHEN': 'Dashen'
}

# Scraping Configuration
SCRAPING_CONFIG = {
    'reviews_per_bank': int(os.getenv('REVIEWS_PER_BANK', 400)),
    'max_retries': int(os.getenv('MAX_RETRIES', 3)),
    'lang': 'en',
    'country': 'et'  # Ethiopia
}

# File Paths
DATA_PATHS = {
    'raw': r"C:\Users\user\Desktop\Project\Mobile-Banking\data\raw",
    'processed': r"C:\Users\user\Desktop\Project\Mobile-Banking\data\processed",
    'raw_reviews': r"C:\Users\user\Desktop\Project\Mobile-Banking\data\raw\reviews_raw.csv",
    'processed_reviews': r"C:\Users\user\Desktop\Project\Mobile-Banking\data\processed\reviews_processed.csv",
    'sentiment_results': r"C:\Users\user\Desktop\Project\Mobile-Banking\data\processed\reviews_with_sentiment.csv",
    'final_results': r"C:\Users\user\Desktop\Project\Mobile-Banking\data\processed\reviews_final.csv"
}








