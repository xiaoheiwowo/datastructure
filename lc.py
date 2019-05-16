t = ["flower","flow","floght"]
# hhhhh
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        length = len(strs)
        if length == 0:
            return ''
        elif length == 1:
            return strs[0]      
        else:
            for i in strs:
                if len(i) == 0:
                    return ''
            max_len = 0
            for p in range(len(strs[0])):
                for i in range(length - 1):
                    try:
                        if strs[i][p] != strs[i + 1][p]:
                            return strs[0][:max_len]
                    except:
                        return strs[0][:max_len]
                max_len += 1 
            return strs[0]


    def s2(self, strs):
        l_str = ''
        for i in list(zip(*[list(i) for i in strs])):
            if len(set(i)) == 1:
                l_str += i[0]
            else:
                break
        return l_str



s = Solution()
# print(s.longestCommonPrefix(t))
# print(s.longestCommonPrefix([]))
# print(s.longestCommonPrefix(['a']))
# print(s.longestCommonPrefix(['c','c']))
# print(s.longestCommonPrefix(['a','c']))

print(s.s2(t))
print(s.s2([]))
print(s.s2(['a']))
print(s.s2(['c','c']))
print(s.s2(['a','c']))
