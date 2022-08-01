class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        
        curr = 0
        max_l = 0
        
        if n<3:
            return 0
        
        while curr < n:
            start = curr
            if start+1 <n and arr[start] < arr[start+1]:
                while start+1 <n and arr[start] < arr[start+1]:
                    start += 1
                    
                if start+1 <n and arr[start] > arr[start+1]:
                    while start+1 <n and arr[start] > arr[start+1]:
                        start += 1
                        
                    lenn = start - curr +1
                    if max_l < lenn:
                        max_l = lenn
            if max_l > n//2:
                return max_l
            
            if curr == start:
                curr+=1
            else:
                curr = start
        return max_l