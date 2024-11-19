import heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = [1]
        seen = set(heap)
        num = 1

        for _ in range(n):
            num = heapq.heappop(heap)
            for prime in primes:
                tmp = num * prime
                if tmp not in seen:
                    seen.add(tmp)
                    heapq.heappush(heap, tmp)
        return num