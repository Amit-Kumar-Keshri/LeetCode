class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n=len(nums1)
        m=len(nums2)
        if m<n:
            return self.findMedianSortedArrays(nums2,nums1)
        start=0
        end=n
        while start<=end:
            i1=int((start+end)/2)
            i2=int((m+n+1)/2)-i1
            min1=1000000 if i1==n else nums1[i1]
            min2=1000000 if i2== m else nums2[i2]
            max1=-1000000if i1==0 else nums1[i1-1]
            max2=-1000000 if i2==0 else nums2[i2-1]

            if max1<=min2 and max2<=min1:
                if (m+n)%2==0:
                    return (max(max1,max2)+min(min1,min2))/2
                else:
                    return max(max1,max2)
            elif max1>min2:
                end=i1-1
            elif max2>min1:
                start=i1+1
        return 0 