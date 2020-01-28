def function(file_name):
    with open("C:\\Users\\Admin\\Downloads\\" + file_name + ".txt", "r") as file:
        str1 = file.read()
        str1 = str1.replace("Rosalind_", "").replace("\n", "")
        str1 = ''.join([i for i in str1 if not i.isdigit()])
        mat = str1.split(">")
        mat.remove("")
        #         print(mat)

        s = mat[0]
        t = mat[1]

        currentbase = -1
        subseqindex = []

        for base in t:
            currentbase += s.index(base) + 2
            subseqindex.append(currentbase)

            s = s[s.index(base) + 2::]

        print(' '.join(map(str, subseqindex)))


(function("rosalind_sseq"))