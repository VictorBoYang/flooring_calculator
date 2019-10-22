from Floor_Type import *


class House:
    class Room:
        def __init__(self, areaIn, floorTypeIn):
            self.area = areaIn
            self.floorType = floorTypeIn

        def area_getter(self):
            return self.area

        def floorType_getter(self):
            return self.floorType

    def __init__(self, num_Rooms):
        self.ownerName = None
        self.phoneNumber = None
        self.streetAddress = None
        self.city = None
        self.state = None
        self.zipCode = None
        self.rooms = [self.Room for i in range(num_Rooms)]
        self.roomIndex = 0

    def ownerName_setter(self, owner_name):
        self.ownerName = owner_name

    def phoneNumber_setter(self, phone_number):
        self.phoneNumber = phone_number

    def streetAddress_setter(self, street_address):
        self.streetAddress = street_address

    def city_setter(self, city):
        self.city = city

    def state_setter(self, state):
        self.state = state

    def zipCode_setter(self, zip_code):
        self.zipCode = zip_code

    def addRooms(self, sqft, fType):
        self.Room(sqft, fType)

    def get_installation_cost(self):
        total = self.Room.area_getter() * 10
        return total

    def get_flooring_cost(self):
        if self.Room.floorType_getter() == Floor_Type.CARPET:
            floor_cost = self.Room.area_getter() * 7
            return floor_cost
        elif self.Room.floorType_getter() == Floor_Type.TILE:
            floor_cost = self.Room.area_getter() * 5
            return floor_cost
        elif self.Room.floorType_getter() == Floor_Type.HARDWOOD:
            floor_cost = self.Room.area_getter() * 6
            return floor_cost
