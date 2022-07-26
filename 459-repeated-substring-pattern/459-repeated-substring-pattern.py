class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = []
        n = len(s)
        for i in range(1,(n//2)+1):
            if n%i==0:
                a= s[0:i]
                #print(a)
                flag = True
                for j in range(0,n,len(a)):
                    ans = s[j:j+i]
                    #print(ans)
                    if a != ans:
                        #print("x")
                        flag = False
                        break     
                if flag==True:
                    return True
        return False
                        
        