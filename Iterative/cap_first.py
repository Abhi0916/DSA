def cap_first(arr):
    new_arr = []
    for item in arr:
        new_arr.append(item.capitalize())
    return new_arr

print(cap_first(["hello","world","namaste"]))