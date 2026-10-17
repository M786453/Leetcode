class Solution(object):

    def maxProfit(self, prices):

        profit = 0

        buy_price = prices[0]

        for prc in prices:

            if prc < buy_price:
                buy_price = prc
            else:
                if prc - buy_price > profit:
                    profit = prc -buy_price

        return profit

obj = Solution()

print("Answer: ", obj.maxProfit([7,6,4,3,1]))

