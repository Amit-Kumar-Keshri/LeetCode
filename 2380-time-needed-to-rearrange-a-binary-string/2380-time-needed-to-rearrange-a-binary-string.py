class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        l = list(s)
        l1 = sorted(l,reverse = True)
        c = 0
        n = len(l)
        if l1 == l:
            return c
        while True:
            flag = False
            j = 0
            while j < n:
                if j+1<n and l[j] == "0" and l[j+1]=="1":
                    flag = True
                    l[j], l[j+1] = l[j+1], l[j]
                    #print(j, end= ", ")
                    j += 1
                j+=1
                
            if flag == True:
                c += 1
            else:
                break
        return c