def longestCommonPrefix(strs: list[str]) -> str:
        
    lcp = ""

    for i in range(len(strs[0])):
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                return lcp

        lcp += strs[0][i]
        
    return lcp