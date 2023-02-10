from typing import List
import random


def convert_txt_to_list(file_name: str) -> List[List[str]]:
    """Convert a txt file to a list of lists
    :param file_name: The name of the file to convert
    :return: A list of lists of strings
    """
    list_of_lists = []
    # Open the file in read only mode
    with open(file_name) as f:
        line = f.readline()
        while line != '':
            # Remove spaces and new lines
            right_side = line.split('->')[1].replace(' ', '').replace('\n', '').split(',')
            left_side = line.split('->')[0].replace(' ', '').replace('\n', '')
            # Add the list to the list of lists
            list_of_lists.append([left_side, right_side])
            line = f.readline()
    return list_of_lists


def FermTransAttr(F: List[List[str]], A: List[str]) -> List[str]:
    """
    Compute the closure of a set of attributes under a set of functional dependencies.
    :param F: A list of functional dependencies
    :param A: A list of attributes
    :return: A list of strings representing the closure of attributes under a set of functional dependencies.
    """
    a_plus = list(A)
    a_tmp = -1
    while a_plus != a_tmp:
        a_tmp = list(a_plus)
        for X, Y in F:
            if all(item in a_plus for item in X):
                for y in Y:
                    if y not in a_plus:
                        a_plus.append(y)
    return a_plus


def CouvMinDF(F: List[List[str]]) -> List[List[str]]:
    """
    Compute the minimal cover of a set of functional dependencies.
    :param F: A list of functional dependencies
    :return: A list of functional dependencies representing the minimal cover of a set of functional dependencies.
    """

    # Create C by making each element of Y its own sublist in C
    C = []
    for X, Y in F:
        for y in Y:
            C.append([X, [y]])
    
    # Remove sublists if all elements in the second element are in FermTransAttr
    i = 0
    while i < len(C):
        current_line = C[i]
        c_tmp = C[:i] + C[i+1:]
        if all(item in FermTransAttr(c_tmp, current_line[0]) for item in current_line[1]):
            C.pop(i)
            i -= 1
        i += 1
    
    # Remove elements from first element of sublists if they are in FermTransAttr
    i = 0
    while i < len(C):
        lst_key = C[i][0]
        for key in lst_key:
            values_to_test = list(lst_key)
            values_to_test.remove(key)
            c_tmp = C[:i] + C[i+1:]
            if key in FermTransAttr(c_tmp, values_to_test):
                C[i][0] = [x for x in C[i][0] if x != key]
                i -= 1
                break
        i += 1
    return C


def DecompoDFen3FN(F: List[List[str]], A: List[str]) -> List[List[str]]:
    """
    Decompose a set of functional dependencies into a set of 3NF dependencies.
    :param F: A list of functional dependencies
    :param A: A list of attributes
    :return: A list of functional dependencies representing the decomposition of a set of functional dependencies into a set of 3NF dependencies.
    """
    C = CouvMinDF(F)
    i = 0
    while i < len(C):
        j = i + 1
        while j < len(C):
            if C[i][0] == C[j][0] and C[i][1] != C[j][1]:
                C.append([C[i][0], C[i][1] + C[j][1]])
                del C[j]
                del C[i]
                i -= 1
                break
            j += 1
        i += 1
    B = A
    for X, Y in F:
        for x in X:
            if x not in B:
                B.append(x)
        for y in Y:
            if y not in B:
                B.append(y)
    for X, Y in C:
        for x in X:
            if x in B:
                B.remove(x)
        for y in Y:
            if y in B:
                B.remove(y)
    S = []
    for b in B:
        S.append([[b], [b]])
    for X, Y in C:
        S.append([X, Y])
    return S


def _display(F: List[List[str]]) -> None:
    """
    Display a list of functional dependencies.
    :param F: A list of functional dependencies
    """
    for X, Y in F:
        for x in X:
            print(x, end='')
        print(" -> ", end='')
        for y in Y:
            print(y, end='')
        print()


def _display_decomposition(F: List[List[str]]) -> None:
    """
    Display a list of functional dependencies.
    :param F: A list of functional dependencies
    """
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
    """
    Create a file with random letters.
    :param letter: A string of letters
    """
    
    # Create the output file
    file = open("jeu_donnée.txt", "w")
    
    # Transforms the string into a list of letters
    letter_list = list(letter.lower())

    # Picks a random letter and writes it in the file
    for l in letter_list:
        int1 = random.randint(1, len(letter_list))
        int2 = random.randint(1, len(letter_list))
        rand_letters = []
        rand_right_letters = []
            
        # Get two random numbers and use them to choose two random letters
        for _ in range(int1):
            rand_letter = random.choice(letter_list)
            rand_letters.append(rand_letter)

        for _ in range(int2):
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