def romanToInt(s: str) -> int:
    mydict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 
              'C': 100, 'D': 500, 'M': 1000}
    total = 0
    i = 0
    while i < len(s):
        # Проверяем пару символов (текущий и следующий)
        if i + 1 < len(s) and mydict[s[i]] < mydict[s[i+1]]:
            total += mydict[s[i+1]] - mydict[s[i]]
            i += 2  # Пропускаем обработанную пару
        else:
            total += mydict[s[i]]
            i += 1  # Переходим к следующему символу
    return total

print(romanToInt('MCMXCIV'))  # Вернёт 1994 (корректно)