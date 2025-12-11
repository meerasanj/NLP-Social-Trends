# GUI update helpers for geography/description/sentiment panels and center content.
import tkinter as tk
from tkinter import font
import graph_utils
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk # for dynamic image resizing
import math

canvas_widget = None

# Global variables for the resizable phone screen image
phone_screen_original_img = None # original Pillow Image object
phone_screen_tk_img = None       # resized Tkinter ImageTk object

# Helper class to mock a Tkinter Event for manual triggering 
# Fixes 'Event() takes no arguments'
class MockResizeEvent:
    """A minimal object to pass necessary attributes (widget, width, height) to a resize handler."""
    def __init__(self, widget, width, height):
        self.widget = widget
        self.width = width
        self.height = height

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


# Helper function to clear a frame
def clear_frame(frame):
    for w in frame.winfo_children():
        w.destroy()

# Initializes global resources, loading the original phone screen image using PIL
def init_display_logic(root_window):
    global phone_screen_original_img
    try:
        # Load the image using Pillow (Image.open)
        phone_screen_original_img = Image.open('img/phone-graphic.gif')
        print("[display_logic] phonescreen.png loaded successfully by PIL.")
    except Exception as e:
        print(f"[display_logic] Error loading phonescreen.png with PIL: {e}")
        phone_screen_original_img = None

# Event handler bound to the middle frame to resize the phone screen image 
def _on_middle_resize(event):
    global phone_screen_original_img, phone_screen_tk_img
    
    if not phone_screen_original_img:
        return

    frame_width = event.width
    frame_height = event.height
    
    # Check for valid dimensions
    if frame_width <= 0 or frame_height <= 0:
        return

    # Calculate the new size while maintaining aspect ratio
    original_width, original_height = phone_screen_original_img.size
    
    # Calculate scale factor for fitting inside the frame
    ratio_w = frame_width / original_width
    ratio_h = frame_height / original_height
    
    # Choose the smaller ratio to ensure the image fits entirely within the frame
    ratio = min(ratio_w, ratio_h)
    
    # Apply a slight padding/margin 
    margin_factor = 0.95
    new_width = int(original_width * ratio * margin_factor)
    new_height = int(original_height * ratio * margin_factor)

    if new_width <= 0 or new_height <= 0:
        return # Avoid errors with zero-sized results

    # Resize the image using Pillow
    # Image.Resampling.LANCZOS is a high-quality resampling filter
    resized_img = phone_screen_original_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    # Create the Tkinter compatible PhotoImage
    phone_screen_tk_img = ImageTk.PhotoImage(resized_img)
    
    # Find the label currently holding the image and update it
    middle_frame = event.widget
    
    # Use winfo_children()[0] to safely find the label created in update_middle
    if middle_frame.winfo_children():
        image_label = middle_frame.winfo_children()[0]
        image_label.config(image=phone_screen_tk_img)
        # Keep the necessary Tkinter reference on the label
        image_label.image = phone_screen_tk_img 

# Helper function to safely convert None values to "N/A"
def _safe_text(value):
    if value is None:
        return "N/A"
    return str(value)

# Updates the geography label on the upper left frame
def update_geography(frames, geo_text_or_post):
    try:
        if isinstance(geo_text_or_post, dict):
            text = geo_text_or_post.get('Location', 'Unknown')
        else:
            text = geo_text_or_post
        lbl = frames["labels"]["geography"]
        lbl.config(text="", font=("Georgia", 12), fg="#71557A")
        if text in FLAG_PATHS:
            flag_photo = tk.PhotoImage(file=FLAG_PATHS[text])
            lbl.config(image=flag_photo, compound='left')
            lbl.image = flag_photo 
        else:
            lbl.config(image='')
    except Exception as e:
        print("[display_logic.update_geography] Error:", e)

