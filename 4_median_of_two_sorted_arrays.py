from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array_length = len(nums1) + len(nums2)
        i = 0
        cursor_1 = 0
        cursor_2 = 0
        ended_1 = False if len(nums1) > 0 else True
        ended_2 = False if len(nums2) > 0 else True
        
        if merged_array_length % 2 != 0:
            while i <= merged_array_length // 2:
                if ended_2 or (not ended_1 and (nums1[cursor_1] < nums2[cursor_2])):
                    median = nums1[cursor_1]
                    if cursor_1 + 1 < len(nums1):
                        cursor_1 += 1
                    else:
                        ended_1 = True
                else:
                    median = nums2[cursor_2]
                    if cursor_2 + 1 < len(nums2):
                        cursor_2 += 1
                    else:
                        ended_2 = True
                i += 1
        else:
            median1 = None
            while i <= merged_array_length // 2:
                if median1 is not None:
                    median_prev = median1
                if ended_2 or (not ended_1 and (nums1[cursor_1] < nums2[cursor_2])):
                    median1 = nums1[cursor_1]
                    if cursor_1 + 1 < len(nums1):
                        cursor_1 += 1
                    else:
                        ended_1 = True
                else:
                    median1 = nums2[cursor_2]
                    if cursor_2 + 1 < len(nums2):
                        cursor_2 += 1
                    else:
                        ended_2 = True
                i += 1
            median = (median1 + median_prev) / 2
        return median

a = Solution()
nums1 = []
nums2 = [1]
print(a.findMedianSortedArrays(nums1, nums2))

