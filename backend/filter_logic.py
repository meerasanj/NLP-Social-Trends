# Provide reusable filtering helpers for GUI actions (filters panel)

import pandas as pd
from typing import Optional, List

# Central entry point for filtering logic
# Filter DataFrame by platform/country/likes/retweets/sentiment
def filter_dataframe(
    df: pd.DataFrame, 
    platform: Optional[str] = None, 
    country: Optional[str] = None, 
    min_likes: Optional[int] = None,
    min_retweets: Optional[int] = None,
    sentiment: Optional[str] = None
) -> pd.DataFrame:
    if df is None or df.empty:
        print("[FilterLogic] Warning: Cannot filter. Input DataFrame is empty.")
        return pd.DataFrame()
        
    filtered_df = df.copy()
    
    # Filter by Platform (Uses 'Platform' column)
    if platform and 'Platform' in filtered_df.columns:
        filtered_df = filtered_df[filtered_df['Platform'].astype(str).str.lower() == platform.lower()]

    # Filter by Country (Uses 'Location' column.
    if country and 'Location' in filtered_df.columns:
        filtered_df = filtered_df[filtered_df['Location'].astype(str).str.lower() == country.lower()]
        
    # Filter by Minimum Likes (Uses 'Likes' column, assumes numeric)
    if min_likes is not None and min_likes >= 0 and 'Likes' in filtered_df.columns:
        # Use >= operator for filtering minimum values
        filtered_df = filtered_df[filtered_df['Likes'] >= min_likes]

    # Filter by Minimum Retweets - Uses 'Retweets' column, assumes numeric
    if min_retweets is not None and min_retweets >= 0 and 'Retweets' in filtered_df.columns:
        filtered_df = filtered_df[filtered_df['Retweets'] >= min_retweets]
        
    # 5. Filter by Sentiment - Uses 'Sentiment' column.
    if sentiment and 'Sentiment' in filtered_df.columns:
        filtered_df = filtered_df[filtered_df['Sentiment'].astype(str).str.lower() == sentiment.lower()]
        
    # Check if filtering resulted in an empty set
    if filtered_df.empty and not df.empty:
        print("[FilterLogic] Filter returned no posts matching criteria.")
        
    return filtered_df

# Helper: filter by platform
def filter_by_platform(df: pd.DataFrame, platform_name: str) -> pd.DataFrame:
    return filter_dataframe(df, platform=platform_name)

# Helper: filter by country (Location)
def filter_by_country(df: pd.DataFrame, country_name: str) -> pd.DataFrame:
    return filter_dataframe(df, country=country_name)

# Helper: filter by likes threshold
def filter_by_likes(df: pd.DataFrame, min_likes: int) -> pd.DataFrame:
    return filter_dataframe(df, min_likes=min_likes)
    
# Helper: filter by sentiment value
def filter_by_sentiment(df: pd.DataFrame, sentiment_value: str) -> pd.DataFrame:
    return filter_dataframe(df, sentiment=sentiment_value)