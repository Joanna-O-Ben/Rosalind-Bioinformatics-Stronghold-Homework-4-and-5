def tran_tran(s, t):
    transition = 0
    transversion = 0
    for a, b in zip(s, t):
        if a != b:
            if (a == "A" and b == "G") or (a == "T" and b == "C") or (a == "G" and b == "A") or (a == "C" and b == "T"):
                transition += 1
            elif (a == "A" and b == "C" or "T") or (a == "T" and b == "A" or "G") or (a == "G" and b == "C" or "T") or (
                    a == "C" and b == "A" or "G"):
                transversion += 1
    ratio = str(transition / transversion)

    return ratio[:13]


def function(file_name):
    with open("C:\\Users\\Admin\\Downloads\\" + file_name + ".txt", "r") as file:
        str1 = file.read()
        str1 = str1.replace("Rosalind_", "").replace("\n", "")
        str1 = ''.join([i for i in str1 if not i.isdigit()])
        mat = str1.split(">")
        mat.remove("")
        #         print(mat, len(mat))

        s = mat[0]
        t = mat[-1]
        #         print("s =", s)
        #         print("t =", t)

        return tran_tran(s, t)


print(function("rosalind_tran"))