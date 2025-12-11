# NLP-Social-Trends

## Project Overview 
NLP-Social-Trends is a desktop app for exploring social media data through an interactive GUI. It cleans a Kaggle-sourced dataset, loads it via a robust DataLoader, and uses a Llama-3.2-1B model to perform NLP-based sentiment and tone analysis on posts. These LLM-driven insights dynamically update live Matplotlib graphs, helping users visualize relationships between sentiment, likes, retweets, and geographic or platform filters. By combining AI-powered NLP with real-time visualization, the app turns text into data-driven insights on global social media trends.

### Tech Stack
- Data Analysis & Manipulation: pandas, numpy
- GUI: tkinter, Pillow (PIL), matplotlib
- Machine Learning: torch, transformers, accelerate, bitsandbytes
- Testing: pytest

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
python3 -m pytest .\tests\test_navigation.py
```
### Model & Data Description
The application utilizes the ```Llama-3.2-1B model```, accessed via the Hugging Face transformers library, for the core NLP tasks. This is a pre-trained Large Language Model (LLM) designed for general language understanding. For the sentiment classification itself, we further leverage the ```finiteautomata/bertweet-base-sentiment-analysis``` pipeline to reliably classify emotions extracted from the posts into three categories: POS (Positive), NEG (Negative), or NEU (Neutral). The entire model inference process is handled offline using GPU acceleration (```torch```, ```bitsandbytes```) to produce the final, rich dataset consumed by the GUI.

### Dataset
The source material for the project is the [Kaggle Social Media Sentiments Analysis Dataset](https://www.kaggle.com/datasets/kashishparmar02/social-media-sentiments-analysis-dataset). This rich dataset contains over 732 social media entries, along with metadata such as the platform, geographic location, likes, retweets, and a base sentiment value. The final application structure relies heavily on the consistency and completeness of the final 732 rows derived from this source.

### Data Preprocessing steps
The data pipeline transforms the raw Kaggle file through multiple stages to ensure consistency and quality for both the LLM and the GUI:
- **Source Data & Mocking**: ```mock_data.csv``` is used during early development for quick, isolated testing of backend logic and UI functionality.
- **Initial Cleanup**: The pipeline loads ```raw_kaggle.csv```, standardizes column names (e.g., Text to text), performs text cleaning (removing special characters, URLs, and trimming whitespace), and drops incomplete rows where the post text is missing or empty.
- **Intermediate Output**: The cleaned data is outputted to an intermediate file, ```processed_data.csv```.
- **LLM Processing**: This processed data undergoes Llama-3.2-1B and Bertweet sentiment analysis, resulting in the model-ready dataset, ```LLM_data.csv```. This file includes 732 fully processed rows and specific columns used by the application (Post_Number, text, Sentiment, Location, Platform, Likes, Retweets).
- **Final Data Source**: The last version created by the pipeline, ```LLM_data_final.csv```, is the definitive dataset used by the running application as the source for all graphs and dynamic display panels.