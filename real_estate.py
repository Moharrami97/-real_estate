from main import *

if __name__ == "__main__":
    apartment_rent = ApartmentRent(floor=2, elevator=True, fixed_amount=50000000, monthly_amount=1000000)
    apartment_sale = ApartmentSale(floor=2, elevator=True, fee=500000000)
    house_rent = HouseRent(age=8, address="tehran", fixed_amount=60000000, monthly_amount=2000000)
    house_sale = HouseSale(age=8, address="tehran", fee=600000000)

    print(apartment_rent)
    print(apartment_sale)
    print(house_rent)
    print(house_sale)
