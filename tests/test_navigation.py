# Tests all navigation logic (Next, Back, Select) including 
# wrap-around and validation boundary conditions
import os
import sys
import pandas as pd
import pytest

# Mirroring team standard for absolute imports 
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

try:
    import backend.navigation as nav_module
    # Extract components from the imported module
    Navigator = nav_module.Navigator
    MIN_POST_INDEX = nav_module.MIN_POST_INDEX
    MAX_POST_INDEX = nav_module.MAX_POST_INDEX
except ImportError as e:
    # This should now only fail if the file structure is wrong, not the import logic itself.
    raise ImportError(f"Failed to import Navigator module. Check backend/navigation.py. Details: {e}")

# Fixture to create a fresh Navigator instance for each test
@pytest.fixture
def setup_navigator():
    dummy_df = pd.DataFrame({'col': range(MAX_POST_INDEX)})
    return Navigator(dummy_df)

# ----------------------------------------------------------------------
# Navigation Logic Tests
# ----------------------------------------------------------------------
class TestNavigation:
    # Test moving from the MAX index (732) back to the MIN index (1)
    def test_next_post_wrap_around(self, setup_navigator):
        nav = setup_navigator
        nav.current_index = MAX_POST_INDEX
        nav.next_post()
        assert nav.current_index == MIN_POST_INDEX

    # Test moving from the MIN index (1) back to the MAX index (732)
    def test_prev_post_wrap_around(self, setup_navigator):
        nav = setup_navigator
        nav.current_index = MIN_POST_INDEX
        nav.prev_post()
        assert nav.current_index == MAX_POST_INDEX

    # Test moving from 50 to 51
    def test_next_post_normal(self, setup_navigator):
        nav = setup_navigator
        nav.current_index = 50
        nav.next_post()
        assert nav.current_index == 51
        
    # Test moving from 50 to 49
    def test_prev_post_normal(self, setup_navigator):
        nav = setup_navigator
        nav.current_index = 50
        nav.prev_post()
        assert nav.current_index == 49

    # Test selecting a valid post ID (e.g., 400)
    def test_select_post_valid_number(self, setup_navigator):
        nav = setup_navigator
        nav.current_index = 1 
        nav.select_post(400)
        assert nav.current_index == 400

    # Test selecting a post ID higher than the max count (e.g., 1000). 
    # Index should not change.
    def test_select_post_out_of_range_high_no_change(self, setup_navigator):
        nav = setup_navigator
        nav.current_index = 50 
        nav.select_post(MAX_POST_INDEX + 50) # Invalid ID
        assert nav.current_index == 50

    # Test selecting a post ID lower than the min count (e.g., 0).
    # Index should not change.
    def test_select_post_out_of_range_low_no_change(self, setup_navigator):
        nav = setup_navigator
        nav.current_index = 50 
        nav.select_post(0)
        assert nav.current_index == 50

    # Test handling non-integer input (simulating cancel or bad user input from the GUI).
    # Should raise a TypeError.
    def test_select_post_non_numeric_input_raises_error(self, setup_navigator):
        nav = setup_navigator
        with pytest.raises(TypeError):
            nav.select_post("abc")
