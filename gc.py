from collections import Counter


def function(file_name):
    with open("C:\\Users\\Admin\\Downloads\\" + file_name + ".txt", "r") as file:

        f = file.read().split(">")
        l = []
        for i in f:
            c = dict(Counter(i).most_common())

            if len(i) != 0:
                percentage = ((c.get("C") + c.get("G")) / (c.get("C") + c.get("G") + c.get("A") + c.get("T")) * 100)
                l.append(percentage)
                index = l.index(max(l))

                if len(l) == len(f) - 1:
                    print(f[index + 1][:13], max(l), sep = "\n")


print (function("rosalind_gc"))
