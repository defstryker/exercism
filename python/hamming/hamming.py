def distance(a, b):
    fin = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            fin += 1
    return fin
