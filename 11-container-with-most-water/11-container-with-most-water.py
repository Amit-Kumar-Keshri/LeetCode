class Solution:
    def maxArea(self, arr: List[int]) -> int:
        m_w = 0
        left = 0
        right = len(arr)-1
        while left<right:
            hl, hr = arr[left], arr[right]
            curr_w = (min(hl,hr))*(right-left)
            if curr_w > m_w:
                m_w = curr_w
            if hl <= hr:
                left += 1
            if hr <= hl:
                right -= 1
        return m_w
               