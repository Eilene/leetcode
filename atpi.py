def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """

    if (len(str) > 1):
        k = 0
        temp = 0
        str = ''.join(str.split(" "))
        while (str[k] in ["+", "-"]):
            if (str[k] == "-"):
                temp = temp + 1
            temp = temp % 2
            k = k + 1
        if (str[k:].islower()):
            return 0

        if (temp == 0):
            temp = int(str[k:])
        else:
            temp = int("-" + str[k:])
    else:
        if (len(str) == 0 or str == "+" or str == "-"):
            temp = 0
        else:
            temp = int(str)
    return temp

print myAtoi(" ++--1")