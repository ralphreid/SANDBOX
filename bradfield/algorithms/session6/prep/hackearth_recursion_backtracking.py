# Number of Recursive calls: There is an upper limit to the number of recursive calls that can be made. To prevent this make sure that your base case is reached before stack size limit exceeds.
#
# So, if we want to solve a problem using recursion, then we need to make sure that:
#
# The problem can broken down into smaller problems of same type.
# Problem has some base case(s).
# Base case is reached before the stack size limit exceeds.


# N-Queens Problem:

# Given a chess board having cells, you need to place N queens on the board in such a way that no queen attacks any other queen.

# Input:
# The only line of input consists of a single integer denoting N.

# Output:
# If it is possible to place all the N queens in such a way that no queen attacks another queen, then print "YES" (without quotes)
# in first line, then print N lines having N integers.

# If it is not possible to place all N queens in the desired way, then print "NO" (without quotes).

# Constraints:
#
# 1 ≤ N ≤ 10.