# Updates the description label area
# This function is flexible:
# - If platform_or_post is a dict/Series, it extracts Platform, Likes, Retweets, and text.
# - Else, platform_or_post is treated as the platform string and count_text as additional info.
def update_description(frames, platform_or_post, count_text=None):
    try:
        if isinstance(platform_or_post, dict):
            post = platform_or_post
            platform = post.get('Platform', 'Unknown')
            post_number = post.get('Post_Number', '')
            likes = post.get('Likes', '')
            retweets = post.get('Retweets', '')
            text = post.get('text') or post.get('post_text') or ''
        else:
            platform = platform_or_post or ''
            post_number = ''
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
                                  fg="#B83556", bg="#D4C5AE")
        platform_label.pack(pady=(10, 5))
        
        # Post number
        postnum_label = tk.Label(top_section, text=f"POST {_safe_text(post_number)}",
                                 font=("Georgia", 12, "bold"),
                                 fg="#71557A", bg="#D4C5AE")
        postnum_label.pack(pady=(0, 5))
        
        # Stats line with heart and retweet symbols
        stats_text = f"❤ {_safe_text(likes)} likes  ↻ {_safe_text(retweets)} retweets"
        stats_label = tk.Label(top_section, text=stats_text,
                              font=("Georgia", 12),
                              fg="#B83556", bg="#D4C5AE")
        stats_label.pack(pady=(0, 10))
        
        # Create bottom subsection for post text
        bottom_section = tk.Frame(parent, bg="#D4C5AE", bd=2, relief="groove")
        bottom_section.pack(fill="both", expand=True, padx=20, pady=(10, 20))
        
        # Post text
        txt = tk.Text(bottom_section, wrap="word", font=("Georgia", 16), 
                     fg="#B83556", bg="#D4C5AE", bd=0)
        txt.insert("1.0", text)
        txt.tag_configure("center", justify="center")
        txt.tag_add("center", "1.0", "end")
        txt.config(state="disabled")
        txt.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Store reference
        frames["labels"]["description"] = txt
    except Exception as e:
        print("[display_logic.update_description] Error:", e)

# Updates the center panel
# If content is graph, show it.
# Otherwise, show the phone screen image with dynamic resizing.
def update_middle(frames, content):
    global canvas_widget
    middle_frame = frames["middleTopFrame"]
    
    # 1. Always unbind any previous resize handler when updating the content
    middle_frame.unbind('<Configure>')
    clear_frame(middle_frame)
    
    try:
        if callable(content):
            # Graph Logic
            fig = content()
            canvas = FigureCanvasTkAgg(fig, master=middle_frame)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.pack(fill="both", expand=True)
            canvas.draw()

        else:
            # Phone Screen Image Logic (when navigating posts)
            if phone_screen_original_img:
                
                # 2. Create the label placeholder
                lbl = tk.Label(middle_frame, bg=middle_frame.cget("bg"))
                lbl.pack(expand=True)
                
                # 3. Bind the resize function to the frame
                middle_frame.bind('<Configure>', _on_middle_resize)
                
                # 4. Manually trigger the resize function 
                middle_frame.update_idletasks() 
                
                # Create and call with the MockResizeEvent to pass required size attributes
                mock_event = MockResizeEvent(
                    middle_frame, 
                    middle_frame.winfo_width(), 
                    middle_frame.winfo_height()
                )
                
                _on_middle_resize(mock_event)
                
            else:
                # Fallback to displaying text content if image failed to load
                lbl = tk.Label(middle_frame, text=str(content), bg=middle_frame.cget("bg"), font=("Arial",16))
                lbl.pack(expand=True)

    except Exception as e:
        print(f"[display_logic.update_middle] Error: {e}")

# Updates sentiment area
# Accepts a simple string or a post dict/Series.
def update_sentiment(frames, sentiment_text_or_post):
    try:
        if isinstance(sentiment_text_or_post, dict):
            sentiment_text = sentiment_text_or_post.get('Sentiment', 'Unknown')
        else:
            sentiment_text = sentiment_text_or_post
        lbl = frames["labels"]["sentiment"]
        lbl.config(text="", font=("Georgia", 12), fg="#71557A")

        if sentiment_text in SENTIMENT_PATHS:
            sentiment_photo = tk.PhotoImage(file=SENTIMENT_PATHS[sentiment_text])
            lbl.config(image=sentiment_photo, compound='left')
            lbl.image = sentiment_photo 
        else:
            lbl.config(image='') 
    except Exception as e:
        print("[display_logic.update_sentiment] Error:", e)

# Wires the bottom buttons to callbacks if provided.
def wire_buttons(frames, on_back=None, on_select=None, on_next=None):
    try:
        if on_back:
            frames["buttons"]["back"].config(command=on_back)
        if on_select:
            frames["buttons"]["select"].config(command=on_select)
        if on_next:
            frames["buttons"]["next"].config(command=on_next)
    except Exception as e:
        print("[display_logic.wire_buttons] Error:", e)