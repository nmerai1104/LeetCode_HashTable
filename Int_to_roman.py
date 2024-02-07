class Solution:
    @staticmethod
    def intToRoman(num: int) -> str:
        roman_dict = {
            1000: "M", 900: "CM", 500: "D", 400: "CD",
            100: "C", 90: "XC", 50: "L", 40: "XL",
            10: "X", 9: "IX", 5: "V", 4: "IV",
            1: "I"
        }

        roman_num = ''
        for value, symbol in roman_dict.items():
            while num >= value:
                roman_num += symbol
                num -= value

        return roman_num

# Example usage:
number = 22
roman_representation = Solution.intToRoman(number)
print(f"The Roman numeral representation of {number} is: {roman_representation}")
