def get_power(num,pow):
    assert pow >= 0 and int(pow) == pow, "The entered input is not as expected"
    if pow == 0:
        return 1
    if pow == 1:
        return num
    else:
        return num*get_power(num,pow-1)

print(get_power(8,1))