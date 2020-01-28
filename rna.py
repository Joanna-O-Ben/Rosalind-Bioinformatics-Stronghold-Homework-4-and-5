def function(file_name):
    with open("C:\\Users\\Admin\\Downloads\\" + file_name + ".txt", "r") as file:
        s = file.readline()
        print(s.replace("T", "U"))


print (function("rosalind_rna"))