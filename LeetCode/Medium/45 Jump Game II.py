class Solution:
    def jump(self, nums: List[int]) -> int:
        near, far, step = 0, 0, 0

        while far < len(nums) - 1:
            can_reach = 0
            for i in range(near, far + 1):
                can_reach = max(can_reach, i + nums[i])
            near = far + 1
            far = can_reach
            step += 1

        return step