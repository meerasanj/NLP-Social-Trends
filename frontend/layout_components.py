# GUI import
import tkinter as tk

#Omar
def build_layout(window_title="Placeholder Title", geometry="750x500"):
    """
    Minimal wrapper around the existing layout.
    Returns (root, frames) so other modules can import without starting mainloop.
    """
    # Creates the GUI window
    mainWindow = tk.Tk()
    mainWindow.title("Placeholder Title")
    mainWindow.geometry("750x500")

    # Add 'icon' to app
    icon = tk.PhotoImage(file='img/app-icon.gif')
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

    filter_label = tk.Label(filterFrame, text="Graph Filters", bg="orange")
    filter_label.pack(side="top", pady=5)

    filter_btns = {}

    btn_labels = ["Sentiment by Likes", "Sentiment by Post Number", " Platform by Likes", "Return to Base Graph"]

    for i, label_text in enumerate(btn_labels):
        # Create the button
        btn = tk.Button(filterFrame, text=label_text)
        
        # side="top" stacks them vertically. fill="x" makes them stretch horizontally.
        btn.pack(side="top", fill="x", padx=10, pady=5)
        
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
    filter_label = _add_label(filterFrame, "TODO: Filter / Controls")

    # Bottom buttons (laid out simply to match spec)
    button_frame = tk.Frame(bottomFrame, bg=bottomFrame.cget("bg"))
    button_frame.pack(expand=True)

    btn_back = tk.Button(button_frame, text="<-- Back")
    btn_select = tk.Button(button_frame, text="Select Post #")
    btn_next = tk.Button(button_frame, text="Next -->")
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
