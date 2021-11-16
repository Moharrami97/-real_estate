from estate import *
from deal import Rent, Sale


class ApartmentRent(Apartment, Rent):
    def show_detail(self):
        self.show_description()
        self.show_price()

    def __str__(self):
        return f"floor: {self.floor} \t fixed_amount: {self.initial_price}"


class ApartmentSale(Apartment, Sale):
    def __str__(self):
        return f"floor: {self.floor} \t fee: {self.price_per_meter}"


class HouseRent(House, Rent):
    def __str__(self):
        return f"address: {self.address} \t fixed_amount: {self.initial_price}"


class HouseSale(House, Sale):
    def __str__(self):
        return f"address: {self.address} \t fixed_amount: {self.price_per_meter}"


class StoreSale(Store, Sale):
    pass


class StoreRent(Store, Rent):
    pass
