import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

#Load data for use
df = pd.read_csv('../data/LLM_data.csv')

#Set Up Scatter plot
fig, ax = plt.subplots()
x = df['Post_Number']
y = df['Likes']
ax.scatter(x,y, color = "darkorange")

#Set Up Graph Environment
plt.xlabel('Post Number')
plt.ylabel('Likes')
plt.title('Post Summary')
plt.grid(True)

#Show Graph
plt.show()


