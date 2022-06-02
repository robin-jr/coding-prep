from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r= len(matrix)
        c= len(matrix[0])
        t_mat = [[None]*r for _ in range(c)]
        for i in range(0,r):
            for j in range(0,c):
                t_mat[j][i] = matrix[i][j]
        return t_mat

matrix = [[1,2,3],[4,5,6]]
s = Solution()
x = s.transpose(matrix)
print(x)
        