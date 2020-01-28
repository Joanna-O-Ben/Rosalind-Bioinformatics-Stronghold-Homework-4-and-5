def profilecount(fragmentarray, base):
    basecount = base + ":"
    for stringslice in range(len(fragmentarray[0])):
        count = 0
        for frag in fragmentarray:
            if frag[stringslice] == base:
                count += 1
        basecount += " "
        basecount += str(count)
    return basecount


def profile(fragmentarray):
    print(profilecount(fragmentarray, "A"))
    print(profilecount(fragmentarray, "C"))
    print(profilecount(fragmentarray, "G"))
    print(profilecount(fragmentarray, "T"))


def consensuscount(fragmentarray, position):
    basecount = [0, 0, 0, 0]
    for frag in fragmentarray:
        if frag[position] == "A":
            basecount[0] += 1
        if frag[position] == "C":
            basecount[1] += 1
        if frag[position] == "G":
            basecount[2] += 1
        if frag[position] == "T":
            basecount[3] += 1
    return basecount.index(max(basecount))


def consensus(fragmentarray):
    basemax = []
    #     print(fragmentarray[0])
    for i in range(len(fragmentarray[0])):
        basemax.append(consensuscount(fragmentarray, i))
    consensusstring = ""
    for base in basemax:
        if base == 0:
            consensusstring += "A"
        if base == 1:
            consensusstring += "C"
        if base == 2:
            consensusstring += "G"
        if base == 3:
            consensusstring += "T"
    print(consensusstring)


def function(file_name):
    with open("C:\\Users\\Admin\\Downloads\\" + file_name + ".txt", "r") as f:

        rawdna = ""
        for line in f:
            rawdna += line
        #         print(rawdna)

        fragments = rawdna.split(">")

        fra = []
        fragments.pop(0)
        #         print("OLD =", fragments, len(fragments))
        for string in fragments:
            s = string.replace("\n", "")
            fra.append(s)
        #         print("NEW =", fra)

        rosaid = []
        dnafrag = []

        for el in fra:
            if el[0] == "R":
                rosaid.append(el)
            else:
                dnafrag.append(el)

        #         print("R =", rosaid)
        #         print("dna =", dnafrag, len(dnafrag[0]))

        consensus(dnafrag)

        profile(dnafrag)


(function("rosalind_cons"))