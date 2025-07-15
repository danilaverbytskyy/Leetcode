def convertToTitle(columnNumber: int) -> str:
    d = {i - 64: chr(i) for i in range(65, 91)}
    result=''
    while columnNumber>0:
        columnNumber-=1
        result += d[columnNumber%26+1]
        columnNumber//=26
    return result[::-1]

print(convertToTitle(28))