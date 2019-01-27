class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag=1 if x>0 else -1
        x=x if x>0 else -x
        res=0
        while x>0:
            if res*10.0 + x%10 > 2147483647:return 0
            res = res*10+x%10
            x/=10
        return res*flag   
