def incrsubsequence(seq):
    if not seq:
        return seq

    M = [None] * len(seq)
    P = [None] * len(seq)

    L = 1
    M[0] = 0

    for i in range(1, len(seq)):
        lower = 0
        upper = L

        if seq[M[upper - 1]] < seq[i]:
            j = upper
        else:
            while upper - lower > 1:
                mid = (upper + lower) // 2
                if seq[M[mid - 1]] < seq[i]:
                    lower = mid
                else:
                    upper = mid

            j = lower

        P[i] = M[j - 1]

        if j == L or seq[i] < seq[M[j]]:
            M[j] = i
            L = max(L, j + 1)

    result = []
    pos = M[L - 1]
    for _ in range(L):
        result.append(seq[pos])
        pos = P[pos]

    return result[::-1]


def decrsubsequence(seq):
    m = [0] * len(seq)
    for x in range(len(seq) - 2, -1, -1):
        for y in range(len(seq) - 1, x, -1):
            if m[x] <= m[y] and seq[x] > seq[y]:
                m[x] = m[y] + 1

    max_value = max(m)

    result = []
    for i in range(len(m)):
        if max_value == m[i]:
            result.append(seq[i])
            max_value -= 1

    return result


def function(file_name):
    with open("C:\\Users\\Admin\\Downloads\\" + file_name + ".txt", "r") as file:
        n = int(file.readline())
        #         print(n)
        pi = file.readline().split()
        permutation = list(map(int, pi))
        #         print(pi, type(pi), permutation)

        incr = incrsubsequence(permutation)
        decr = decrsubsequence(permutation)
        print(' '.join(map(str, incr)))
        print(' '.join(map(str, decr)))


print(function("rosalind_lgis"))