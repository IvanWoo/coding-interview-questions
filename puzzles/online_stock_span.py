# https://leetcode.com/problems/online-stock-span/
"""
Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].

Example 1:

Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
Output: [null,1,1,1,2,1,4,6]
Explanation:
First, S = StockSpanner() is initialized.  Then:
S.next(100) is called and returns 1,
S.next(80) is called and returns 1,
S.next(60) is called and returns 1,
S.next(70) is called and returns 2,
S.next(60) is called and returns 1,
S.next(75) is called and returns 4,
S.next(85) is called and returns 6.

Note that (for example) S.next(75) returned 4, because the last 4 prices
(including today's price of 75) were less than or equal to today's price.
"""


# monotonic stack: increasing
class StockSpanner:
    def __init__(self):
        self.stack = []
        self.index = 0

    def next(self, price: int) -> int:
        self.index += 1
        ans = 1
        while self.stack and self.stack[-1][1] <= price:
            self.stack.pop()
        if self.stack:
            ans = self.index - self.stack[-1][0]
        else:
            ans = self.index
        self.stack.append((self.index, price))
        return ans


class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        ans = 1
        while self.stack and self.stack[-1][0] <= price:
            ans += self.stack.pop()[1]
        self.stack.append((price, ans))
        return ans


if __name__ == "__main__":
    obj = StockSpanner()
    for p in [100, 80, 60, 70, 60, 75, 85]:
        print(obj.next(p))
