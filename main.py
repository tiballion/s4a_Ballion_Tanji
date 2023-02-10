from typing import List
import random


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
        Ctmp = C[:i] + C[i+1:]
        if all(item in FermTransAttr(Ctmp, current_line[0]) for item in current_line[1]):
            C.pop(i)
            i -= 1
        i += 1

    i = 0
    while i < len(C):
        lst_key = C[i][0]
        for key in lst_key:
            values_to_test = list(lst_key)
            values_to_test.remove(key)
            Ctmp = C[:i] + C[i+1:]
            if key in FermTransAttr(Ctmp, values_to_test):
                C[i][0] = [x for x in C[i][0] if x != key]
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


def letter_to_file(letter: str) -> None:
    # Create file
    file = open("jeu_donnée.txt", "w")
    
    # Transform letter in a list
    letter_list = list(letter.lower())

    # Iterate through each letter in the list
    for l in letter_list:
        int1 = random.randint(1, len(letter_list))
        int2 = random.randint(1, len(letter_list))
        rand_letters = []
        rand_right_letters = []
            
        # Get two random numbers and use them to choose two random letters
        for i in range(int1):
            rand_letter = random.choice(letter_list)
            rand_letters.append(rand_letter)

        for i in range(int2):
            right_letter = random.choice(letter_list)
            while right_letter in rand_letters:
                right_letter = random.choice(letter_list)
            rand_right_letters.append(right_letter)

        # Check that the same letter is not written twice
        for l in rand_right_letters:
            if l in rand_right_letters:
                rand_right_letters.remove(l)

        for l in rand_letters:
            if l in rand_letters:
                rand_letters.remove(l)

        # Check if the list are not empty
        if len(rand_letters) == 0:
            rand_letters.append(random.choice(letter_list))
        if len(rand_right_letters) == 0:
            rand_right_letters.append(random.choice(letter_list))
            
        # Write chosen letters and matching answer to file
        for l in rand_letters:
            file.write(l)
            if l != rand_letters[-1]:
                file.write(",")
        file.write(" -> ")
        for l in rand_right_letters:
            file.write(l)
            if l != rand_right_letters[-1]:
                file.write(",")
        file.write("\n")
    file.close()
    file = open("jeu_donnée.txt", "r")
    lines = file.readlines()
    for line in lines:
        line.replace(",\n", "\n")
    file.close()


def main():
    letter_to_file("TanjiBallion")

    print(convert_txt_to_list('HTS+_simplif.txt'))
    print("====== CouvMinDF ======")
    _display(CouvMinDF(convert_txt_to_list('HTS+_simplif.txt')))


if __name__ == '__main__':
    main()