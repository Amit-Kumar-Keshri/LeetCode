class Solution:
    def productExceptSelf(self, arr: List[int]) -> List[int]:
        prd = 1
        zeros = 0
        n = len(arr)
        for i in range(n):
            if arr[i] == 0:
                zeros += 1
                continue
            prd *= arr[i]
        if zeros == 0:
            for j in range(n):
                arr[j] = prd//arr[j]
        elif zeros == 1:
            for i in range(n):
                if arr[i] == 0:
                    arr[i] = prd
                else:
                    arr[i] = 0
        else:
            for i in range(n):
                arr[i] = 0
        return arr