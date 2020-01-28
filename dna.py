def function(file_name):
    with open("C:\\Users\\Admin\\Downloads\\" + file_name + ".txt", "r") as file:
        s = file.readline()
#         print(s)
        s1 = s.count("A")
        s2 = s.count("C")
        s3 = s.count("G")
        s4 = s.count("T")
        print(s1, s2, s3, s4)

print (function("rosalind_dna"))