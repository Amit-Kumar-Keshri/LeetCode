class Solution:
    def fact(self,n):
        if n==0:
            return 1
        return n*self.fact(n-1)
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        
        for n in range(numRows):
            temp = []
            for r in range(n+1):
                t = self.fact(n)//(self.fact(n-r)*self.fact(r))
                temp.append(t)
            ans.append(temp)
        return ans