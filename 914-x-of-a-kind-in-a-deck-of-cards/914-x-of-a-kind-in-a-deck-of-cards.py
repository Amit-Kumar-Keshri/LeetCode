class Solution:
    def gcd(self,x,y):
        if y==0:
            return x
        return gcd(y,x % y)
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        res = {}
        for el in deck:
            if el in res.keys():
                res[el] +=1
            else:
               res[el] = 1
        ans = res[deck[0]]

        ans = res[deck[0]]
        for i in res:
            ans = self.gcd(ans, res[i])
        if ans>1:
            return 1
        else:
            return 0