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

        ssm = [''] * (len(t) + 1)
        for i in s:
            last = ssm
            ssm = ['']
            for j, k in enumerate(t):
                if (i == k):
                    ssm.append(last[j] + i)
                else:
                    ssm.append(max(last[j + 1], ssm[-1], key=len))
        print(ssm[-1])


(function("rosalind_lcsq"))