from house_builder import House, HousePrototype, HouseBuilder

def main():
    # Using HousePrototype
    house_prototype = HousePrototype(House(rooms=3, floors=2, color='red'))
    house1 = house_prototype.clone()
    house2 = house_prototype.clone(color='blue')
    house3 = house_prototype.clone(rooms=4, floors=3)

    print(house1)
    print(house2)
    print(house3)

    # Using HouseBuilder
    house_builder = HouseBuilder().set_rooms(3).set_floors(2).set_color('red')
    house4 = house_builder.build()
    house_builder.set_color('blue')
    house5 = house_builder.build()
    house_builder.set_rooms(4).set_floors(3)
    house6 = house_builder.build()

    print(house4)
    print(house5)
    print(house6)

if __name__ == "__main__":
    main()
