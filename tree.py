def function(file_name):
    with open("C:\\Users\\Admin\\Downloads\\" + file_name + ".txt", "r") as file:
        str1 = ' '
        mat = []
        while (str1 != ''):
            str1 = file.readline().strip()
            #             print(str1)
            mat.append(str1)
        mat.remove('')
        #         print(mat)
        #         print(len(mat))

        n = int(mat[0])
        #         print(n)

        edge = n - len(mat)
        print(edge)


(function("rosalind_tree"))