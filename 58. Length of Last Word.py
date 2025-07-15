def lengthOfLastWord(self, s: str) -> int:
    res= 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ' ' and res == 0:  # пробел, но слово еще не началось -> пропускаем
                continue
        elif s[i] == ' ' and res > 0:  # пробел, но слово уже началось -> конец слова
                return res
        res += 1
    return res