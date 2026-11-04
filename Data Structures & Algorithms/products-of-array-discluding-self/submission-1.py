class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n   # prefix[i] = product of everything LEFT of i
        suffix = [1] * n   # suffix[i] = product of everything RIGHT of i

        # Build prefix left to right. prefix[0] stays 1 (nothing to its left).
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # Build suffix right to left. suffix[n-1] stays 1 (nothing to its right).
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        # Answer at i = left product × right product
        return [prefix[i] * suffix[i] for i in range(n)]