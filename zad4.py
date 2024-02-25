# 4. Stworzyć funkcję, która przyjmie 3 argumenty typu int
# i sprawdzi czy suma dwóch pierwszych liczb jest większa
# lub równa trzeciej, a następnie zwróci tę informację
# jako typ logiczny bool


def suma(l1: int, l2: int, l3: int):
    if l1+l2 >= l3:
        return True
    else:
        return False


print(suma(6, 7, 8))
