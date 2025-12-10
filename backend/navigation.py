# Manages the current index of the social media post being viewed

from dataclasses import dataclass

# (1-732 posts from the dataset)
MAX_POST_INDEX = 732
MIN_POST_INDEX = 1

@dataclass
class Navigator:
    # Track current post index (1-based).
    current_index: int = MIN_POST_INDEX
    
    # Reset to first post.
    def initialize(self) -> None:
        self.current_index = MIN_POST_INDEX
        
    # Move to next post with wrap-around.
    def next_post(self) -> int:
        if self.current_index == MAX_POST_INDEX:
            self.current_index = MIN_POST_INDEX
        else:
            self.current_index += 1
        return self.current_index

    # Move to previous post with wrap-around.
    def prev_post(self) -> int:
        if self.current_index == MIN_POST_INDEX:
            self.current_index = MAX_POST_INDEX
        else:
            self.current_index -= 1
        return self.current_index

    # Jump to a specific post within bounds.
    def select_post(self, new_index: int) -> int:
        if MIN_POST_INDEX <= new_index <= MAX_POST_INDEX:
            self.current_index = new_index
        return self.current_index
    
    # Get current index.
    def get_current_index(self) -> int:
        return self.current_index


# ----------------------------------------------------------------------
# LOCAL TEST SCRIPT
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Testing navigation.py (Functional Logic with Wrap-Around) ---")
    
    nav = Navigator()
    
    # 1. Test Wrap-Around Forward (732 -> 1)
    nav.select_post(MAX_POST_INDEX)
    print(f"Index before Next (at 732): {nav.get_current_index()}")
    nav.next_post()
    print(f"Index after Next (Loop to 1): {nav.get_current_index()}")
    
    # 2. Test Wrap-Around Backward (1 -> 732)
    nav.select_post(MIN_POST_INDEX)
    print(f"Index before Prev (at 1): {nav.get_current_index()}")
    nav.prev_post()
    print(f"Index after Prev (Loop to 732): {nav.get_current_index()}")
    
    # 3. Test Normal Navigation (10 -> 11)
    nav.select_post(10)
    nav.next_post()
    print(f"Index after Next (Normal 10 -> 11): {nav.get_current_index()}")
    
    # 4. Test Invalid Select
    current_index_before_invalid = nav.get_current_index()
    nav.select_post(0)
    print(f"Index after Invalid Select (0): {nav.get_current_index()} (should be {current_index_before_invalid})")
