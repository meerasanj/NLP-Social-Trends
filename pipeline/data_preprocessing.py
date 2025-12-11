# Clean raw Kaggle CSV and output a normalized processed_data.csv
import pandas as pd
import re
import os

# Path configuration
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)

# Define paths to the data folder
INPUT_FILENAME = os.path.join(PROJECT_ROOT, 'data', 'raw_kaggle.csv')
OUTPUT_FILENAME = os.path.join(PROJECT_ROOT, 'data', 'processed_data.csv')

# Cleans raw text by removing URLs, emojis, and extra whitespace.
def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = re.sub(r'http\S+|www\.\S+', '', text)
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    text = text.replace('\n', ' ').replace('\t', ' ')
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Renames columns to a standard format used by the app.
def normalize_structure(df):
    column_mapping = {
        'Text': 'text',
        'Sentiment': 'sentiment',
        'Platform': 'platform',
        'Hashtags': 'hashtags',
        'Country': 'country',
        'Timestamp': 'timestamp',
        'Likes': 'likes',
        'Retweets': 'retweets'
    }
    df = df.rename(columns=column_mapping)
    required_columns = ['text', 'sentiment', 'platform', 'hashtags', 'country', 'timestamp', 'likes', 'retweets']
    existing_cols = [col for col in required_columns if col in df.columns]
    return df[existing_cols]

# Main function to run the data preprocessing pipeline
def main():
    print(f"Looking for data at: {INPUT_FILENAME}")
    
    if not os.path.exists(INPUT_FILENAME):
        print(f"Error: Could not find {INPUT_FILENAME}")
        print("Make sure 'raw_kaggle.csv' is inside the 'data' folder.")
        return

    # Load the raw data and normalize the structure
    try:
        df = pd.read_csv(INPUT_FILENAME)
        print(f"Raw data loaded: {len(df)} rows.")
        
        df = normalize_structure(df)

        if 'text' in df.columns:
            print("Cleaning text columns...")
            df['text'] = df['text'].apply(clean_text)
            
        if 'sentiment' in df.columns:
            df['sentiment'] = df['sentiment'].astype(str).str.strip()
            
        df = df[df['text'] != '']
        
        for col in ['platform', 'hashtags', 'country']:
            if col in df.columns:
                df[col] = df[col].astype(str).str.strip()

        # Save to new CSV
        df.to_csv(OUTPUT_FILENAME, index=False)
        print(f"Success! Processed data saved to: {OUTPUT_FILENAME}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()