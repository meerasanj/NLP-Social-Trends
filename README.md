# NLP-Social-Trends

## Project Overview 
NLP-Social-Trends is a desktop app for exploring social media data through an interactive GUI. It cleans a Kaggle-sourced dataset, loads it via a robust DataLoader, and uses a Llama-3.2-1B model to perform NLP-based sentiment and tone analysis on posts. These LLM-driven insights dynamically update live Matplotlib graphs, helping users visualize relationships between sentiment, likes, retweets, and geographic or platform filters. By combining AI-powered NLP with real-time visualization, the app turns text into data-driven insights on global social media trends.

### TODO: Tech Stack
- bullet point list all technologies used 
- Data Analysis & Manipulation:
- GUI:
- Machine Learning

## Instructions to Compile & Run

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Main Application
```bash
python3 frontend/main_gui.py
```

3. (Optional) Test Cases and Debugging
```bash
# Preprocess raw data (creates processed_data.csv)
python3 pipeline/data_preprocessing.py

# Optional: test data loader
python3 backend/data_loader.py

# Run test cases for graph and filters
python3 tests/test_graph_filters.py

# Run test cases for buttons/navigation

```

## TODO: Model & Data Description
- format the following as paragraphs

### TODO: Model Architecture 
- discuss Hugging Face Llama-3.2-1B model, if it was pre-trained, other necessary details

### TODO: Dataset 
- discuss Kaggle dataset source and link it, type of data it contains

### TODO: Data Preprocessing steps 
- mock_data.csv is used for early testing of the app 
- discuss what preprocessing steps were done on the original dataset from kaggle ie load raw kaggle csv, normalize column names to standard schema, clean text and trim whitespace, drop rows where text is missing/empty, output it to processed_data.csv
- then LLM_data.csv is the GUI/model-ready dataset w 732 rows and columns: Post_Number, text, Sentiment, Location, Platform, Likes, Retweets
- lastly LLM_data_final.csv is the dataset used by the app and is the source for the graphs and display 