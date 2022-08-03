class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = {}
        st = []
        i = len(nums2)-1
        
        while i>=0:
            while st and nums2[i] > st[-1]:
                st.pop()
              
                #print(nums2[i])
            if len(st)==0:
                m[nums2[i]] = -1
            else:
                m[nums2[i]] = st[-1]
            st.append(nums2[i])
            i -=1
        #print(m)
            
        for i in range(len(nums1)):
            if nums1[i] in m.keys():
                nums1[i] = m[nums1[i]]
        
        return nums1
                
            
            
        
        
        