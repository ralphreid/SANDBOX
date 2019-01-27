class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reverse = 0
        while(x > 0):
            reminder = x %10
            reverse = (reverse * 10) + reminder
            x = x //10
        
        return reverse
