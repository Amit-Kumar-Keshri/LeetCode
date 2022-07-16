class Solution:
    def searchInsert(self, arr: List[int], key: int) -> int:
        n = len(arr)
        if(key>arr[n-1]):
            return n
        elif(key<arr[0]):
            return 0
        s=0
        e=n-1
        while(s<=e):
            mid = s+(e-s)//2
            if (arr[mid]==key):
                return mid
            if arr[mid]>key:
                e=mid-1
            else:
                s=mid+1
        return s