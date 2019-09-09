def sumMatrix(A,B):
    answer = []

    for i in range(len(A)):
        answer.append([])
        for j in range(len(A[0])):
            answer[i].append(A[i][j] + B[i][j])

    return answer

print(sumMatrix([[1, 2], [2, 3]], [[3, 4], [5, 6]]))
