# 6. Stworzyć funkcję, która przyjmuje 2 argumenty typu list
# i zwraca wynik typu list . Funkcja ma za zadanie złączyć
# przekazane listy w jedną, usunąć duplikaty, każdy
# element podnieść do potęgi 3 stopnia, a następnie zwrócić powstałą listę.


def operacje(lista1: list, lista2: list):
    nowa_lista = lista1+lista2
    nowa_lista = list(dict.fromkeys(nowa_lista))
    nowa_lista = [el**3 for el in nowa_lista]
    return nowa_lista


print(operacje([1, 2, 3, 4, 5], [0, 9, 8, 2, 2, 3]))
