from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            right = i + 1
            left = len(nums) - 1
            while right < left:
                total = nums[i] + nums[right] + nums[left]
                if abs(target - total) <= abs(target - closest_sum):
                    closest_sum = total
                if total < target:
                    right += 1
                elif total > target:
                    left -= 1 
                else:
                    break
        return closest_sum

print(Solution().threeSumClosest([-1,1,0,2], 1))