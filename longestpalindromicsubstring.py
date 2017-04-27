def manacher(s):
    '''
    https://segmentfault.com/a/1190000003914228
    '''
    s='#'+'#'.join(s)+'#'
    RL=[0]*len(s)
    MaxRight=0
    pos=0
    MaxLen=0
    longstr = ""
    for i in range(len(s)):
        if i<MaxRight:
            RL[i]=min(RL[2*pos-i], MaxRight-i)
        else:
            RL[i]=1
        while i-RL[i]>=0 and i+RL[i]<len(s) and s[i-RL[i]]==s[i+RL[i]]:
            RL[i]+=1
        if RL[i]+i-1>MaxRight:
            MaxRight=RL[i]+i-1
            pos=i
        if(RL[i]>MaxLen):
            MaxLen = RL[i]
            longstr =  "".join(s[i-RL[i]+1:i+RL[i]].split("#"))
    return longstr
def test(s):
    s = '^'+'#'+'#'.join(s)+'#'+'$'
    maxlen = 0
    maxright = 0
    longstr = ""
    zhongxinpoint = 0
    r = [0]*len(s)

    for i in range(2,len(s)):
        temp = i
        j = 1
        if(i<maxright):
            j = min(r[2*zhongxinpoint-i],maxright-i)
        while(temp-j>-1 and temp+j <len(s) and s[temp-j] == s[temp+j]):
            j = j+1
        r[i] = j
        if(i+j-1>maxright):
            maxright = i+j-1
            zhongxinpoint = i
        if(j*2-1>maxlen):
            maxlen = j*2-1
            longstr = "".join(s[i-j+1:i+j].split("#"))
    return longstr


def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    if(len(s)<=1):
        return s
    temp = [([0] * len(s)) for i in range(len(s))]
    longstr = s[0]
    for i in range(0,len(s)):
        temp[i][i]=1

    for i in range(0,len(s)-1):
        if(s[i] == s[i+1]):
            temp[i][i+1] = 1
            longstr = s[i:i+2]
    for length in range(3,len(s)+1):
        for i in range(0,len(s)-length+1):
            j = i+length-1
            if(s[i]==s[j]and temp[i+1][j-1]):
                temp[i][j] = temp[i+1][j-1]
                if(length>len(longstr)):
                    longstr = s[i:j+1]
            else:
                temp[i][j] = 0
    return longstr

print test("abaa")
#print longestPalindrome("esbtzjaaijqkgmtaajpsdfiqtvxsgfvijpxrvxgfumsuprzlyvhclgkhccmcnquukivlpnjlfteljvykbddtrpmxzcrdqinsnlsteonhcegtkoszzonkwjevlasgjlcquzuhdmmkhfniozhuphcfkeobturbuoefhmtgcvhlsezvkpgfebbdbhiuwdcftenihseorykdguoqotqyscwymtjejpdzqepjkadtftzwebxwyuqwyeegwxhroaaymusddwnjkvsvrwwsmolmidoybsotaqufhepinkkxicvzrgbgsarmizugbvtzfxghkhthzpuetufqvigmyhmlsgfaaqmmlblxbqxpluhaawqkdluwfirfngbhdkjjyfsxglsnakskcbsyafqpwmwmoxjwlhjduayqyzmpkmrjhbqyhongfdxmuwaqgjkcpatgbrqdllbzodnrifvhcfvgbixbwywanivsdjnbrgskyifgvksadvgzzzuogzcukskjxbohofdimkmyqypyuexypwnjlrfpbtkqyngvxjcwvngmilgwbpcsseoywetatfjijsbcekaixvqreelnlmdonknmxerjjhvmqiztsgjkijjtcyetuygqgsikxctvpxrqtuhxreidhwcklkkjayvqdzqqapgdqaapefzjfngdvjsiiivnkfimqkkucltgavwlakcfyhnpgmqxgfyjziliyqhugphhjtlllgtlcsibfdktzhcfuallqlonbsgyyvvyarvaxmchtyrtkgekkmhejwvsuumhcfcyncgeqtltfmhtlsfswaqpmwpjwgvksvazhwyrzwhyjjdbphhjcmurdcgtbvpkhbkpirhysrpcrntetacyfvgjivhaxgpqhbjahruuejdmaghoaquhiafjqaionbrjbjksxaezosxqmncejjptcksnoq")
#print manacher("esbtzjaaijqkgmtaajpsdfiqtvxsgfvijpxrvxgfumsuprzlyvhclgkhccmcnquukivlpnjlfteljvykbddtrpmxzcrdqinsnlsteonhcegtkoszzonkwjevlasgjlcquzuhdmmkhfniozhuphcfkeobturbuoefhmtgcvhlsezvkpgfebbdbhiuwdcftenihseorykdguoqotqyscwymtjejpdzqepjkadtftzwebxwyuqwyeegwxhroaaymusddwnjkvsvrwwsmolmidoybsotaqufhepinkkxicvzrgbgsarmizugbvtzfxghkhthzpuetufqvigmyhmlsgfaaqmmlblxbqxpluhaawqkdluwfirfngbhdkjjyfsxglsnakskcbsyafqpwmwmoxjwlhjduayqyzmpkmrjhbqyhongfdxmuwaqgjkcpatgbrqdllbzodnrifvhcfvgbixbwywanivsdjnbrgskyifgvksadvgzzzuogzcukskjxbohofdimkmyqypyuexypwnjlrfpbtkqyngvxjcwvngmilgwbpcsseoywetatfjijsbcekaixvqreelnlmdonknmxerjjhvmqiztsgjkijjtcyetuygqgsikxctvpxrqtuhxreidhwcklkkjayvqdzqqapgdqaapefzjfngdvjsiiivnkfimqkkucltgavwlakcfyhnpgmqxgfyjziliyqhugphhjtlllgtlcsibfdktzhcfuallqlonbsgyyvvyarvaxmchtyrtkgekkmhejwvsuumhcfcyncgeqtltfmhtlsfswaqpmwpjwgvksvazhwyrzwhyjjdbphhjcmurdcgtbvpkhbkpirhysrpcrntetacyfvgjivhaxgpqhbjahruuejdmaghoaquhiafjqaionbrjbjksxaezosxqmncejjptcksnoq")
