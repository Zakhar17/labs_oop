from ..house.house import House

class HouseBuilder:
    def __init__(self):
        self._house = House(rooms=0, floors=0, color='')

    def set_rooms(self, rooms: int):
        self._house.rooms = rooms
        return self

    def set_floors(self, floors: int):
        self._house.floors = floors
        return self

    def set_color(self, color: str):
        self._house.color = color
        return self

    def build(self) -> House:
        return self._house
