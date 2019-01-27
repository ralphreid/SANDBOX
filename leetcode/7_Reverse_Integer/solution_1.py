class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:   return int(str(x)[1:][::-1])*-1
        else:       return int(str(x)[::-1])
