def rm_small(mylist):
    mylist.remove(min(mylist))

    return mylist


my_list = [4, 3, 2, 1]
print("결과 {} ".format(rm_small(my_list)))
