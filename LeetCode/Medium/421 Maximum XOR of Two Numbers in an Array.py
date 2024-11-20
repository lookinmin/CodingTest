class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = TrieNode()
        maxLen = max(nums).bit_length()
        # 제일 큰 숫자의 비트길이

        for num in nums:
            node = root

            for bit in f"{num:032b}":
                if bit not in node.children:
                    node.children[bit] = TrieNode()
                node = node.children[bit]
        
        max_xor = 0
        for num in nums:
            node = root
            xor_sum = 0
            for bit in f"{num:032b}":
                toggle = '1' if bit == '0' else '0'
                if toggle in node.children:
                    xor_sum = (xor_sum << 1) | 1
                    node = node.children[toggle]
                else:
                    xor_sum = (xor_sum << 1) | 0
                    node = node.children[bit]
            max_xor = max(max_xor, xor_sum)
        
        return max_xor
    
## --------------------------------------- trie 안쓰고 ------------------------

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res = 0
        for i in range(32)[::-1]:
            res <<= 1
            prefixes = {num >> i for num in nums}
            res += any(res^1^p in prefixes for p in prefixes)
        return res