
# using Dictionary and loop   #time complexity O(1)
class Solution(object):
    def intToRoman(self, num):
     
            roman_numerals = {
                1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
                100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
                10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
            }
            result = ''
            for value, numeral in sorted(roman_numerals.items(), reverse=True):
                while num >= value:
                    num -= value
                    result += numeral
            return result

    



# Using a List of Tuples and Loop (Time complexity: O(1))
class solution(object):
    def intToRoman(self, num):
        roman_numerals = [
                (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
                (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
                (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        result = ''
        for value, numeral in roman_numerals:
                while num >= value:
                    num -= value
                    result += numeral
        return result
   
   
   
   
   
   

