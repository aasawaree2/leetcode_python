class Solutions:
    def maxProfit(self, prices):
        buy = float('inf')
        profit = 0

        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                profit = max(profit, prices[i] - buy)
        return profit


def main():
    s = Solutions()
    a = s.maxProfit([7, 1, 5, 3, 6, 4])
    print(a)


if __name__ == '__main__':
    main()
