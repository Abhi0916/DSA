def is_palin(strng):
    count = len(strng)
    rev_strng = ""
    while count > 0:
        rev_strng = rev_strng + strng[count-1]
        count -=1
    return rev_strng == strng

print(is_palin("tot"))
print(is_palin("awesome"))

def is_palin_index(new_word):
    return new_word == new_word[::-1]

print(is_palin_index("tot"))
print(is_palin_index("awesome"))