from random import choice
from user import User
from region import Region
from advertisment import *

FIRST_NAME = ["narges", "negin", "milad"]
LAST_NAME = ["moharrami", "razavi", "hasani"]
MOBILES = ["09105556677", "09304445588", "09919996585", "09129996633"]


def create_sample():
    for mobile in MOBILES:
        User(choice(FIRST_NAME), choice(LAST_NAME), mobile)

    #for user in User.object_list:
        #print(f"{user.id} \t {user.fullname}")

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

    # create advertisment
    apartment_sell1 = ApartmentSale(
        user=User.object_list[0], area=80, room_count=2, has_elevator=True, floor=2,
        has_parking=True, region=reg1, built_year=1393,
        address="some text...", price_per_meter=50, convertable=False, discountable=True
    )

    apartment_sell2 = ApartmentSale(
        user=User.object_list[1], area=100, room_count=3, has_elevator=True, floor=1,
        has_parking=True, region=reg2, built_year=1385,
        address="some text...", price_per_meter=70, convertable=True, discountable=True
    )

    apartment_rent = ApartmentRent(
        user=User.object_list[2], area=50, room_count=1, has_elevator=False, floor=2,
        has_parking=True, region=reg1, built_year=1395, address="some text...",
        initial_price=60, monthly_price=20, convertable=True, discountable=True
    )

    house_sell = HouseSale(
        has_yard=True, floors_count=1, user=User.object_list[2], area=480,
        room_count=6, built_year=1370, region=reg1, address="some text...",
        price_per_meter=90, convertable=True, discountable=False
    )

    house_rent = HouseRent(
        has_yard=True, floors_count=1, user=User.object_list[2], area=480,
        room_count=6, built_year=1370, region=reg1, address="some text...",
        initial_price=70, monthly_price=5, convertable=False, discountable=True
    )

    store_sale = StoreSale(
        user=User.object_list[-1], area=30, room_count=0,
        built_year=1390, region=reg1, address="some text...",
        price_per_meter=65, convertable=False, discountable=False
        )

    store_rent = StoreRent(
        user=User.object_list[-2], area=40, room_count=0,
        built_year=1380, region=reg2, address="some text...",
        initial_price=50, monthly_price=10, convertable=True, discountable=False
    )

    search_result_manager = ApartmentSale.manager.search(region=reg2)

    search_result_manager = ApartmentSale.manager.search(price_per_meter__max=80)

    search_result_get = ApartmentSale.manager.get(room_count=3)

    search_result_get = ApartmentSale.manager.get(area__max=100)

    print("#" * 20, "\t sample created \t", "#" * 20)
