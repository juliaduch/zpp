# 5. Stworzyć funkcję, która przyjmie 2 argumenty.
# Pierwszy typu list , a drugi typu int. Funkcja ma sprawdzić
# (zwracając typ logiczny bool ), czy lista z parametru
# pierwszego zawiera taką wartość jaką przekazano w parametrze drugim.


def zawiera(lista: list, element: int):
    if lista.__contains__(element):
        return True
    else:
        return False


print(zawiera([1, 2, 3, 4, 5], 9))
