from random import choice
from user import User
from region import Region
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
    reg2 = Region(name="javid")
    apt1 = Apartment(
        user=User.object_list[0], area=80, room_count=2, has_elevator=True,
        has_parking=True, floor=2, region=reg1, built_year=1393,
        address="some text..."
    )

    house1 = House(
        has_yard=True, floors_count=1, user=User.object_list[2], area=480,
        room_count=6, built_year=1370, region=reg1, address="some text..."
    )

    store1 = Store(
        user=User.object_list[-1], area=30, room_count=0, built_year=1390,
        region=reg1, address="some text..."
    )

    # creat advertisment
    apartment_sell1 = ApartmentSale(
        user=User.object_list[0], area=80, room_count=2, has_elevator=True, floor=2,
        has_parking=True, region=reg1, built_year=1393,
        address="some text...", price_per_meter=50, convertable=False, discountable=True
    )
    apartment_sell1.show_detail()

    apartment_sell2 = ApartmentSale(
        user=User.object_list[1], area=100, room_count=3, has_elevator=True, floor=1,
        has_parking=True, region=reg2, built_year=1385,
        address="some text...", price_per_meter=70, convertable=True, discountable=True
    )
    apartment_sell2.show_detail()

    house_sell = HouseSale(
        has_yard=True, floors_count=1, user=User.object_list[2], area=480,
        room_count=6, built_year=1370, region=reg1, address="some text...",
        price_per_meter=90, convertable=True, discountable=False
    )
    house_sell.show_detail()

    search_result_manager = ApartmentSale.manager.search(region=reg2)
    print(search_result_manager)

    search_result_manager = ApartmentSale.manager.search(price_per_meter__max=80)
    print(search_result_manager)

    search_result_get = ApartmentSale.manager.get(room_count=3)
    print(search_result_get)

    search_result_get = ApartmentSale.manager.get(area__max=100)
    print(search_result_get)
