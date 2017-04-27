import math
def isPowerOfFour(num):
    """
    :type num: int
    :rtype: bool
    """
    x = math.log(num)
    y = math.log(4)
    if(x%y==0):
        return True
    else:
        return False
print isPowerOfFour(176)