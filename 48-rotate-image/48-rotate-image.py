class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        r = len(matrix)
        c = len(matrix[0])
        #transpose of matrix horizental to vertical
        for i in range(r):
            for j in range(i+1,c):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        #reverse in list from 0 to last and soon
        for i in range(r):
            for j in range(c//2):
                matrix[i][j], matrix[i][c-j-1] = matrix[i][c-j-1], matrix[i][j]
