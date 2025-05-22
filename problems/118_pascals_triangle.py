class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []
        for i in range(1, numRows + 1):
            if i == 1:
                output.append([1])
            elif i == 2:
                output.append([1, 1])
            else:
                tmp = [1]
                for y in range(1, i - 1):
                    tmp.append(output[i - 2][y - 1] + output[i - 2][y])
                tmp.append(1)

                output.append(tmp)
        return output
