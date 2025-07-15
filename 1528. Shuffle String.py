# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"
# Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
# Example 2:
#
# Input: s = "abc", indices = [0,1,2]
# Output: "abc"
# Explanation: After shuffling, each character remains in its position.
from typing import List


def restoreString(self, s: str, indices: List[int]) -> str:
    res = [''] * len(s)
    for i in range(len(s)):
        res[indices[i]] = s[i]
    return ''.join(res)