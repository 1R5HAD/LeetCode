class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        pre=strs[0]
        for word in strs[1:]:
            prefix=""
            for j in range(min(len(pre),len(word))):
                if pre[j]==word[j]:
                    prefix+=word[j]
                else:
                    break
            pre=prefix
            if pre=="":
                return ""

        return pre