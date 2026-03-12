from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ele = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(len(nums)-1, i, -1):
                if j < len(nums)-1 and nums[j] == nums[j+1]:
                    continue       
                right = i + 1        
                left = j - 1
                while right < left:
                    total = nums[i] + nums[j] + nums[right] + nums[left]
                    print(i, right, left, j, total)
                    if total < target:
                        right += 1
                    elif total > target:
                        left -= 1
                    else:
                        ele.append([nums[i], nums[j], nums[right], nums[left]])
                        right += 1
                        while nums[right] == nums[right-1] and right < left:
                            right += 1
        return ele

print(Solution().fourSum([-3,-1,0,2,4,5], 2))
