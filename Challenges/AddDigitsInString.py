class Solution():
    def __init__(self, num):
        self.num = num

    def addDigits(self, num):
        total = 0
        digitList = [digit for digit in str(self.num)]
        for digit in digitList:
            total = total + int(digit)
        return total


a = Solution(159)
print(a.addDigits(a.num))