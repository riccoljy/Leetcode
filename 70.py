def count(n):
    dp = {}
    def helper(n):
        if n in dp: return dp[n]
        if n <= 2:
            dp[n] = n
            return n
        dp[n] = (helper(n-1) + helper(n-2))
        return dp[n]
    return helper(n)

print(count(int(input())))
