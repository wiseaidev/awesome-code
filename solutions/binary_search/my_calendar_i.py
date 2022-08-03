class MyCalendar:
    def __init__(self):
        self.calendar = []
        self.nb_book = 0

    def book(self, start: int, end: int) -> bool:
        if not start or not end:
            return None
        self.nb_book += 1
        assert 0 <= start <= 10**9
        assert 0 <= end <= 10**9
        assert 0 <= self.nb_book <= 1000

        def helper(nums: list[int], target: int) -> int:
            left, right = 0, len(nums)
            while left < right:
                mid: int = left + (right - left) // 2
                if target <= nums[mid][0]:
                    right = mid
                else:
                    left = mid + 1
            return left

        index: int = helper(self.calendar, start)
        if index > 0 and self.calendar[index - 1][1] > start:
            return False
        if index < len(self.calendar) and end > self.calendar[index][0]:
            return False
        self.calendar.insert(index, [start, end])
        return True


__all__ = ["MyCalendar"]
