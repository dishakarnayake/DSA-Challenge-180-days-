class Solution:
    def lemonadeChange(self, bills):
        five, ten = 0, 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else:  # bill == 20
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True





class Solution:
    def lemonadeChange(self, bills):
        wallet = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            wallet[bill] += 1
            if bill == 10:
                if wallet[5] > 0:
                    wallet[5] -= 1
                else:
                    return False
            elif bill == 20:
                if wallet[10] > 0 and wallet[5] > 0:
                    wallet[10] -= 1
                    wallet[5] -= 1
                elif wallet[5] >= 3:
                    wallet[5] -= 3
                else:
                    return False
        return True



from collections import Counter

class Solution:
    def lemonadeChange(self, bills):
        wallet = Counter()
        for bill in bills:
            wallet[bill] += 1
            if bill == 10:
                if wallet[5] > 0:
                    wallet[5] -= 1
                else:
                    return False
            elif bill == 20:
                if wallet[10] > 0 and wallet[5] > 0:
                    wallet[10] -= 1
                    wallet[5] -= 1
                elif wallet[5] >= 3:
                    wallet[5] -= 3
                else:
                    return False
        return True
