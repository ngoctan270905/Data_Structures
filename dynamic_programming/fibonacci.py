# Tính số Fibonacci thứ n bằng phương pháp Lập trình động.
def fibonacci(n):

    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

n = 10
print(fibonacci(n))


# In ra toàn bộ dãy Fibonacci
def fibonacci_sequence(n):

    if n == 0:
        return []

    if n == 1:
        return [0]

    dp = [0, 1]

    for i in range(2, n):
        insert = dp[i - 1] + dp[i - 2]
        dp.append(insert)

    return dp

n = 10
print(f"Dãy fibonacci là: {fibonacci_sequence(n)}")

