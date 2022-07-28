class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        
        while l<=r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            
            if nums[l]<=nums[m]:
                if nums[l] <= target and  target < nums[m]:
                    r = m-1
                else:
                    l = m+1
            else:
                if nums[r] >= target and nums[m] < target:
                    l = m+1
                else:
                    r = m-1
            
        return -1
#     class Solution {
# public:
#     int search(vector<int>& nums, int target) {
        
#         int low = 0 , high = nums.size()-1;
        
#         while(low <= high)
#         {
#             int mid = (low + high)/2;
#             if(nums[mid] == target)
#                 return mid;
            
#             if(nums[low] <= nums[mid])
#             {
#                 if(target >= nums[low] && target < nums[mid])
#                     high = mid-1;
#                 else
#                     low = mid+1;
#             }
#             else
#             {
#                 if(target > nums[mid] && target <= nums[high])
#                     low = mid+1;
#                 else
#                     high = mid-1;
#             }
#         }
        
#         return -1;
        
#     }
# }; 