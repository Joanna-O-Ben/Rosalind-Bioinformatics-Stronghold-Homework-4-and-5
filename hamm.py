def hamming_distance(s, t):
    value = 0

    for a, b in zip(s, t):
        if a != b:
            value += 1

    return value


def function(file_name):
    with open("C:\\Users\\Admin\\Downloads\\" + file_name + ".txt", "r") as file:
        s = file.readline()
        t = file.readline()

        #         print("s =", s)
        #         print("t =", t)

        return hamming_distance(s, t)


print(function("rosalind_hamm"))