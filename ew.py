from sys import prefix
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=strs[0]
        for word in strs:
            for i in range(len(prefix)):
                if i>len(word)-1 or i>len(prefix)-1 or prefix[i]!=word[i]:
                    prefix=prefix[0:i]
        return prefix


print(Solution.longestCommonPrefix(Solution(), strs=["flower","flow","flight"]))