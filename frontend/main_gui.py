# main_gui.py
from layout_components import build_layout
import display_logic

def main():
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
