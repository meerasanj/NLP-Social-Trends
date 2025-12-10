# File purpose: load CSV data for the app, clean it, and expose helpers to access posts.

import pandas as pd
import os
import numpy as np

# DataLoader class to load and manage the data
class DataLoader:
    # Initialize loader with a target filename and trigger load
    def __init__(self, filename='mock_data.csv'):
        # Get the backend folder
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Get project root
        project_root = os.path.dirname(current_dir)
        # Construct full path to data/filename
        self.filepath = os.path.join(project_root, 'data', filename)
        
        self.df = None
        self.load_data()

    # Load the CSV and clean it
    def load_data(self):
        if os.path.exists(self.filepath):
            try:
                # Read CSV with comprehensive NaN value handling
                self.df = pd.read_csv(
                    self.filepath, 
                    na_values=['', 'nan', 'NaN', 'NULL', 'null', 'None', 'N/A', 'n/a', '#N/A', '#VALUE!']
                )
                print(f"[DataLoader] Success: Loaded {self.filepath}")
                
                # Clean and normalize the data
                self._clean_data()
                
            except pd.errors.EmptyDataError:
                print(f"[DataLoader] Error: CSV file is empty: {self.filepath}")
                self.df = pd.DataFrame()
            except pd.errors.ParserError as e:
                print(f"[DataLoader] Error parsing CSV: {e}")
                self.df = pd.DataFrame()
            except Exception as e:
                print(f"[DataLoader] Error reading CSV: {e}")
                self.df = pd.DataFrame()
        else:
            print(f"[DataLoader] File not found: {self.filepath}")
            self.df = pd.DataFrame()
    
    # Clean and normalize the loaded data
    def _clean_data(self):
        if self.df is None or self.df.empty:
            return
        
        # Strip whitespace from string columns
        string_columns = self.df.select_dtypes(include=['object']).columns
        for col in string_columns:
            self.df[col] = self.df[col].astype(str).str.strip()
            # Replace empty strings and various NaN representations with NaN
            self.df[col] = self.df[col].replace(['', 'nan', 'NaN', 'NULL', 'null', 'None', 'N/A', 'n/a', '#N/A'], np.nan)
        
        # Handle numeric columns (Likes, Retweets, etc.)
        numeric_columns = self.df.select_dtypes(include=[np.number]).columns
        for col in numeric_columns:
            # Convert to numeric, coercing errors to NaN, then fill with 0
            self.df[col] = pd.to_numeric(self.df[col], errors='coerce').fillna(0)
            # Convert float to int if all values are whole numbers
            if self.df[col].dtype == 'float64' and (self.df[col] % 1 == 0).all():
                self.df[col] = self.df[col].astype('Int64')  # Nullable integer type
        
        # Handle Post_Number column specifically
        if 'Post_Number' in self.df.columns:
            self.df['Post_Number'] = pd.to_numeric(self.df['Post_Number'], errors='coerce')
            # Fill NaN post numbers with sequential numbers
            nan_indices = self.df['Post_Number'].isna()
            if nan_indices.any():
                max_post = self.df['Post_Number'].max()
                if pd.isna(max_post):
                    max_post = 0
                self.df.loc[nan_indices, 'Post_Number'] = range(int(max_post) + 1, int(max_post) + 1 + nan_indices.sum())
            self.df['Post_Number'] = self.df['Post_Number'].astype('Int64')
        
        # Fill NaN values in string columns with appropriate defaults
        if 'Sentiment' in self.df.columns:
            self.df['Sentiment'] = self.df['Sentiment'].fillna('Unknown')
        if 'Location' in self.df.columns:
            self.df['Location'] = self.df['Location'].fillna('Unknown')
        if 'Platform' in self.df.columns:
            self.df['Platform'] = self.df['Platform'].fillna('Unknown')
        
        # Report any remaining issues
        nan_counts = self.df.isna().sum()
        if nan_counts.any():
            print(f"[DataLoader] Warning: Found NaN values after cleaning:")
            print(nan_counts[nan_counts > 0])

    # Get one post as a dict by 0-based index
    def get_post_by_index(self, index):
        if self.df is None or self.df.empty:
            return None
        if 0 <= index < len(self.df):
            post_dict = self.df.iloc[index].to_dict()
            # Convert any remaining NaN values to None for JSON compatibility
            return {k: (None if pd.isna(v) else v) for k, v in post_dict.items()}
        else:
            return None

    # Return the entire DataFrame
    def get_all_posts(self):
        return self.df
    
    # Return total number of posts
    def get_total_count(self):
        return len(self.df) if self.df is not None else 0

# Quick test - runs only if you run this script directly
if __name__ == "__main__":
    # Test with LLM_data.csv (1-732 posts)
    loader = DataLoader('LLM_data.csv')
    print(f"Total posts: {loader.get_total_count()}")
    print("Test Post #0:", loader.get_post_by_index(0))