from ..house.house import House

class HousePrototype:
    def __init__(self, house: House):
        self._house = house

    def clone(self, **kwargs):
        house_attrs = self._house.__dict__.copy()
        house_attrs.update(kwargs)
        return House(**house_attrs)
