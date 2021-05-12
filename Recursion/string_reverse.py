def rev_string(strs):
    cnt = len(strs)
    assert cnt >= 1 , "please enter a valid string"
    if cnt == 1:
        return strs
    else:
        return strs[cnt-1] + rev_string(strs[:cnt-1])


print(rev_string("hello"))
print(rev_string(" "))