class Solution:
    def fact(self,n):
        if n==0:
            return 1
        return n*self.fact(n-1)
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        for i in range(rowIndex+1):
            t = self.fact(rowIndex)//(self.fact(rowIndex-i)*self.fact(i))
            ans.append(t)
            
        return ans