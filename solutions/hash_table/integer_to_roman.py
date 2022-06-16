class Solution:
    def int_to_roman(self, num: int) -> str:
        if num < 1:
            return ""
        assert 1 <= num <= 3999
        ret: list[str] = []
        sym_val: dict[int, str] = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        for number in sym_val:
            ret.append((num // number) * sym_val[number])
            num %= number

        return "".join(ret)


IntegerToRomanSolution = Solution

__all__ = [
    "IntegerToRomanSolution",
]
