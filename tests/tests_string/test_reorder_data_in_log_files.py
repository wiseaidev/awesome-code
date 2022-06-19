import pytest

from solutions import (
    ReorderDataLogFiles,
)


@pytest.fixture
def solution():
    return ReorderDataLogFiles()


def test_reorder_data_in_log_files_case1(solution):
    ref = [
        "let1 art can",
        "let3 art zero",
        "let2 own kit dig",
        "dig1 8 1 5 1",
        "dig2 3 6",
    ]
    logs = [
        "dig1 8 1 5 1",
        "let1 art can",
        "dig2 3 6",
        "let2 own kit dig",
        "let3 art zero",
    ]
    result = solution.reorder_log_files(logs)
    assert all([result, ref])


def test_reorder_data_in_log_files_case2(solution):
    ref = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
    logs = ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]
    result = solution.reorder_log_files(logs)
    assert all([result, ref])


def test_constraints(solution):
    with pytest.raises(AssertionError):
        logs = ["f" * 101]
        solution.reorder_log_files(logs)

    with pytest.raises(AssertionError):
        logs = ["f"] * (101)
        solution.reorder_log_files(logs)
