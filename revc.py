def function(file_name):
    with open("C:\\Users\\Admin\\Downloads\\" + file_name + ".txt", "r") as file:
        s = file.readline()

        intab = b"ACGT"
        outtab = b"TGCA"
        print (s.translate(bytes.maketrans(intab, outtab))[::-1])


print (function("rosalind_revc"))