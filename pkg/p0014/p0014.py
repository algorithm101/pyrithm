# coding=utf-8


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        if len(strs) == 1:
            return strs[0]

        lens = 0
        for i in range(len(strs[0])):
            c = strs[0][i]
            for s in strs:
                if i >= len(s) or c != s[i]:
                    break
            else:
                lens += 1
                continue
            break

        return strs[0][:lens]
