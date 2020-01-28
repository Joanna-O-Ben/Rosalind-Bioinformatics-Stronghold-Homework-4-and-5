def function(file_name):
    with open("C:\\Users\\Admin\\Downloads\\" + file_name + ".txt", "r") as file:
        n = int(file.read())
        return n - 2

print(function("rosalind_inod"))