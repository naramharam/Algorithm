def toWeirdCase(s):
    def change(t):
        result = ""
        for i, v in enumerate(t):
            if i % 2:  
                result += v.lower()
            else:  
                result += v.upper()
        return result
    return ' '.join(list(map(change, s.split())))


print("결과 : {}".format(toWeirdCase("try hello world")))
