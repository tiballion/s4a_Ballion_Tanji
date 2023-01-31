
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

F = [
    (set('c'), set('a')),
    (set({'c', 'e'}), set({'b','d'})),
    (set({'a', 'b','d'}), set('b')),
    (set('d'), set('e')),
    (set({'b', 'c'}), set('d')),
]

assert FermTransAttr(F, set()) == set()
assert FermTransAttr(F, {'b', 'e'}) == {'b', 'e'}
assert FermTransAttr(F, {'c'}) == {'a', 'c'}
assert FermTransAttr(F, {'a', 'd'}) == {'a', 'd', 'e'}
assert FermTransAttr(F, {'c', 'd'}) == {'a', 'b', 'c', 'd', 'e'}
