def cap_first(arr):
    op_arr = []
    if len(arr) == 0:
        return arr
    else:
        op_arr.append(arr[0][0].upper()+arr[0][1:])
        return op_arr + cap_first(arr[1:])

print(cap_first(['hello','wassup','null']))