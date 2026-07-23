class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums2 = nums.copy()
        nums2.sort()
        res = []
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums2) -1 
            while j < k:
                print([nums2[i], nums2[j], nums2[k]])
                if nums2[i] + nums2[j] + nums2[k] < 0:
                    j += 1
                elif nums2[i] + nums2[j] + nums2[k] > 0:
                    k -= 1
                else:
                    if [nums2[i], nums2[j], nums2[k]] not in res:
                        res.append([nums2[i], nums2[j], nums2[k]])
                    break
        
        return res
