def FermTransAttr(F, A):
    A_plus = set(A)
    while True:
        A_plus_tmp = set(A_plus)
        for X, Y in F:
            if X.issubset(A_plus):
                A_plus |= Y
        if A_plus == A_plus_tmp:
            break
    return A_plus


def CouvMinDF(F):
    C = []
    for X, Y in F:
        for y in Y:
            C.append((X, {y}))
    C_temp = C.copy()
    for f in list(C):
        X, Y = f
        C_temp.remove(f)
        for y in list(Y):
            if y in FermTransAttr(C_temp, X):
                Y.remove(y)
    for f in list(C):
        X, Y = f
        if len(Y) == 0:
            C.remove(f)
    return C


def DecompoDFen3FN(F, A):
    C = CouvMinDF(F)
    for i, f1 in enumerate(C):
        for j, f2 in enumerate(C):
            if i == j:
                continue
            X1, Y1 = f1
            X2, Y2 = f2
            if X1 == X2 and Y1 != Y2:
                C.remove(f1)
                C.remove(f2)
                C.append((X1, Y1.union(Y2)))
                break
    B = A.copy()
    for f in F:
        B = B.union(set(f[0]).union(set(f[1])))
    for f in C:
        B = B.difference(set(f[0]).union(set(f[1])))
    S = []
    for Z in B:
        S.append((Z, [Z]))
    while C:
        f = C.pop()
        X, Y = f
        S.append((X, [X] + list(Y)))
    return S


    
F = [
    (set('c'), set('a')),
    (set({'c', 'e'}), set({'b','d'})),
    (set({'a', 'b','d'}), set('b')),
    (set('d'), set('e')),
    (set({'b', 'c'}), set('d')),
]

C = [
    (set('c'), set('a')),
    (set({'c', 'e'}), set({'d'})),
    (set({'c','d'}), set('b')),
    (set({'d'}), set('e')),
    (set({'b', 'c'}), set('d')),
]

B = [
    (set('a'), set({'b','f'})),
    (set({'a', 'c', 'd'}), set({'b'})),
    (set({'b','g'}), set({'h'})),
]

A = {
    'a' , 'c' ,'c'
}


assert FermTransAttr(F, set()) == set()
assert FermTransAttr(F, {'b', 'e'}) == {'b', 'e'}
assert FermTransAttr(F, {'c'}) == {'a', 'c'}
assert FermTransAttr(F, {'a', 'd'}) == {'a', 'd', 'e'}
assert FermTransAttr(F, {'c', 'd'}) == {'a', 'b', 'c', 'd', 'e'}


print(DecompoDFen3FN(B,A))