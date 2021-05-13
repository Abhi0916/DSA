def revr_string(word):
    count = len(word)
    new_str = ""
    while count > 0:
        new_str = new_str + word[count - 1]
        count -= 1
    return new_str

print(revr_string("namaste"))