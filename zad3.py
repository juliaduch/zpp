# 3. Stworzyć funkcję, która będzie sprawdzała czy przekazana
# liczba w parametrze jest parzysta i zwróci tą informację jako
# typ logiczny bool ( True / False ). Należy uruchomić funkcję,
# wynik wykonania zapisać do zmiennej, a następnie wykorzystując
# warunek logiczny wyświetlić prawidłowy tekst "Liczba parzysta" /
# "Liczba nieparzysta"


def parzysta(liczba):
    if liczba % 2 == 0:
        return True
    else:
        return False


wynik = parzysta(5)

print("Liczba parzysta") if wynik is True else print("Liczba nieparzysta")
