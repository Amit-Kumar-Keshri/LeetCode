class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldier = []
        r= len(mat)
        c= len(mat[0])
        for i in range(r):
            count = 0
            for j in range(c):
                if mat[i][j] == 1:
                    count += 1
            soldier.append(count)
        print(soldier)
        ans = []
        for i in range(len(soldier)):
            m = 1000
            x = 0
            for j in range(len(soldier)):
                if soldier[j] < m:
                    m = soldier[j]
                    x = j
            ans.append(x)
            soldier[x] = 9999999
        return ans[:k]
            
                
                    