def shared_motif(s):
    D = {}
    gene = 'x'
    str1 = ''
    for line in s:
        if line[0] == '>':
            D.update({gene: str1})
            gene = line[1:]
            str1 = ''
        else:
            str1 += line
#     print(D)
    D.update({gene: str1})
#     print(D)
    D.pop('x')
#     print(D)
    seq = list(D.values())
#     print("seq =", seq)
    l = ""
    if len(seq) > 1 and len(seq[0]) > 0:
        for i in range(len(seq[0])):
            for j in range(len(seq[0]) - i + 1):
                if j > len(l) and all(seq[0][i:i+j] in y for y in seq):
                    l = seq[0][i:i+j]
    return(l)

def function(file_name):
    with open("C:\\Users\\Admin\\Downloads\\" + file_name + ".txt", "r") as file:

        s = file.read().split()
#         print(s)

        return shared_motif(s)

print(function("rosalind_lcsm"))