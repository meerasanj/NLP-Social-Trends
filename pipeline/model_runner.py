#!/usr/bin/env python
# coding: utf-8

# In[1]:


import torch
import csv
from transformers import pipeline, BitsAndBytesConfig
from ipywidgets import FileUpload
from IPython.display import display
import os

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


filePath = "/home/james/NLP-Social-Trends/data/mock_data.csv"

rows = []
with open(filePath, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        rows.append(row)


# In[3]:


prompt = f"""Task: Extract information from each social media post.

For each post, provide:
- Post Number (sequential, starting at 1)
- Sentiment (Positive, Negative, or Neutral)
- Location (country)
- Platform
- Likes count
- Retweets count

Output format (one line per post):
Post Number: X, Sentiment: X, Location: X, Platform: X, Likes: X, Retweets: X

Dataset:
{rows}

Output:"""


# In[4]:


response = pipe(prompt, max_new_tokens=200, temperature=0.3, do_sample=False, return_full_text=False)
output = response[0]["generated_text"]
print(output)


# In[5]:


with open("model_output.txt", "w") as f:
    f.write(output)


# In[ ]:




