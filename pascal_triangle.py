from typing import List

class Solution:
    def generate(numRows: int)->List[List[int]]:
        output = []
        for row in range(numRows):
            output.append([])
            output[row].append(1)
            for element in range(1, row):
                output[row].append(output[row - 1][element - 1] + output[row - 1][element])
            if row != 0:
                output[row].append(1)
                
        return output

    print(generate(numRows=5))
