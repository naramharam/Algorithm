def hide_numbers(s):
    return "*" * (len(s) - 4) + s[-4:]


hide_numbers("결과 : " + hide_numbers('01033334444'))
hide_numbers("결과 : " + hide_numbers('027778888'))
