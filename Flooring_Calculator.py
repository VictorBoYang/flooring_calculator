from Class_House import *


name_input = input("Enter the customer’s name: \n")
phone_input = input("Enter the customer’s phone number: \n")
state_input = input("Enter the customer’s state: \n")
zip_input = input("Enter the customer’s zip code: \n")
number_of_rooms_input = input("Enter the number of rooms: \n")
number_of_rooms_input = int(number_of_rooms_input)

house1 = House(number_of_rooms_input)
house1.ownerName_setter(name_input)
house1.phoneNumber_setter(phone_input)
house1.state_setter(state_input)
house1.zipCode_setter(zip_input)
print(house1.rooms)

for i in range(number_of_rooms_input):
    area_in = input("Enter the area(in square feet) of room %d: " % (i+1))
    floor_type_in = input("Select flooring type(1 for Carpet, 2 for Tile, 3 for Hardwood): ")
    house1.addRooms(area_in, floor_type_in)

