from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    for i in range(len(strs[0])):
        char = strs[0][i]
        for s in strs[1:]:
            if len(s) <= i or s[i] != char:
                return strs[0][0:i]
    return strs[0]


print(longestCommonPrefix(strs=["flower", "flow", "flight"]))
