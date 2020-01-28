import itertools


def rev_palindrome(s):
    d = {}
    gene = 'x'
    str1 = ''
    for line in s:
        if line[0] == '>':
            d.update({gene: str1})
            gene = line[1:]
            str1 = ''
        else:
            str1 += line
    d.update({gene: str1})
    d.pop('x')
    DNAx = list(d.values())
    DNA = ''.join(DNAx)
    DNAy = []
    for o in DNAx:
        for oo in o:
            DNAy.append(oo)
    minL = 4
    maxL = 12
    substr = []
    resubstr = []
    for j in range(minL, maxL + 1):
        for jj in range(0, len(DNAy) - j + 1):
            sub = DNAy[jj:jj + j]
            subsPos = jj + 1
            substr.append([''.join(sub), subsPos, len(sub)])
            resubstr.append(sub)
    l2 = [''.join(g) for g in resubstr]
    l3 = [gg.replace('T', 'a').replace('A', 't').replace('C', 'g').replace('G', 'c').upper()[::-1] for gg in l2]
    lfin = []
    for k in range(len(l2)):
        if l2[k] == l3[k]:
            lfin.append(l2[k])
    fin2 = []
    for p in lfin:
        for u in substr:
            if p in u:
                fin2.append(u)
    for uu in fin2:
        if fin2.count(uu) > 1:
            fin2.remove(uu)
    fin3 = []
    for v in fin2:
        fin3.append(v[1:])
    fin = sorted(fin3)
    FIN = list(fin for fin, _ in itertools.groupby(fin))
    for f in FIN:
        print(*f)
    return ('')


def function(file_name):
    with open("C:\\Users\\Admin\\Downloads\\" + file_name + ".txt", "r") as file:
        s = file.read().split()
        #         print(s)

        return rev_palindrome(s)


print(function("rosalind_revp"))