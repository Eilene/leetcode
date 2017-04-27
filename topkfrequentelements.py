def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    dict = {}
    for i in nums:
        if(i in dict):
            dict[i] = dict[i]+1
        else:
            dict[i] =1
    dict =  sorted(dict.iteritems(),key = lambda asd:asd[1],reverse=True)
    temp = []
    for i in range(k):
        temp.append(dict[i][0])
    return temp
topKFrequent([1,1,1,2,2,3],2)

