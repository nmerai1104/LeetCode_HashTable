class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_mapping = {
            '2': 'abc', '3': 'def',
            '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }

        def backtrack(index, current):
            if index == len(digits):
                result.append(current)
                return

            current_digit = digits[index]
            for letter in digit_mapping[current_digit]:
                backtrack(index + 1, current + letter)

        result = []
        backtrack(0, '')
        return result
