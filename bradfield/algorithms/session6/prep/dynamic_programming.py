# From http://bradfieldcs.com/algos/recursion/dynamic-programming/

# 0,1,1,2,3,5,8,13,21...
# f(n)=f(n−1)+f(n−2).


# With 0 and 1 as base case
# This is recursive but carrys losts of redundant calls
def fib(n):
    if n <= 1:
        return n  # base cases: return 0 or 1 if n is 0 or 1, respectively
    return fib(n - 1) + fib(n - 2)

# This is Dynamic or 'Bottom-Up' rather than top-down like above

# At any point in time we only need to retain a memory of the previous two calculations,
# and we never obtain the same sum twice.

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = a + b, a
    return a

# Putting our base case and general case together, we obtain a succinct recursive solution:
def num_paths(height, width):
    if height == 0 or width == 0:
        return 1
    return num_paths(height, width - 1) + num_paths(height - 1, width)

def num_paths_dp(height, width):
    memo = [[1] * (width + 1) for _ in range(0, height + 1)]
    for i, row in enumerate(memo):
        for j, _ in enumerate(row):
            if i == 0 or j == 0:
                continue
            memo[i][j] = memo[i - 1][j] + memo[i][j - 1]
    return memo[-1][-1]