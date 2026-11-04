class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        first = strs[0]
        for i, char in enumerate(first):
            for str in strs[1:]:
                if i == len(str) or str[i] != char:
                    return first[:i]
        
        return first