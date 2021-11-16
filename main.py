from random import choice
from user import User
from region import Region
from estate import *
from advertisment import *

FIRST_NAME = ["narges", "negin", "milad"]
LAST_NAME = ["moharrami", "razavi", "hasani"]
MOBILES = ["09105556677", "09304445588", "09919996585", "09129996633"]

if __name__ == "__main__":
    for mobile in MOBILES:
        User(choice(FIRST_NAME), choice(LAST_NAME), mobile)

    for user in User.object_list:
        print(f"{user.id} \t {user.fullname}")

    reg1 = Region(name="azadi")
    apt1 = Apartment(
        user=User.object_list[0], area=80, room_count=2, has_elevator=True,
        has_parking=True, floor=2, region=reg1, built_year=1393,
        address="some text..."
    )
    apt1.show_description()

    house1 = House(
        has_yard=True, floors_count=1, user=User.object_list[2], area=480,
        room_count=6, built_year=1370, region=reg1, address="some text..."
    )
    house1.show_description()

    store1 = Store(
        user=User.object_list[-1], area=30, room_count=0, built_year=1390,
        region=reg1, address="some text..."
    )
    store1.show_description()


    #creat advertisment
    apartment_sell = ApartmentSale(
        user=User.object_list[0], area=80, room_count=2, has_elevator=True,
        has_parking=True, floor=2, region=reg1, built_year=1393,
        address="some text...", price_per_meter=10,convertable=False, discountable=True
    )
    apartment_sell.show_detail()