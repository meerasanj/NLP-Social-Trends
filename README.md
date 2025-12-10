# NLP-Social-Trends

## TODO: Project Overview 
- (paragraph summary of what our project is)

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

## Tests for Data Preprocessing & Data Loading
```bash
# Preprocess raw data (creates processed_data.csv)
python3 pipeline/data_preprocessing.py

# Optional: test data loader
python3 backend/data_loader.py
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