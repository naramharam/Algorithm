def solution(n):
    num = list(str(n))
    num.sort(reverse=True)
    answer = " "
    for i in num:
        answer += str(i)

    return print(int(answer))


n = 45890426
solution(n)
