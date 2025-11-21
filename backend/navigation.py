from dataclasses import dataclass

# (1-732 posts from the dataset)
MAX_POST_INDEX = 732
MIN_POST_INDEX = 1

@dataclass
class Navigator:
    """
    Purpose: Allows GUI interaction without breaking core app.
    Manages the current index of the social media post being viewed. 
    """
    # The current post index, initialized to the first post.
    current_index: int = MIN_POST_INDEX
    
    def initialize(self) -> None:
        # Initializes the navigator (resets the index to 1).
        self.current_index = MIN_POST_INDEX
        
    def next_post(self) -> int:
        """
        Implements next_post() logic  with wrap-around. 
        If at 707, it loops back to 1. Otherwise, it increments.
        """
        if self.current_index == MAX_POST_INDEX:
            self.current_index = MIN_POST_INDEX  # Loop to 1
        else:
            self.current_index += 1
        return self.current_index

    def prev_post(self) -> int:
        """
        Implements prev_post() logic with wrap-around. 
        If at 1, it loops back to 707. Otherwise, it decrements.
        """
        if self.current_index == MIN_POST_INDEX:
            self.current_index = MAX_POST_INDEX  # Loop to 707
        else:
            self.current_index -= 1
        return self.current_index

    def select_post(self, new_index: int) -> int:
        """
        Implements select_post logic. Jumps to an index if it's within 1-707.
        """
        if MIN_POST_INDEX <= new_index <= MAX_POST_INDEX:
            self.current_index = new_index
        return self.current_index
    
    def get_current_index(self) -> int:
        """Helper method for verifying the index state."""
        return self.current_index


# ----------------------------------------------------------------------
# LOCAL TEST SCRIPT
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Testing navigation.py (Functional Logic with Wrap-Around) ---")
    
    nav = Navigator()
    
    # 1. Test Wrap-Around Forward (707 -> 1)
    nav.select_post(MAX_POST_INDEX)
    print(f"Index before Next (at 707): {nav.get_current_index()}")
    nav.next_post()
    print(f"Index after Next (Loop to 1): {nav.get_current_index()}")
    
    # 2. Test Wrap-Around Backward (1 -> 707)
    nav.select_post(MIN_POST_INDEX)
    print(f"Index before Prev (at 1): {nav.get_current_index()}")
    nav.prev_post()
    print(f"Index after Prev (Loop to 707): {nav.get_current_index()}")

    # 3. Test Normal Navigation (10 -> 11)
    nav.select_post(10)
    nav.next_post()
    print(f"Index after Next (Normal 10 -> 11): {nav.get_current_index()}")
    
    # 4. Test Invalid Select
    current_index_before_invalid = nav.get_current_index()
    nav.select_post(0)

    print(f"Index after Invalid Select (0): {nav.get_current_index()} (should be {current_index_before_invalid})")
