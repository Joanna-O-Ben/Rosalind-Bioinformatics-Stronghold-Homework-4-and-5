import re
from more_itertools import sliced


def function(file_name):
    with open("C:\\Users\\Admin\\Downloads\\" + file_name + ".txt", "r") as file:
        str1 = file.read()
        str1 = str1.replace("Rosalind_", "").replace("\n", "")
        str1 = ''.join([i for i in str1 if not i.isdigit()])
        mat = str1.split(">")
        mat.remove("")
        #         print(mat)

        dna = mat[0]
        #         print(dna, len(dna))

        introns = mat[1:]
        #         print(introns)

        #         c = 0
        for i in introns:
            if i in dna:
                #                 c += 1
                dna = re.sub(i, "", dna)

        #             print(dna, len(dna), c, "i =", i)

        s1 = list(sliced(dna, 3))
        #         print(s1, len(s1))

        d = {"TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
             "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
             "TAT": "Y", "TAC": "Y", "TAA": "", "TAG": "",
             "TGT": "C", "TGC": "C", "TGA": "", "TGG": "W",
             "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
             "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
             "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
             "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
             "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
             "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
             "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
             "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
             "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
             "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
             "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
             "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

        l = []
        for obj in s1:

            if obj in list(d.keys()):
                l.append(d[obj])

        #         print(l)
        l1 = "".join(l)

        return (l1)


print(function("rosalind_splc"))