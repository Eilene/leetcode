def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    s = str(x)
    print s
    length = len(s)-1
    midlen = length/2
    flag = True
    for i in range(0,midlen+1):
        if(s[i]!=s[length-i]):
            flag = False
            break
    return flag



print isPalindrome(14445678)
