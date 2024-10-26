# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        while 1:
            mid = (start + end) // 2
            if isBadVersion(mid) == False:
                start = mid + 1
                continue
            elif isBadVersion(mid) == True and mid > 1 and isBadVersion(mid - 1) == True:
                end = mid - 1
                continue
            elif isBadVersion(mid) == True and isBadVersion(mid - 1) == False:
                return mid