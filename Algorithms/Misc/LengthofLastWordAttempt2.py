def lengthOfLastWord(self, s: str) -> int:

    s = s.strip()

    l_word = s[s.rfind(' ') + 1:]

    return len(l_word)