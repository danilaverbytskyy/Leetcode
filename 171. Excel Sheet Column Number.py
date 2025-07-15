def convertToTitle(columnTitle: str) -> int:
    d = {chr(i): i - 64 for i in range(65, 91)}
    index = len(columnTitle)-1
    rez = 0
    for i in columnTitle:
        rez += d[i] * 26**index
        index-=1
    return rez

print(convertToTitle('AB'))