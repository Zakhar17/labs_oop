class House:
    def __init__(self, rooms: int, floors: int, color: str):
        self.rooms = rooms
        self.floors = floors
        self.color = color

    def __str__(self):
        return f"House(rooms={self.rooms}, floors={self.floors}, color={self.color})"
