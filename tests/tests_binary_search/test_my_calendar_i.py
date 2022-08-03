import pytest

from solutions import (
    MyCalendar,
)


def test_book():
    my_calendar = MyCalendar()
    events = [[None, None], [10, 20], [15, 25], [20, 30]]
    results = []
    ref = [None, True, False, True]
    for event in events:
        results.append(my_calendar.book(event[0], event[1]))
    assert ref == results


def test_constraints():
    with pytest.raises(AssertionError):
        my_calendar = MyCalendar()
        events = [[10, 20]] * 1001
        for event in events:
            my_calendar.book(event[0], event[1])

    with pytest.raises(AssertionError):
        my_calendar = MyCalendar()
        events = [[10**9 + 1, 20]] * 1000
        for event in events:
            my_calendar.book(event[0], event[1])

    with pytest.raises(AssertionError):
        my_calendar = MyCalendar()
        events = [[10, 10**9 + 1]] * 1000
        for event in events:
            my_calendar.book(event[0], event[1])
