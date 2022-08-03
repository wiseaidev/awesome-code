class MySqrt:
    def sqrt(self, x: int) -> int:
        if x == 1:
            return x
        left, right = 0, x
        while left <= right:
            mid: int = left + (right - left) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif x < mid * mid:
                right = mid
            else:
                left = mid


__all__ = ["MySqrt"]
