def combination(s):
    if len(s) < 2:
        return s
    res = []
    for i, c in enumerate(s):
        res.append(c)
        for j in combination(s[:i] + s[i+1:]):
            res.append(c + j)
    return res


if __name__ == '__main__':
    result = combination("abc")
    print(result)