# using recursive approach
class Solution:
    def numberToWords(self,num):
            def one(num):
                switcher = {
                    1: 'One',
                    2: 'Two',
                    3: 'Three',
                    4: 'Four',
                    5: 'Five',
                    6: 'Six',
                    7: 'Seven',
                    8: 'Eight',
                    9: 'Nine'
                }
                return switcher.get(num)

            def two_less_20(num):
                switcher = {
                    10: 'Ten',
                    11: 'Eleven',
                    12: 'Twelve',
                    13: 'Thirteen',
                    14: 'Fourteen',
                    15: 'Fifteen',
                    16: 'Sixteen',
                    17: 'Seventeen',
                    18: 'Eighteen',
                    19: 'Nineteen'
                }
                return switcher.get(num)

            def ten(num):
                switcher = {
                    2: 'Twenty',
                    3: 'Thirty',
                    4: 'Forty',
                    5: 'Fifty',
                    6: 'Sixty',
                    7: 'Seventy',
                    8: 'Eighty',
                    9: 'Ninety'
                }
                return switcher.get(num)

            def two(num):
                if not num:
                    return ''
                elif num < 10:
                    return one(num)
                elif num < 20:
                    return two_less_20(num)
                else:
                    tens_digit = num // 10
                    rest = num - tens_digit * 10
                    return ten(tens_digit) + ' ' + one(rest) if rest else ten(tens_digit)

            def three(num):
                hundred_digit = num // 100
                rest = num - hundred_digit * 100
                if hundred_digit and rest:
                    return one(hundred_digit) + ' Hundred ' + two(rest)
                elif not hundred_digit and rest:
                    return two(rest)
                elif hundred_digit and not rest:
                    return one(hundred_digit) + ' Hundred'

            billion = num // 1000000000
            num %= 1000000000
            million = num // 1000000
            num %= 1000000
            thousand = num // 1000
            num %= 1000
            result = ''
            if billion:
                result = three(billion) + ' Billion'
            if million:
                result += ' ' if result else ''
                result += three(million) + ' Million'
            if thousand:
                result += ' ' if result else ''
                result += three(thousand) + ' Thousand'
            if num:
                result += ' ' if result else ''
                result += three(num)
            return result or 'Zero'





# using iterative method

    # def numberToWords(self, num: int) -> str:
    #     if num == 0:
    #         return "Zero"
    #     ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    #     tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    #     teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    #     suffixes = ["", "Thousand", "Million", "Billion", "Trillion", "Quadrillion", "Quintillion", "Sextillion", "Septillion", "Octillion", "Nonillion", "Decillion"]
    #     words = []
    #     i = 0
    #     while num > 0:
    #         triplet = num % 1000
    #         num = num // 1000
    #         if triplet == 0:
    #             i += 1
    #             continue
    #         temp = []
    #         if triplet // 100 > 0:
    #             temp.append(ones[triplet // 100])
    #             temp.append("Hundred")
    #         if triplet % 100 >= 10 and triplet % 100 <= 19:
    #             temp.append(teens[triplet % 10])
    #         else:
    #             if triplet % 100 >= 20:
    #                 temp.append(tens[triplet % 100 // 10])
    #             if triplet % 10 > 0:
    #                 temp.append(ones[triplet % 10])
    #         if i > 0:
    #             temp.append(suffixes[i])
    #         words = temp + words
    #         i += 1
    #     return " ".join(words)