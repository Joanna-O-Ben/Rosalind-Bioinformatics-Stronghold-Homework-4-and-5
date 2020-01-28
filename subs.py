def function(file_name):
    with open("C:\\Users\\Admin\\Downloads\\" + file_name + ".txt", "r") as file:

        f = file.read().split("\n")

        s = f[0]
        t = f[1]

        l = []
        for i in range(len(s)):
            if s[i:i + len(t)] == t:
                l.append(i + 1)
        print(*l)


print (function("rosalind_subs"))