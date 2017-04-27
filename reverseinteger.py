import math
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    s= str(x)
    length = len(s)-1
    temp = ''
    if(s[0]not in ['-','+']):
        while(length>-1):
            temp = temp+s[length]
            length -=1
    else:
        temp = temp+s[0]
        while (length > 0):
            temp = temp + s[length]
            length -= 1
    temp = int(temp)
    if(math.abs(temp)>math.pow(2,31)):
        temp=0
    return temp
print reverse(123)
print reverse(-123)
