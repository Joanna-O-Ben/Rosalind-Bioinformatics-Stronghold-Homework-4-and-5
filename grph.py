def function(file_name):
    with open("C:\\Users\\Admin\\Downloads\\" + file_name + ".txt", "r") as file:
        data = file.read().split(">")
        del data[0]

        k = 3
        dna = []

        for i in range(len(data)):
            dna.append("".join(data[i].splitlines()[1:]))

        for i in range(len(dna)):
            for j in range(len(dna)):
                if (i != j and dna[i][-k:] == dna[j][:k]):
                    print(data[i].splitlines()[0], data[j].splitlines()[0])


(function("rosalind_grph"))