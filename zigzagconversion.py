def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    result = ""
    length = len(s)
    k = 0
    j = 2
    if(len(s)>numRows and numRows>1):
        while(k<len(s)):
            result = result + s[k]
            k = k + 2*numRows-j
        row = 2
        k =1
        while(row<numRows):
            result = result+s[row-1]
            temp = row*2
            k = row-1 + 2 * numRows - temp
            while(k<len(s)):
                result = result+s[k]
                k = k+temp-2
                if(k<len(s)):
                    result = result+s[k]
                k = k + 2 * numRows - temp
            row = row+1
        result = result +s[row-1]
        k = 3*numRows-3
        while(k<len(s)):
            result = result+s[k]
            k = k+2*numRows-2
        return result
    else:
        return s


print convert("AB", 1)