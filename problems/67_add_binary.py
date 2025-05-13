import math

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        total = 0
        total += self.binaryToDecimal(a)
        total += self.binaryToDecimal(b)

        if total == 0:
            return "0"

        return self.decimalToBinary(total)
        
    def binaryToDecimal(self, binary):
        total = 0
        for i in range(len(binary)):
            if binary[-i-1] == "1":
                total += 2**i

        return total

    def decimalToBinary(self, decimal):
        indexes_to_be_populated_by_1 = []

        while decimal != 0:
            nearest_pow = int(math.log(decimal, 2))
            indexes_to_be_populated_by_1.append(nearest_pow)
            decimal = decimal - 2**nearest_pow

        binary_list = ["0"] * (max(indexes_to_be_populated_by_1) + 1)

        for index in indexes_to_be_populated_by_1:
            binary_list[index] = "1"

        binary = "".join(binary_list)

        return binary[::-1]