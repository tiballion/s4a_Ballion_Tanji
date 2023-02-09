from typing import List, Set, Tuple

# This function implements the process of "Ferm attic transformation". 
# The input 'F' is a set of dependency pairs, where each pair is composed of two sets. 
# The function finds the closure of a given set 'A' under the dependencies in 'F'.
# The closure is the smallest set that contains all elements in 'A' and is closed under the dependencies in 'F'.

def ferm_trans_attr(F : dict, A : dict) -> dict:
    A_plus = set(A)
    while True:
        A_plus_tmp = set(A_plus)
        for X, Y in F.items():
            if set(X).issubset(A_plus):
                A_plus |= set(Y)
        if A_plus == A_plus_tmp:
            break
    return A_plus


# This function implements the process of "Covering minimal dependency set".

def couv_min_df(F: dict) -> dict:
    #   1. décomposition des membres droits des dépendances fonctionnelles
    C = {}
    for X, Y in F.items():
        for y in Y:
            if X not in C:
                C[X] = {y}
    # 2. élimination des dépendances fonctionnelles qui ne modifent pas sa fermeture
    to_remove = []
    for f in C.items():
        # C_tmp is a copy of C without f
        C_tmp = C.copy()
        del C_tmp[f[0]]
        if ferm_trans_attr(C_tmp,X) == f :
            to_remove.append(f[0])
    for f in to_remove:
        del C[f]
    # 3. réduction des membres gauches des dépendances fonctionnelles
    for X, Y in C.items():
        if len(X) == 1:
            # X' = X
            X_prime = X
            # Pour chaque X'' ∈ C tel que X' ⊆ X'' faire
            for X_prime_prime, Y_prime_prime in C.items():
                if set(X_prime[0]).issubset(set(Y_prime_prime[0])):
                    # C ← C \ {(X'', Y'')}
                    del C[X_prime_prime]
                    # C ← C ∪ {(X' ∪ X'', Y' ∪ Y'')}
                    C[X_prime.union(X_prime_prime)] = Y.union(Y_prime_prime)
    return C    


# This function implements the process of "Decomposition of a functional dependency set".
# The input 'F' is a set of dependency pairs, where each pair is composed of two sets.
# The function returns a set of pairs, where each pair is composed of a set and a list.

def DecompoDFen3FN(F, A):
    # 1. Constitution d'une couverture minimale de F, et utilisation de la propriété d'union
    C = couv_min_df(F)
    for X_to_Y, X_to_Z in [(X_to_Y, X_to_Z) for X_to_Y in C for X_to_Z in C if X_to_Y[0] == X_to_Z[0] and X_to_Y[1] != X_to_Z[1]]:
        C.remove(X_to_Y)
        C.remove(X_to_Z)
        C.append((X_to_Y[0], X_to_Y[1].union(X_to_Z[1])))

    # 2. Traitement des attributs isolés
    B = set(A)
    for X, Y in F:
        B.difference_update(X + Y)
    for X, Y in C:
        B.difference_update(X + Y)

    S = []
    S.append((B, B, B))

    # 3. Création des relations
    while C:
        X_to_Y = C.pop()
        S.append((X_to_Y[0], X_to_Y[0] + Y, X_to_Y[0]))

    return S


# transform_file is a function that transforms a text file into a set of pairs.
# The input 'txt_file' is a text file.
# The function returns a set of pairs, where each pair is composed of two sets.

def transform_file(txt_file):
    with open(txt_file, 'r') as f:
        lines = f.readlines()
    F = {}
    for line in lines:
        line = line.split('->')
        x_element = line[0].split(',')
        y_element = line[1].split(',')
        for i in range(len(x_element)):
            x_element[i] = x_element[i].strip()
        for i in range(len(y_element)):
            y_element[i] = y_element[i].strip()
        F[tuple(x_element)] = tuple(y_element)
    return F

# display is a function that displays the result of the function FermTransAttr and CouvMinDF
# The input 'F' is a set of pairs, where each pair is composed of two sets.

def display(F: dict):
    for X, Y in F.items():
        print( X, '->', Y)

# display_DecompDFen3FN is a function that displays the result of the function DecompoDFen3FN
# The input 'F' is a set of pairs, where each pair is composed of a set and a list.

def display_DecompoDFen3FN(F):
    for f in F:
        print('R (', end='')
        for i in f[0]:
            print(i, end='')
        print(') de clé ', end='')
        for i in f[0]:
            print(i, end='')
        print('\n')



print(ferm_trans_attr(transform_file('HTS+_simplif.txt'), {'d'}))
print("Couverture Minimal de F")   
display(couv_min_df(transform_file('HTS+_simplif.txt')))