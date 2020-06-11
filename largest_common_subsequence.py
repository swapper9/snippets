def lcs(a, b):
    """ Наибольшая общая подпоследовательность """
    f = [[0] * (len(b) + 1) for i in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                f[i][j] = 1 + f[i - 1][j - 1]
            else:
                f[i][j] = max(f[i - 1][j], f[i][j - 1])
    return f[-1][-1]


def lis(a):
    """ Наибольшая возрастающая подпоследовательность """
    f = [0] * (len(a) + 1)
    for i in range(1, len(a) + 1):
        cur_max = 0
        for j in range(0, i):
            if a[i] > a[j] and f[j] > cur_max:
                cur_max = f[j]
        f[i] = cur_max + 1
    return f[len(a)]
