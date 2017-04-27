def findMedianSortedArrays(nums1,nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    sl1 = 0
    sl2 = 0
    num = []

    while(sl1<len(nums1) and sl2 < len(nums2)):
        if(nums1[sl1]<nums2[sl2]):
            num.append(nums1[sl1])
            sl1 = sl1 +1
        else:
            num.append(nums2[sl2])
            sl2 = sl2 + 1
    if sl2 == len(nums2):
        for i in nums1[sl1:]:
            num.append(i)
    else:
        for i in nums2[sl2:]:
            num.append(i)
    print num
    temp = len(num) / 2
    if(len(num)%2==0):
        return float(num[temp-1]+num[temp])/2
    else:
        return float(num[temp])

print findMedianSortedArrays([1,2],[3,4])