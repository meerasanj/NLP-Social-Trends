import pandas as pd
import os

# DataLoader class to load and manage the data
class DataLoader:
    # Initializes the loader.
    def __init__(self, filename='mock_data.csv'):
        # Get the backend folder
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Get project root
        project_root = os.path.dirname(current_dir)
        # Construct full path to data/filename
        self.filepath = os.path.join(project_root, 'data', filename)
        
        self.df = None
        self.load_data()

    # Loads the data from the CSV file and returns it as a Pandas DataFrame.
    def load_data(self):
        if os.path.exists(self.filepath):
            try:
                self.df = pd.read_csv(self.filepath)
                print(f"[DataLoader] Success: Loaded {self.filepath}")
            except Exception as e:
                print(f"[DataLoader] Error reading CSV: {e}")
                self.df = pd.DataFrame()
        else:
            print(f"[DataLoader] File not found: {self.filepath}")
            self.df = pd.DataFrame()

    # Returns a dictionary of the post at the specific index.
    def get_post_by_index(self, index):
        if self.df is None or self.df.empty:
            return None
        if 0 <= index < len(self.df):
            return self.df.iloc[index].to_dict()
        else:
            return None

    # Returns the entire DataFrame.
    def get_all_posts(self):
        return self.df
    
    # Returns the total number of posts.
    def get_total_count(self):
        return len(self.df) if self.df is not None else 0

# Quick test - runs only if you run this script directly
if __name__ == "__main__":
    loader = DataLoader('mock_data.csv')
    print("Test Post #0:", loader.get_post_by_index(0))