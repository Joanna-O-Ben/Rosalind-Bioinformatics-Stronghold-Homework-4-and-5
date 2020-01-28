import itertools

def lexigraph(x, l):
    y = sorted(x)
    #     print(x, y)
    perms = itertools.product(y, repeat=l)
    #     print(perms)
    for i in perms:
        print(''.join(i))
    return ('')

def function(file_name):
    with open("C:\\Users\\Admin\\Downloads\\" + file_name + ".txt", "r") as file:
        s = file.readline().strip().split(" ")
        s = "".join(s)
        #         print(s)
        n = int(file.readline())
        #         print(n)
        return lexigraph(s, n)


print(function("rosalind_lexf"))