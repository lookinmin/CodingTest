class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [str(nums[0])]
        else:
            now = nums[0]
            nxt = 0
            res = []

            for i in range(1, len(nums)):
                if nums[i - 1] + 1 != nums[i]:
                    nxt = nums[i - 1]
                    if now == nxt:
                        tmp = str(now)
                    else:
                        tmp = str(now) + "->" + str(nxt)
                    res.append(tmp)
                    now = nums[i]
                if now == nums[-1]:
                    res.append(str(now))
                if nums[i] == nums[-1] and nums[i] != now:
                    tmp = str(now) + "->" + str(nums[i])
                    res.append(tmp)
            return res

# --------------------------------------------------------------

class Solution:
    def cvt(self, a, b):
        if a == b:
            return str(a)
        return "{}->{}".format(a, b)

    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        res = []
        tmp = []
        now = nums[0]

        for num in nums:
            if num == now:
                tmp.append(num)
                now += 1
            else:
                res.append(self.cvt(tmp[0], tmp[-1]))
                tmp = [num]
                now = num + 1
        res.append(self.cvt(tmp[0], tmp[-1]))
        return res
