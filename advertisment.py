from estate import *
from deal import Rent, Sale


class ApartmentRent(Apartment, Rent):
    def __str__(self):
        return f"floor: {self.floor} \t fixed_amount: {self.fixed_amount}"


class ApartmentSale(Apartment, Sale):
    def __str__(self):
        return f"floor: {self.floor} \t fee: {self.fee}"


class HouseRent(House, Rent):
    def __str__(self):
        return f"address: {self.address} \t fixed_amount: {self.fixed_amount}"


class HouseSale(House, Sale):
    def __str__(self):
        return f"address: {self.address} \t fixed_amount: {self.fee}"


class StoreSale(Store, Sale):
    pass


class StoreRent(Store, Rent):
    pass
