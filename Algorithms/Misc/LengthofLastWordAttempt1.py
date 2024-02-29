def lengthOfLastWord(s: str) -> int:

    idx_beginning = [i for i in range(len(s)-1, -1, -1) if s[i] != ' '][0]
    
    idx_end = [i for i in range(idx_beginning, -1, -1) if s[i] == ' '][0]

    if idx_end < 0:
        idx_end = 0

    return idx_beginning - idx_end







print(lengthOfLastWord('What is that sound   '))



