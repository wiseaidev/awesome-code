class Solution:
    def reorder_log_files(self, logs: list[str]) -> list[str]:
        assert 1 <= len(logs) <= 100

        def sorting_algorithm(log):
            assert 3 <= len(log) <= 100
            # Is a numerical log, make sure these entries appear on the right
            # side without further sorting.
            if log[-1].isnumeric():
                # A tuple of one element. One element tuples need a trailing comma so t
                # hey are not confused with (1) by python.
                return (1,)

            # Is an alphabetical log, use 0 so they are always to the left of the numerical logs,
            # then use the more complex sorting rules for just the alphabetical logs.
            left_side, right_side = log.split(" ", maxsplit=1)
            return (0, right_side, left_side)

        # Sort the logs according to the function we defined.
        return sorted(logs, key=sorting_algorithm)


ReorderDataLogFiles = Solution

__all__ = [
    "ReorderDataLogFiles",
]
