class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mg = []
        
        
        i = 0
        j = 0
        
        while i<len(nums1) and j<len(nums2):
            
            if nums1[i] <= nums2[j]:
                mg.append(nums1[i])
                i += 1
            else:
                mg.append(nums2[j])
                j += 1
        for i in range(i,len(nums1)):
            mg.append(nums1[i])
        for i in range(j,len(nums2)):
            mg.append(nums2[i])
        
        if len(mg)%2==1:
            return mg[len(mg)//2]
        else:
            return (mg[len(mg)//2]+mg[(len(mg)//2)-1])/2