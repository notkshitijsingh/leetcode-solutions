class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        if len(nums3) % 2 == 0:
            median_idx1 = (len(nums3)/2) - 1
            median_idx2 = len(nums3)/2
            ans = (nums3[int(median_idx1)] + nums3[int(median_idx2)])/2
        else:
            median_idx = (len(nums3) + 1)/2 - 1
            ans = nums3[int(median_idx)]
        return ans
