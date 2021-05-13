def palin_check(strng):
    assert str(strng) == strng , "the input should be of string type"
    if len(strng) == 0:
        return True
    else:
        return strng[0] == strng[len(strng)-1]
        palin_check(strng[1:-1])

print(palin_check('tot'))