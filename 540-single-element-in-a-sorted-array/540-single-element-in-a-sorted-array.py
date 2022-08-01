class Solution:
    def singleNonDuplicate(self, arr: List[int]) -> int:
        n = len(arr)
        l = 0
        h = n-1
        # if n==1:
        #     return arr[0]
        
        while l<=h:
            m = (l+h)//2
            if (m == 0 or arr[m-1] != arr[m]) and (m == n-1 or arr[m+1] != arr[m]):
                return arr[m]
            
            elif m%2==0:
                if arr[m] == arr[m-1]:
                    h = m-1
                elif m+1<n and arr[m] == arr[m+1]:
                    l = m+1
                # else:
                #     return arr[m]
            elif m%2==1:
                if arr[m] == arr[m-1]:
                    l = m+1
                elif m+1<n and arr[m] == arr[m+1]:
                    h = m-1
                # else:
                #     return arr[m]
            else:
                return arr[0]
                
    