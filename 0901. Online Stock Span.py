class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        cnt = 1
        while self.stack and self.stack[-1][0] <= price:
            old_price, old_cnt = self.stack.pop()
            cnt += old_cnt
        self.stack.append((price, cnt))
        
        return cnt

