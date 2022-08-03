class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        h = len(arr)-1
        
        while l<=h:
            
            m = (l+h)//2
            print(m)
            if arr[m+1] < arr[m] and arr[m] > arr[m-1]:
                return m
            elif m>=1 and arr[m] < arr[m-1]:
                h = m-1 
            else:
                l = m+1
            