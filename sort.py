def insert_sort(a):
    """ Сортировка вставками
    :param a: список
    """
    n = len(a)
    for top in range(1, n):
        k = top
        while k > 0 and a[k - 1] > a[k]:
            a[k], a[k - 1] = a[k - 1], a[k]
            k -= 1


def choice_sort(a):
    """ Сортировка выбором
        :param a: список
    """
    n = len(a)
    for pos in range(0, n - 1):
        for k in range(pos + 1, n):
            if a[k] < a[pos]:
                a[k], a[pos] = a[pos], a[k]


def bubble_sort(a):
    """ Сортировка пузырьком
        :param a: список
    """
    n = len(a)
    for bypass in range(1, n):
        for k in range(0, n - bypass):
            if a[k] > a[k + 1]:
                a[k], a[k + 1] = a[k + 1], a[k]


def hoar_sort(a):
    """ Сортировка Хоара
        :param a: список
    """
    if len(a) <= 1:
        return
    barrier = a[0]
    left = []
    right = []
    middle = []
    for x in a:
        if x < barrier:
            left.append(x)
        elif x == barrier:
            middle.append(x)
        else:
            right.append(x)
    hoar_sort(left)
    hoar_sort(right)
    k = 0
    for x in left + middle + right:
        a[k] = x
        k += 1


def merge_sort(a):
    """ Сортировка слиянием
        :param a: список
    """
    if len(a) <= 1:
        return
    middle = len(a) // 2
    left = [a[i] for i in range(0, middle)]
    right = [a[i] for i in range(middle, len(a))]
    merge_sort(left)
    merge_sort(right)
    c = merge(left, right)
    a = list(c)


def merge(a: list, b: list):
    c = [0] * (len(a) + len(b))
    i = k = n = 0
    while i < len(a) and k < len(b):
        if a[i] <= b[k]:
            c[n] = a[i]
            i += 1
            n += 1
        else:
            c[n] = b[k]
            k += 1
            n += 1
    while i < len(a):
        c[n] = a[i]
        i += 1
        n += 1
    while k < len(b):
        c[n] = b[k]
        i += 1
        n += 1
    return c


def test_sort(sort_algorithm):
    print("Sorting")
    a = [4, 2, 5, 1, 3]
    a_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(a)
    print("ok" if a == a_sorted else "not ok")
    print(a)
    print(a_sorted)
