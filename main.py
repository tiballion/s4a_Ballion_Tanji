# This function implements the process of "Ferm attic transformation". 
# The input 'F' is a set of dependency pairs, where each pair is composed of two sets. 
# The function finds the closure of a given set 'A' under the dependencies in 'F'.
# The closure is the smallest set that contains all elements in 'A' and is closed under the dependencies in 'F'.

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

# This function implements the process of "Covering minimal dependency set".
# The input 'F' is a set of dependency pairs, where each pair is composed of two sets.
# The function returns a covering minimal dependency set of 'F'.

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

# This function implements the process of "Decomposition of a functional dependency set".
# The input 'F' is a set of dependency pairs, where each pair is composed of two sets.
# The function returns a set of pairs, where each pair is composed of a set and a list.

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
        S.append((X, list(Y)))
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


# transform_file is a function that transforms a text file into a set of pairs.
# The input 'txt_file' is a text file.
# The function returns a set of pairs, where each pair is composed of two sets.

def transform_file(txt_file):
    with open(txt_file, 'r') as f:
        lines = f.readlines()
    F = []
    for line in lines:
        line = line.split('->')
        x_element = line[0].split(',')
        y_element = line[1].split(',')
        for i in range(len(x_element)):
            x_element[i] = x_element[i].strip()
        for i in range(len(y_element)):
            y_element[i] = y_element[i].strip()
        F.append((set(x_element), set(y_element)))
    return F

# display is a function that displays the result of the function FermTransAttr and CouvMinDF
# The input 'F' is a set of pairs, where each pair is composed of two sets.

def display(F):
    for f in F:
        print(f[0], '->', f[1])

# display_DecompDFen3FN is a function that displays the result of the function DecompoDFen3FN
# The input 'F' is a set of pairs, where each pair is composed of a set and a list.

def display_DecompoDFen3FN(F):
    for f in F:
        print('(', end='')
        for i in range(len(f[1])):
            print(f[1][i], end='')
            if i != len(f[1]) - 1:
                print(',', end='')
        print(') a pour attribut', f[0])



