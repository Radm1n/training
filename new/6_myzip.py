def myzip(*real):
    real = [list(A) for A in real]
    obraz = []
    while all(real):
        obraz.append(tuple(A.pop(0) for A in real))
    return obraz
A1 = ('kjhjlk')
A2 = ('1klj45n56')
print(myzip(A1, A2))
