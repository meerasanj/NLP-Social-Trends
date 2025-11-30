import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

#First Part is Test for how matplotlib works

#Load data for use
df = pd.read_csv('../data/LLM_data.csv')

#Set Up Scatter plot
figTest, axTest = plt.subplots()
x = df['Post_Number']
y = df['Likes']
axTest.scatter(x,y, color = "darkorange")

#Set Up Graph Environment
plt.xlabel('Post Number')
plt.ylabel('Likes')
plt.title('Post Summary')
plt.grid(True)

#Show Graph
plt.show()

#Logic that will be used in the main gui
def scatter_plot(xIn, yIn):
    fig, ax =plt.subplots()
    ax.scatter(xIn,yIn, color = "darkorange")
    plt.xlabel('Post Number')
    plt.ylabel('Likes')
    plt.title('Post Summary')
    plt.grid(True)
    return fig
