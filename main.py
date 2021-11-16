from random import choice
from user import User
from real_estate import *

FIRST_NAME = ["narges", "negin", "milad"]
LAST_NAME = ["moharrami", "razavi", "hasani"]
MOBILES = ["09105556677", "09304445588", "09919996585", "09129996633"]

if __name__ == "__main__":
    for mobile in MOBILES:
        User(choice(FIRST_NAME), choice(LAST_NAME), mobile)

    for user in User.object_list:
        print(f"{user.id} \t {user.fullname}")

# apartment_rent = ApartmentRent(floor=2, elevator=True, fixed_amount=50000000, monthly_amount=1000000)
# apartment_sale = ApartmentSale(floor=2, elevator=True, fee=500000000)
# house_rent = HouseRent(age=8, address="tehran", fixed_amount=60000000, monthly_amount=2000000)
# house_sale = HouseSale(age=8, address="tehran", fee=600000000)
