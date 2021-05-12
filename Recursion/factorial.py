def find_factorial(n):
    assert n>=0 and int(n)==n,"The entered input is not as expected"
    if n in [0,1]:
        return 1
    else:
        return n*find_factorial(n-1)

print(find_factorial(15))