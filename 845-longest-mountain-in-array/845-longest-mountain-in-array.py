class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        
        curr = 0
        max_l = 0
        
        if n<3:
            return 0
        
        while curr < n:
            start = curr
            lenn = 0
            flag = False
            flag1 = False
            # if start+1 <n and arr[start] < arr[start+1]:
            while start+1 <n and arr[start] < arr[start+1]:
                start += 1
                lenn +=1
                flag = True
            # if start+1 <n and arr[start] > arr[start+1]:
            while start+1 < n and arr[start] > arr[start+1]:
                start += 1
                lenn +=1
                flag1 = True
            if lenn != 0:
                lenn+=1
            
            if flag and flag1 and max_l < lenn:
                max_l = lenn
            if max_l > n//2:
                return max_l
            
            if curr == start:
                curr+=1
            else:
                curr = start
        return max_l