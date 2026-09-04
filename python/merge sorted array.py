class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        sum1 = sorted([nums1[i] for i in range(len(nums1)) if i <m]+[nums2[i] for i in range(len(nums2)) if i <n])
        nums1[:] = sum1
               
      
