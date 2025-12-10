# Test cases for graph and filters functionality
# Note: uses monkeypatch to mock file reading and dataframe creation
# 1) Graph path/file existence: handle missing or renamed CSV gracefully.
# 2) Graph should handle empty data gracefully (no rows after filtering).
# 3) Filter with no criteria: returns all rows.
# 4) Filter that returns 0 rows: graph/filter should handle empty data gracefully.

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
import pytest

import frontend.graph_utils as graph_utils
import backend.filter_logic as filter_logic


# Graph path/file existence: handle missing or renamed CSV gracefully.
@pytest.mark.xfail(reason="graph_utils functions currently raise on missing CSV")
def test_graph_missing_file(monkeypatch):
    def fake_read_csv(*args, **kwargs):
        raise FileNotFoundError("missing file")
    monkeypatch.setattr(graph_utils.pd, "read_csv", fake_read_csv)
    graph_utils.postnumByLoc()  # should not hard-crash once handled gracefully


# Graph should handle empty data gracefully (no rows after filtering).
def test_graph_empty_dataframe(monkeypatch):
    empty_df = pd.DataFrame(columns=["Post_Number", "Location"])
    monkeypatch.setattr(graph_utils.pd, "read_csv", lambda *a, **k: empty_df)
    fig = graph_utils.postnumByLoc()
    assert fig is not None


# Filter with no criteria: returns all rows.
def test_filter_no_criteria_returns_all():
    df = pd.DataFrame(
        {"Platform": ["Twitter", "Facebook"], "Location": ["USA", "UK"], "Likes": [10, 20], "Retweets": [1, 2], "Sentiment": ["Positive", "Negative"]}
    )
    result = filter_logic.filter_dataframe(df)
    assert len(result) == len(df)


# Filter that returns 0 rows: graph/filter should handle empty data gracefully.
def test_filter_returns_empty():
    df = pd.DataFrame(
        {"Platform": ["Twitter", "Facebook"], "Location": ["USA", "UK"], "Likes": [10, 20], "Retweets": [1, 2], "Sentiment": ["Positive", "Negative"]}
    )
    result = filter_logic.filter_dataframe(df, platform="instagram")  # no matches
    assert result.empty

