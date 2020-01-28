from numpy import zeros

def function(file_name):
    with open("C:\\Users\\Admin\\Downloads\\" + file_name + ".txt", "r") as file:

        str1 = file.read()
        str1 = str1.replace("Rosalind_", "").replace("\n", "")
        str1 = ''.join([i for i in str1 if not i.isdigit()])
        dna_list = str1.split(">")
        dna_list.remove("")

        dna_len = len(dna_list[0])
        #         print(dna_len)

        M = zeros((len(dna_list), len(dna_list))) * 0.001
        #         print(M, type(M))

        for i in range(len(dna_list)):
            for j in range(len(dna_list)):

                if i < j:
                    for k in range(dna_len):
                        if dna_list[i][k] != dna_list[j][k]:
                            M[i][j] += 1.0 / dna_len

                elif i > j:
                    M[i][j] = M[j][i]

        for l in M:
            print(*l)

(function("rosalind_pdst"))