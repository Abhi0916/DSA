def sum_int(n):
    assert n >= 0 and int(n) == n, "The entered input is not as expected"
    if n in [0, 1]:
        return n
    else:
        return n + sum_int(n-1)

def sum_of_digits(n):
    """f(n) = n%10 + f(n/10)"""
    assert n >= 0 and int(n) == n, "The entered input is not as expected"
    if n == 0:
        return 0
    else:
        return int(n%10)+sumOfDigits(int(n/10))

print(sum_int(10))
print(sum_of_digits(10))