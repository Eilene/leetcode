class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        size = len(nums)
        result = [0,0]
        flag = False
        for i in range(size):
            for j in range(i+1,size):
                if(nums[i]+nums[j] == target):
                    result[0] = i
                    result[1] = j
                    flag = True
                    break
            if(flag == True):
                break
        return result



if __name__ == "main":
    test = Solution()
    test.twoSum()