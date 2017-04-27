class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        end = 0
        countstr = {}
        if(len(s)>1):
            countstr[s[end]] = 1
            length = 0
            while end< (len(s)-1):
                while end< (len(s)-1) and countstr[s[end]]<=1:
                    end = end  +1
                    if(s[end] not in countstr):
                        countstr[s[end]] = 1
                    else:
                        countstr[s[end]] = countstr[s[end]]+1

                templength = len(s[start:end])
                if(end == (len(s)-1) and countstr[s[end]]<=1):
                    templength = templength+1


                if(templength > length):
                    length = templength

                countstr[s[start]] = countstr[s[start]] - 1
                while(countstr[s[end]]>1):
                    start = start +1
                    countstr[s[start]] = countstr[s[start]] - 1
                start = start +1
            return length
        else:
            return len(s)




