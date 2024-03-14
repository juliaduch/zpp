class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, area, rooms: int, price, address, plot,
                 rozmiar_dzialki: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot
        self.rozmiar_dzialki = rozmiar_dzialki

    def __str__(self):
        return f'House with area of {self.area} and {self.rooms} rooms, ' \
               f'costs {self.price}, in {self.address},' \
               f' plot {self.plot}, area {self.rozmiar_dzialki}'


class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f'Flat with area of {self.area} and {self.rooms} rooms,' \
               f' costs {self.price}, ' \
               f'in {self.address}, on {self.floor} floor'
