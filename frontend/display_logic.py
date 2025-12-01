# display_logic.py
import tkinter as tk
from graph_utils import scatter_plot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

canvas_widget = None

def clear_frame(frame):
    """Remove all children from a frame."""
    for w in frame.winfo_children():
        w.destroy()

def _safe_text(value):
    if value is None:
        return "N/A"
    return str(value)

def update_geography(frames, geo_text_or_post):
    """
    Updates the geography label on the upper left frame.
    Accepts either a simple string (country) or a post dict/Series with 'Location'.
    """
    try:
        if isinstance(geo_text_or_post, dict):
            text = geo_text_or_post.get('Location', 'Unknown')
        else:
            text = geo_text_or_post
        lbl = frames["labels"]["geography"]
        lbl.config(text=f"Location: {_safe_text(text)}")
    except Exception as e:
        print("[display_logic.update_geography] Error:", e)

def update_description(frames, platform_or_post, count_text=None):
    """
    Updates the description label area.
    This function is flexible:
      - If platform_or_post is a dict/Series, it extracts Platform, Likes, Retweets, and text.
      - Else, platform_or_post is treated as the platform string and count_text as additional info.
    """
    try:
        if isinstance(platform_or_post, dict):
            post = platform_or_post
            platform = post.get('Platform', 'Unknown')
            likes = post.get('Likes', '')
            retweets = post.get('Retweets', '')
            text = post.get('text') or post.get('post_text') or ''
            desc = f"Platform: {_safe_text(platform)}\nLikes: {_safe_text(likes)}  Retweets: {_safe_text(retweets)}\n\n{text}"
        else:
            platform = platform_or_post or ''
            extra = count_text or ''
            desc = f"Platform: {_safe_text(platform)}\n{_safe_text(extra)}"
        lbl = frames["labels"]["description"]
        # If it's a long text, replace label with Text widget for readability
        parent = lbl.master
        # Destroy the old label widget and create a Text if text is long
        lbl.destroy()
        txt = tk.Text(parent, wrap="word", height=8)
        txt.insert("1.0", desc)
        txt.config(state="disabled", bg=parent.cget("bg"), bd=0)
        txt.pack(fill="both", expand=True, padx=8, pady=8)
        # store reference so other code can still access frames["labels"]["description"]
        frames["labels"]["description"] = txt
    except Exception as e:
        print("[display_logic.update_description] Error:", e)

def update_middle(frames, text):
    """
    Center panel: if text provided, show it; otherwise render the scatter_plot figure.
    """
    global canvas_widget
    try:
        middle_frame = frames["middleTopFrame"]
        clear_frame(middle_frame)

        if text:
            lbl = tk.Label(middle_frame, text=text, anchor="nw", justify="left")
            lbl.pack(fill="both", expand=True, padx=10, pady=10)
            frames["labels"]["middle"] = lbl
        else:
            fig = scatter_plot()
            canvas = FigureCanvasTkAgg(fig, master=middle_frame)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.pack(fill="both", expand=True)
            canvas.draw()
    except Exception as e:
        print("[display_logic.update_middle] Error:", e)

def update_sentiment(frames, sentiment_text_or_post):
    """
    Updates sentiment area. Accepts a simple string or a post dict/Series.
    """
    try:
        if isinstance(sentiment_text_or_post, dict):
            sentiment_text = sentiment_text_or_post.get('Sentiment', 'Unknown')
        else:
            sentiment_text = sentiment_text_or_post
        lbl = frames["labels"]["sentiment"]
        lbl.config(text=f"Sentiment: {_safe_text(sentiment_text)}")
    except Exception as e:
        print("[display_logic.update_sentiment] Error:", e)

def wire_buttons(frames, on_back=None, on_select=None, on_next=None):
    """
    Wires the bottom buttons to callbacks if provided.
    """
    try:
        if on_back:
            frames["buttons"]["back"].config(command=on_back)
        if on_select:
            frames["buttons"]["select"].config(command=on_select)
        if on_next:
            frames["buttons"]["next"].config(command=on_next)
    except Exception as e:
        print("[display_logic.wire_buttons] Error:", e)
