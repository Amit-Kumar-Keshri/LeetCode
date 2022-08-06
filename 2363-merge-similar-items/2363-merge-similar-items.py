class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        m = {}

        for i in range(len(items1)):
            if items1[i][0] not in m.keys():
                m[items1[i][0]] = items1[i][1]
                
        #print(m)
        for i in range(len(items2)):
            if items2[i][0] in m.keys():
                m[items2[i][0]] = m[items2[i][0]]+ items2[i][1]
            else:
                m[items2[i][0]] = items2[i][1]
        # print(m)
        ans = [] 
        
        for i in m:
            ans.append([i,m[i]]) 
        
        return sorted(ans, key = lambda x:x[0])