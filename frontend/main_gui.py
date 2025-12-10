# Entry point to program to wire together layout, data loading, navigation,
# display, and graphs for the GUI
import sys
import os

# Add parent directory to path to import backend modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from layout_components import build_layout
import display_logic
import graph_utils
from backend.navigation import Navigator
from backend.data_loader import DataLoader

def main():
    # Initialize navigation and data loading
    nav = Navigator()  # Manages current post index (1-based: 1-732)
    loader = DataLoader('LLM_data_final.csv')  # Loads the CSV data
    print("Data Loaded")
    
    # Create the GUI first (returns the root window and frames dict)
    root, frames = build_layout(window_title="Omar GUI", geometry="900x600")

    # Initialize display logic to load images after the root window is created
    display_logic.init_display_logic(root) # Pass root for proper Tkinter context

    # Helper function to display a post dictionary
    def _display_post_dict(post_dict):
        if not post_dict:
            print("[main_gui] No post data to display.")
            return
        
        # Geography: accept either a string or dict key
        display_logic.update_geography(frames, post_dict.get('Location', post_dict.get('Location', 'Unknown')))
        
        # Description panel: pass the whole dict (display_logic will extract platform/likes/etc)
        display_logic.update_description(frames, post_dict)
        
        # Sentiment:
        display_logic.update_sentiment(frames, post_dict.get('Sentiment', 'Unknown'))
        
        # **MIDDLE PANEL LOGIC:**
        # Pass a non-callable value (the post number text) to display_logic.update_middle
        # This triggers the 'else' block in update_middle, which is now configured
        # to display the 'phonescreen.png' image and trigger the resizing logic
        try:
            middle_content = f"Post #{post_dict.get('Post_Number', 'N/A')}"
            display_logic.update_middle(frames, middle_content)
        except Exception as e:
            print(f"[main_gui] Error updating middle panel for post: {e}")

    # Handler for back button
    def on_back_pressed():
        print("Back button pressed")
        new_index = nav.prev_post()
        idx0 = new_index - 1
        post = loader.get_post_by_index(idx0)
        if post:
            _display_post_dict(post)
        else:
            print("[main_gui] No post at index", idx0)

    # Handler for select button
    def on_select_post():
        print("Select button pressed")
        try:
            import tkinter.simpledialog as simpledialog
            # Ask user for post number (1-based)
            answer = simpledialog.askinteger("Select Post", "Enter post number (1 - 732):", minvalue=1, maxvalue=9999)
            if answer is None:
                return
            nav.select_post(answer)
            idx0 = nav.get_current_index() - 1
            post = loader.get_post_by_index(idx0)
            if post:
                _display_post_dict(post)
            else:
                print(f"[main_gui] Post #{answer} not found")
        except Exception as e:
            print("[main_gui] Error in select dialog:", e)

    # Handler for next button
    def on_next_pressed():
        print("Next button pressed")
        new_index = nav.next_post()
        idx0 = new_index - 1
        post = loader.get_post_by_index(idx0)
        if post:
            _display_post_dict(post)
        else:
            print("[main_gui] No post at index", idx0)

    # Handler for sentiment by likes button
    def sxlButton():
        display_logic.update_middle(frames, graph_utils.sentByLikes)

    # Handler for sentiment by post number button
    def sxpnButton(): 
        display_logic.update_middle(frames, graph_utils.sentByPostNum)

    # Handler for platform by likes button
    def pxlButton():
        display_logic.update_middle(frames, graph_utils.platformByLikes)

    # Handler for base button
    def baseButton():
        display_logic.update_middle(frames, graph_utils.postnumByLoc)


    # Wire the bottom buttons to the display_logic stubs if layout provides them
    try:
        frames["buttons"]["back"].config(command=on_back_pressed)
        frames["buttons"]["select"].config(command=on_select_post)
        frames["buttons"]["next"].config(command=on_next_pressed)

        #Vertical Buttons
        frames["filter_buttons"]["btn1"].config(command=sxlButton)
        frames["filter_buttons"]["btn2"].config(command=sxpnButton)
        frames["filter_buttons"]["btn3"].config(command=pxlButton)
        frames["filter_buttons"]["btn4"].config(command=baseButton)
    except Exception as e:
        print("[main_gui] Warning: could not wire buttons automatically:", e)

    # Initialize first post display on startup
    try:
        # Initialize first post display on startup
        first_idx0 = nav.get_current_index() - 1
        first_post = loader.get_post_by_index(first_idx0)
        if first_post:
            # Displays first post's data and the phone screen image in the middle
            _display_post_dict(first_post) 
        else:
            print("[main_gui] No data available to initialize first post.")
    except Exception as e:
        print("[main_gui] Error initializing first post:", e)

    # Show Graph Immediately (display_logic.update_middle will render scatter if None passed)
    try:
        # Overwrite the phone screen image with the base graph on startup
        display_logic.update_middle(frames, graph_utils.postnumByLoc)
    except Exception:
        pass

    # Start the GUI
    root.mainloop()

if __name__ == "__main__":
    main()