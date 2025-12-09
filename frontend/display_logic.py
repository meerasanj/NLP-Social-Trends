# display_logic.py
import tkinter as tk
from tkinter import font
import graph_utils
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

canvas_widget = None

FLAG_PATHS = {
    'USA' : 'img/us-flag.gif',
    'UK' : 'img/uk-flag.gif',
    'India' : 'img/india-flag.gif',
    'Australia' : 'img/australia-flag.gif',
    'Canada' : 'img/canada-flag.gif'
}

SENTIMENT_PATHS = {
    'POS' : 'img/positive-sentiment.gif',
    'NEU' : 'img/neutral-sentiment.gif',
    'NEG' : 'img/negative-sentiment.gif'
}

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
        lbl.config(text=f"Location: {_safe_text(text)}", font=("Georgia", 12), fg="#71557A")
        if text in FLAG_PATHS:
            flag_photo = tk.PhotoImage(file=FLAG_PATHS[text])
            lbl.config(image=flag_photo, compound='left')
            lbl.image = flag_photo 
        else:
            lbl.config(image='')
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
        else:
            platform = platform_or_post or ''
            likes = ''
            retweets = ''
            text = count_text or ''
        
        # Get the description frame (the parent container)
        parent = frames["descFrame"]
        
        # Clear all widgets in the description frame
        clear_frame(parent)
        
        # Create top subsection for Platform/Likes/Retweets
        top_section = tk.Frame(parent, bg="#D4C5AE", bd=2, relief="groove")
        top_section.pack(fill="x", padx=20, pady=(20, 10))
        
        # Platform name (bold)
        platform_label = tk.Label(top_section, text=platform.upper(), 
                                  font=("Georgia", 14, "bold"), 
                                  fg="#71557A", bg="#D4C5AE")
        platform_label.pack(pady=(10, 5))
        
        # Stats line with heart and retweet symbols
        stats_text = f"❤ {_safe_text(likes)} likes  ↻ {_safe_text(retweets)} retweets"
        stats_label = tk.Label(top_section, text=stats_text,
                              font=("Georgia", 12),
                              fg="#71557A", bg="#D4C5AE")
        stats_label.pack(pady=(0, 10))
        
        # Create bottom subsection for post text
        bottom_section = tk.Frame(parent, bg="#D4C5AE", bd=2, relief="groove")
        bottom_section.pack(fill="both", expand=True, padx=20, pady=(10, 20))
        
        # Post text
        txt = tk.Text(bottom_section, wrap="word", font=("Georgia", 16), 
                     fg="#71557A", bg="#D4C5AE", bd=0)
        txt.insert("1.0", text)
        txt.config(state="disabled")
        txt.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Store reference
        frames["labels"]["description"] = txt
    except Exception as e:
        print("[display_logic.update_description] Error:", e)

def update_middle(frames, content):
    """
    Center panel: if text provided, show it; otherwise render the scatter_plot figure.
    """
    global canvas_widget
    try:
        middle_frame = frames["middleTopFrame"]
        clear_frame(middle_frame)
        
        if callable(content):
            fig = content()
            canvas = FigureCanvasTkAgg(fig, master=middle_frame)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.pack(fill="both", expand=True)
            canvas.draw()

        else:
            lbl = tk.Label(middle_frame, text=str(content), bg=middle_frame.cget("bg"), font=("Arial",16))
            lbl.pack(expand=True)

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
        lbl.config(text=f"Sentiment: {_safe_text(sentiment_text)}", font=("Georgia", 12), fg="#71557A")

        if sentiment_text in SENTIMENT_PATHS:
            sentiment_photo = tk.PhotoImage(file=SENTIMENT_PATHS[sentiment_text])
            lbl.config(image=sentiment_photo, compound='left')
            lbl.image = sentiment_photo 
        else:
            lbl.config(image='') 
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
