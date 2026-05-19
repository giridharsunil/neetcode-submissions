class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        for i in range(m):
            if i >= m/2:
                break
            matrix[i], matrix[m-1-i] = matrix[m-1-i], matrix[i]
        for i in range(m):
            for j in range(i+1, m):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix)

        