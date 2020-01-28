def function(file_name):
    with open("C:\\Users\\Admin\\Downloads\\" + file_name + ".txt", "r") as file:
        R = file.readline()
        s = file.read().strip().split()
        s = "".join(s)
        #         print(s)

        intab = b"ACGT"
        outtab = b"TGCA"
        t = s.translate(bytes.maketrans(intab, outtab))[::-1]
        #         print(t)

        dna_list = [s, t]
        #         print(dna_list)

        dna_dict = {"TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
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

        protein_orf = set()
        #         print(protein_orf)
        for dna in dna_list:
            for i in range(len(dna) - 2):

                if dna[i:i + 3] == 'ATG':

                    j = i
                    current_protein = ''

                    while j + 3 < len(dna) - 1:
                        if dna_dict[dna[j:j + 3]] == '':
                            protein_orf.add(current_protein)
                            break
                        else:
                            current_protein += dna_dict[dna[j:j + 3]]
                        j += 3

        for el in protein_orf:
            print(el)


(function("rosalind_orf"))