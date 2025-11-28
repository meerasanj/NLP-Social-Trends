# main_gui.py
import sys
import os

# Add parent directory to path to import backend modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from layout_components import build_layout
import display_logic
from backend.navigation import Navigator
from backend.data_loader import DataLoader

"""
================================================================================
DATA MAPPING GUIDE FOR OMAR
================================================================================

What Meera did already:
---------------
- Imports are added
- Navigator and DataLoader instances are created in main()

What Omar needs to do:
-------------------
1. In on_next_pressed() function:
   - Get the next index
   - Get post data
   - Update all labels with the post data (see mapping below)

2. Initialize first post on startup:
   - After creating the GUI, load the first post and display it

Example output of get_post_by_index(0):
----------------------------------------
{
  "Post_Number": 1,
  "text": "Enjoying a beautiful day at the park!",
  "Sentiment": "Positive",
  "Location": "USA",
  "Platform": "Twitter",
  "Likes": 30,
  "Retweets": 15
}

Dataframe field -> GUI widget mapping:
--------------------------------------
Access widgets via: frames["labels"]["widget_name"]

Post_Number Example: frames["labels"]["middle"].config(text=f"Post #{post_data['Post_Number']}")

text → frames["labels"]["description"] (or "middle" if you want to show the post text)
  Example: frames["labels"]["description"].config(text=post_data['text'])

Location → frames["labels"]["geography"]
  Example: frames["labels"]["geography"].config(text=f"Location: {post_data['Location']}")

Platform → frames["labels"]["description"] (combine with other info)
  Example: frames["labels"]["description"].config(
      text=f"Platform: {post_data['Platform']}\\nLikes: {post_data['Likes']}\\nRetweets: {post_data['Retweets']}"
  )

Sentiment → frames["labels"]["sentiment"]
  Example: frames["labels"]["sentiment"].config(text=f"Sentiment: {post_data['Sentiment']}")

Likes → frames["labels"]["description"] (combine with Platform/Retweets)
  Example: See Platform example above

Retweets → frames["labels"]["description"] (combine with Platform/Likes)
  Example: See Platform example above

RECOMMENDED MAPPING:
--------------------
- geography label → Location 
- description label → Platform, Likes, Retweets (multi-line)
- sentiment label → Sentiment
- middle label → Post_Number and text 
- filter label → Not for data display (for filter controls)
"""

def main():
    # Initialize navigation and data loading
    nav = Navigator()  # Manages current post index (1-based: 1-707)
    loader = DataLoader('LLM_data.csv')  # Loads the CSV data
    
    # Create the GUI (returns the root window and frames dict)
    root, frames = build_layout(window_title="Omar GUI", geometry="900x600")

    def on_back_pressed():
        print("Back button pressed")
        
        pass

    def on_select_post():
        print("Select button pressed")
        
        pass

    def on_next_pressed():
        print("Next button pressed")
    
        pass

    # Wire the bottom buttons to the display_logic stubs
    frames["buttons"]["back"].config(command=on_back_pressed)
    frames["buttons"]["select"].config(command=on_select_post)
    frames["buttons"]["next"].config(command=on_next_pressed)

    # (Optional) initialize some placeholder text via display_logic functions
    try:
        display_logic.update_geography(frames, "USA")
    except AttributeError:
        # if your display_logic only has button callbacks that's fine
        pass

    # Start the GUI
    root.mainloop()

if __name__ == "__main__":
    main()
