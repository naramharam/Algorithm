def numPY(s):
    s = s.lower()
    plist = []
    ylist = []

    for i in s:
        if i == 'p':
            plist.append(i)
        elif i == 'y':
            ylist.append(i)

    if len(plist) == len(ylist):
        return True
    if len(plist) == 0 and len(ylist) == 0:
        return True
        
    return False


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(numPY("pPoooyY"))
print(numPY("Pyy"))
