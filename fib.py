def fib(n, k):
    f1 = 1
    f2 = 1
    if n <= 2:
        return 1
    while n > 2:
        g = (f1 * k) + f2
        f1 = f2
        f2 = g
        n -= 1
    return f2


def function(file_name):
    with open("C:\\Users\\Admin\\Downloads\\" + file_name + ".txt", "r") as file:
        s = file.readline().split()
        n = int(s[0])
        k = int(s[-1])

        return fib(n, k)


print (function("rosalind_fib"))