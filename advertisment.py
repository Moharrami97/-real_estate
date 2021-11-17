from estate import *
from deal import Rent, Sale


class ApartmentRent(Apartment, Rent):
    def show_detail(self):
        self.show_description()
        self.show_price()


class ApartmentSale(Apartment, Sale):
    def show_detail(self):
        self.show_description()
        self.show_price()


class HouseRent(House, Rent):
    def show_detail(self):
        self.show_description()
        self.show_price()


class HouseSale(House, Sale):
    def show_detail(self):
        self.show_description()
        self.show_price()


class StoreSale(Store, Sale):
    def show_detail(self):
        self.show_description()
        self.show_price()


class StoreRent(Store, Rent):
    def show_detail(self):
        self.show_description()
        self.show_price()
