"""
steps to convert
1.divide the number by 2
2.get the quotient and save it for next execution
3.save the remainder as bin digit """

def dec_to_bin2(n):
    assert int(n) == n, "The number must be integer type"
    if n == 0:
        return 0
    else:
        return n % 2 + 10*dec_to_bin2(int(n/2))

print(dec_to_bin2(245))