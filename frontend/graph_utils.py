import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 

#First Part is Test for how matplotlib works

#Load data for use
#df = pd.read_csv('../data/LLM_data.csv')

#Set Up Scatter plot
#figTest, axTest = plt.subplots()
#x = df['Post_Number']
#y = df['Likes']
#axTest.scatter(x,y, color = "darkorange")

#Set Up Graph Environment
#plt.xlabel('Post Number')
#plt.ylabel('Likes')
#plt.title('Post Summary')
#plt.grid(True)

#Show Graph
#plt.show()

#Logic that will be used in the main gui
def postnumByLoc(): # Base graph that is shown on app launch
    # Loading correct x and y data for graph
    df = pd.read_csv('data/LLM_data_final.csv')
    xIn = df['Post_Number']
    yIn = df['Location']

    # Initializing figure for the panel
    baseFig = Figure(figsize=(5,4), dpi=80)
    ax = baseFig.add_subplot(111)

    # Outputting and customizing graph
    ax.scatter(xIn,yIn, color = "darkorange")
    ax.set_xlabel('Post Number')
    ax.set_ylabel('Location')
    ax.set_title('Posts by Location')
    ax.grid(True)


    return baseFig


def sentByLikes():
    # Loading correct x and y data for graph
    df = pd.read_csv('data/LLM_data_final.csv')
    xIn = df['Sentiment']
    yIn = df['Likes']

    # Initializing figure for the panel
    sxlFig = Figure(figsize=(5,4), dpi=80)
    ax = sxlFig.add_subplot(111)
    
    # Outputting and customizing graph
    ax.scatter(xIn,yIn, color = "darkorange")
    ax.set_xlabel('Sentiment')
    ax.set_ylabel('Likes')
    ax.set_title('Sentiment by Likes')
    ax.grid(True)

    return sxlFig


def sentByPostNum():
    # Loading correct x and y data for graph
    df = pd.read_csv('data/LLM_data_final.csv')
    xIn = df['Sentiment']
    yIn = df['Post_Number']

    # Initializing figure for the panel
    sxpnFig = Figure(figsize=(5,4), dpi=80)
    ax = sxpnFig.add_subplot(111)

    # Outputting and customizing graph
    ax.scatter(xIn,yIn, color = "darkorange")
    ax.set_xlabel('Sentiment')
    ax.set_ylabel('Post Number')
    ax.set_title('Sentiment by Posts')
    ax.grid(True)
    
    return sxpnFig


def platformByLikes():
    # Loading correct x and y data for graph
    df = pd.read_csv('data/LLM_data_final.csv')
    xIn = df['Platform']
    yIn = df['Likes']
    
    # Initializing figure for the panel
    pxlFig = Figure(figsize=(5,4), dpi=80)
    ax = pxlFig.add_subplot(111)

    # Outputting adn customizing graph
    ax.scatter(xIn,yIn, color = "darkorange")
    ax.set_xlabel('Platform')
    ax.set_ylabel('Likes')
    ax.set_title('Platform by Likes')
    ax.grid(True)

    return pxlFig


