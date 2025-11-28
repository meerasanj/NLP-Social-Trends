#!/usr/bin/env python
# coding: utf-8

# In[1]:


import torch
import csv
from transformers import pipeline, BitsAndBytesConfig
from ipywidgets import FileUpload
from IPython.display import display
import os
from tqdm import tqdm

quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16
)

pipe = pipeline(
    "text-generation",
    model="meta-llama/Llama-3.2-1B", 
    device_map="auto",
    model_kwargs={"quantization_config": quantization_config}
)


# In[2]:


filePath = "../data/raw_kaggle.csv"

# Get the directory of the input file
input_dir = os.path.dirname(filePath)  # This will be "../data"

# Create output path in the same directory
output_path = os.path.join(input_dir, "model_output.csv")

rows = []
with open(filePath, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        rows.append(row)


print(f"Loaded {len(rows)} rows")


# In[3]:


#Processing in Batches, Rather than All at Once
batch_size=20
output_data=[]


# In[4]:


# Process ONE post at a time
for i, row in enumerate(tqdm(rows, desc="Processing posts"), start=1):

    sentiment = row.get('Sentiment', '').strip()
    country = row.get('Country', '').strip()
    platform = row.get('Platform', '').strip()
    likes = row.get('Likes', '0')
    retweets = row.get('Retweets', '0')

    # Simple prompt
    prompt = f"""Extract and format while classifying the Sentiment as Positive, Negative, or Neutral:
Sentiment: {sentiment}
Location: {country}
Platform: {platform}
Likes: {likes}
Retweets: {retweets}

Output: Post Number: {i}, Sentiment: {sentiment}, Location: {country}, Platform: {platform}, Likes: {likes}, Retweets: {retweets}"""

    try:
        response = pipe(
            prompt, 
            max_new_tokens=100,
            temperature=0.1,
            do_sample=False,
            return_full_text=False,
            pad_token_id=pipe.tokenizer.eos_token_id
        )

        # Add to output (with fallback)
        output_data.append({
            'Post_Number': i,
            'Sentiment': sentiment,
            'Location': country,
            'Platform': platform,
            'Likes': likes,
            'Retweets': retweets
        })

    except Exception as e:
        print(f"Post {i} failed: {e}")
        output_data.append({
            'Post_Number': i,
            'Sentiment': sentiment,
            'Location': country,
            'Platform': platform,
            'Likes': likes,
            'Retweets': retweets
        })


# In[5]:


with open("../data/LLM_data.csv", "w", newline='') as csvfile:
    fieldnames = ['Post_Number', 'Sentiment', 'Location', 'Platform', 'Likes', 'Retweets']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(output_data)


# In[ ]:




