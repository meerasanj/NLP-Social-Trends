# Define the static GUI layout and return root + frames for other modules.

# GUI import
import tkinter as tk
from tkinter import font

#Omar
def build_layout(window_title="NLP-Social-Trends", geometry="750x500"):
    """
    Minimal wrapper around the existing layout.
    Returns (root, frames) so other modules can import without starting mainloop.
    """

    # Creates the GUI window
    mainWindow = tk.Tk()
    mainWindow.title("NLP-Social-Trends")

    # Initializes the font variable
    georgia = font.Font(family="Georgia", size=14, weight="normal")

    # Cross-platform approach: set geometry after window initialization 
    mainWindow.withdraw()
    mainWindow.update_idletasks()

    # Get screen dimensions
    screen_width = mainWindow.winfo_screenwidth()
    screen_height = mainWindow.winfo_screenheight()

    # Set window to full screen size
    mainWindow.geometry(f"{screen_width}x{screen_height}+0+0")
    mainWindow.resizable(False, False)
    mainWindow.deiconify()
    # Add 'icon' to app
    icon = tk.PhotoImage(file='img/app-icon.gif')
    mainWindow.iconphoto(True, icon)

    # Bottom frame for the index buttons
    bottomFrame = tk.Frame(mainWindow, bg="#55768C", height = 150)
    bottomFrame.pack(side="bottom", fill="x")
    bottomFrame.pack_propagate(False)

    # Top frame, holds other frames (not visible)
    topFrame = tk.Frame(mainWindow, bg="lightblue")
    topFrame.pack(side="top", fill="both", expand=True)

    # Top left frame, holds other frames (not visible)
    leftTopFrame = tk.Frame(topFrame, bg="white", height = 350)
    leftTopFrame.pack(side="left", fill = "both", expand=True)
    leftTopFrame.pack_propagate(False)

    # Topmost left frame, will display geographic location of the post
    geographyFrame = tk.Frame(leftTopFrame, bg="#D4C5AE", height=150)
    geographyFrame.pack(side="top", fill="both")

    # Frame below geography, will display description and stats for the post
    descFrame = tk.Frame(leftTopFrame, bg="#DC97A5")
    descFrame.pack(side="top", fill="both", expand=True)

    # Will hold the graph and query results from model
    middleTopFrame = tk.Frame(topFrame, bg="#71557A", height = 350, width = 200)
    middleTopFrame.pack(side="left", fill = "both", expand=True)

    # Top right frame, holds other frames (not visible)
    rightTopFrame = tk.Frame(topFrame, bg="pink", height = 350)
    rightTopFrame.pack(side="left", fill = "both", expand=True)
    rightTopFrame.pack_propagate(False)

    # Top right most frame, shows sentiment image for post
    sentimentFrame = tk.Frame(rightTopFrame, bg="#D4C5AE", height=150)
    sentimentFrame.pack(side="top", fill="both")

    # Frame below sentiment, allows filtering of graph
    filterFrame = tk.Frame(rightTopFrame, bg="#DC97A5")
    filterFrame.pack(side="top", fill="both")

    filter_label = tk.Label(filterFrame, text="Graph Filters", bg="#DC97A5", font=("Georgia", 16, "bold"))    
    filter_label.pack(side="top", pady=10, fill="x")
    filter_btns = {}

    btn_labels = ["Sentiment by Likes", "Sentiment by Post Number", " Platform by Likes", "Return to Base Graph"]

    for i, label_text in enumerate(btn_labels):
        # Create the button
        btn = tk.Button(filterFrame, text=label_text, 
                       bg="#D4C5AE", fg="#FF1493", 
                       font=("Georgia", 16),
                       bd=3, relief="groove",
                       highlightbackground="#55768E", highlightthickness=3,
                       height=2)
        
        # side="top" stacks them vertically. fill="x" makes them stretch horizontally.
        btn.pack(fill="x", padx=10, pady = 47, expand=True)
        
        # Save to our dict with keys like "btn1", "btn2", etc.
        filter_btns[f"btn{i+1}"] = btn

    # Add simple placeholder labels so areas are visible when imported
    def _add_label(frame, text):
        lbl = tk.Label(frame, text=text, bg=frame.cget("bg"))
        lbl.pack(expand=True, padx=8, pady=8)
        return lbl

    #Omar2
    geography_label = _add_label(geographyFrame, "TODO: Geography / Country")
    desc_label = _add_label(descFrame, "TODO: Platform / Description / Stats")
    middle_label = _add_label(middleTopFrame, "TODO: Phone / Graph / Query results")
    sentiment_label = _add_label(sentimentFrame, "TODO: Sentiment Image")

    # Bottom buttons (laid out simply to match spec)
    button_frame = tk.Frame(bottomFrame, bg=bottomFrame.cget("bg"))
    button_frame.pack(side="top", pady=20, fill="x")

    button_frame.columnconfigure(0, weight=1)
    button_frame.columnconfigure(1, weight=1)
    button_frame.columnconfigure(2, weight=1)

    btn_back = tk.Button(button_frame, text="<--   Back", width=12, height=2, font=("Georgia", 11), highlightbackground="#DC97A5", fg="#71557A")
    btn_select = tk.Button(button_frame, text="Select Post #", width=15, height=2, font=("Georgia", 11), highlightbackground="#DC97A5", fg="#71557A")
    btn_next = tk.Button(button_frame, text="Next   -->", width=12, height=2, font=("Georgia", 11), highlightbackground="#DC97A5", fg="#71557A")
    btn_back.grid(row=0, column=0, padx=8, pady=8)
    btn_select.grid(row=0, column=1, padx=8, pady=8)
    btn_next.grid(row=0, column=2, padx=8, pady=8)

    frames = {
        "root": mainWindow,
        "bottomFrame": bottomFrame,
        "topFrame": topFrame,
        "leftTopFrame": leftTopFrame,
        "geographyFrame": geographyFrame,
        "descFrame": descFrame,
        "middleTopFrame": middleTopFrame,
        "rightTopFrame": rightTopFrame,
        "sentimentFrame": sentimentFrame,
        "filterFrame": filterFrame,
        "labels": {
            "geography": geography_label,
            "description": desc_label,
            "middle": middle_label,
            "sentiment": sentiment_label,
            #"filter": filter_label
        },
        "buttons": {
            "back": btn_back,
            "select": btn_select,
            "next": btn_next
        },
        "filter_buttons": filter_btns
    }

    return mainWindow, frames

# Keep behavior identical when Lili runs this file directly
if __name__ == "__main__":
    root, frames = build_layout(window_title="Placeholder Title", geometry="750x500")
    root.mainloop()
