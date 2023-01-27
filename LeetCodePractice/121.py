class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_ptr, best = 0, 0

        for right_ptr in range(len(prices)):
            if prices[right_ptr] < prices[left_ptr]:
                left_ptr = right_ptr
            else:
                best = max(best, prices[right_ptr] - prices[left_ptr])

        return best