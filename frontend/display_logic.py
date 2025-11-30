# display_logic.py
# All functions are stubs for now — no real logic yet.

import tkinter as tk
from graph_utils import scatter_plot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

canvas_widget = None

def update_geography(frames, geo_text):
    """
    TODO: updates the geography label on the upper left frame.
    """
    pass

def update_description(frames, platform, count_text):
    """
    TODO: updates the description fields on the left panel.
    """
    pass

def update_middle(frames, text):
    global canvas_widget

    middle_frame = frames["middleTopFrame"]

    for widget in middle_frame.winfo_children():
        widget.destroy()

    if text:
        frames["labels"]["middle"] = tk.Label(
            middle_frame, 
            text=text, 
            anchor="nw", 
            justify="left")

        frames["labels"]["middle"].pack(fill="both", expand=True, padx=10, pady=10)
    else:
        fig = scatter_plot()

        canvas = FigureCanvasTkAgg(fig, master=middle_frame)
        canvas_widget = canvas.get_tk_widget()

        canvas_widget.pack(fill="both", expand=True)
        canvas.draw()


    pass

def update_sentiment(frames, sentiment_text):
    """
    TODO: updates the sentiment label on the right panel.
    """
    pass

def wire_buttons(frames, on_back=None, on_select=None, on_next=None):
    """
    TODO: wires button callbacks for Back, Select, and Next.
    """
    pass
