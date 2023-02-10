from typing import List
import copy

def convert_txt_to_list(file_name: str) -> List[List[str]]:
    list_of_lists = []
    with open(file_name) as f:
        line = f.readline()
        while line != '':
            right_side = line.split('->')[1].replace(' ', '').replace('\n', '').split(',')
            left_side = line.split('->')[0].replace(' ', '').replace('\n', '')
            list_of_lists.append([left_side, right_side])
            line = f.readline()
    return list_of_lists


def FermTransAttr(F: List[List[str]], A: List[str]) -> List[str]:
    if F == [[]]:
        return
    Aplus = list(A)
    Atmp = -1
    while Aplus != Atmp:
        Atmp = list(Aplus)
        for X, Y in F:
            if all(item in Aplus for item in X):
                for y in Y:
                    if y not in Aplus:
                        Aplus.append(y)
    return Aplus


def CouvMinDF(F: List[List[str]]) -> List[List[str]]:
    C = []

    for X, Y in F:
        for y in Y:
            C.append([X, [y]])

    i = 0
    while i < len(C):
        current_line = C[i]
        Ctmp = copy.deepcopy(C)
        del Ctmp[i]
        if all(item in FermTransAttr(Ctmp, current_line[0]) for item in current_line[1]):
            del C[i]
            i -= 1
        i += 1

    i = 0
    while i < len(C):
        lst_key = C[i][0]
        for key in lst_key:
            values_to_test = list(lst_key)
            values_to_test.remove(key)

            Ctmp = copy.deepcopy(C)
            del Ctmp[i]

            if key in FermTransAttr(Ctmp, values_to_test):
                C[i][0] = values_to_test
                i -= 1
                break
        i += 1
    return C

def DecompoDFen3FN(F: List[List[str]], A: List[str]) -> List[List[str]]:
    C = CouvMinDF(F)
    i = 0
    while i < len(C):
        j = i + 1
        while j < len(C):
            if C[i][0] == C[j][0] and C[i][1] != C[j][1]:
                #Ajouter X → YZ à C
                C.append([C[i][0], C[i][1] + C[j][1]])
                #Supprimer X → Y et X → Z de C
                del C[j]
                del C[i]
                i -= 1
                break
            j += 1
        i += 1
    # // 2. traitement des attributs isolés
    B = A
    # // ajout des attributs de F
    for X, Y in F:
        for x in X:
            if x not in B:
                B.append(x)
        for y in Y:
            if y not in B:
                B.append(y)
    # // suppression des attributs de C
    for X, Y in C:
        for x in X:
            if x in B:
                B.remove(x)
        for y in Y:
            if y in B:
                B.remove(y)
    S = []
    #  // création d'autant de relations que d'attributs isolés
    for b in B:
        S.append([[b], [b]])

    #   // ajout d'autant de relations que de dépendances fonctionnelles
    for X, Y in C:
        S.append([X, Y])
    return S




def _display(F: List[List[str]]) -> None:
    for X, Y in F:
        for x in X:
            print(x, end='')
        print(" -> ", end='')
        for y in Y:
            print(y, end='')
        print()

def _display_decomposition(F: List[List[str]]) -> None:
    for X, Y in F:
        for x in X:
            print(x, end='')
        print("(", end='')
        for x in X:
            print(x, end='')
        for y in Y:
            if y not in X:
                print(", ", end='')
                print(y, end='')
        print(") de clé (", end='')
        for x in X:
            print(x, end='')
        print(")")




print(convert_txt_to_list('HTS+_simplif.txt'))
print("====== CouvMinDF ======")
_display_decomposition(DecompoDFen3FN(convert_txt_to_list('HTS+_simplif.txt'),['a','c','e']))