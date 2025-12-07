# GUI import
import tkinter as tk

# Creates the GUI window
mainWindow = tk.Tk()
mainWindow.title("Placeholder Title")
mainWindow.geometry("750x500")

# Add 'icon' to app
icon = tk.PhotoImage(file='../img/app-icon.gif')
mainWindow.iconphoto(True, icon)

# Bottom frame for the index buttons
bottomFrame = tk.Frame(mainWindow, bg="green", height = 150)
bottomFrame.pack(side="bottom", fill="x")

# Top frame, holds other frames (not visible)
topFrame = tk.Frame(mainWindow, bg="lightblue")
topFrame.pack(side="top", fill="both", expand=True)

# Top left frame, holds other frames (not visible)
leftTopFrame = tk.Frame(topFrame, bg="red", height = 350, width = 225)
leftTopFrame.pack(side="left", fill = "both", expand=True)

# Topmost left frame, will display geographic location of the post
geographyFrame = tk.Frame(leftTopFrame, bg="lightgreen", height=150, width = 225)
geographyFrame.pack(side="top", fill="both")

# Frame below geography, will display description and stats for the post
descFrame = tk.Frame(leftTopFrame, bg="purple")
descFrame.pack(side="top", fill="both", expand=True)

# Will hold the graph and query results from model
middleTopFrame = tk.Frame(topFrame, bg="yellow", height = 350, width = 350)
middleTopFrame.pack(side="left", fill = "both", expand=True)

# Top right frame, holds other frames (not visible)
rightTopFrame = tk.Frame(topFrame, bg="pink", height = 350, width = 200)
rightTopFrame.pack(side="left", fill = "both", expand=True)

# Top right most frame, shows sentiment image for post
sentimentFrame = tk.Frame(rightTopFrame, bg="teal", height=150, width = 200)
sentimentFrame.pack(side="top", fill="both")

# Frame below sentiment, allows filtering of graph
filterFrame = tk.Frame(rightTopFrame, bg="orange")
filterFrame.pack(side="top", fill="both", expand=True)

# Populates everything in window
mainWindow.mainloop()