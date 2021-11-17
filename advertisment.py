from estate import *
from deal import Rent, Sale
from base import BaseClass


class ApartmentRent(Apartment, Rent, BaseClass):
    def show_detail(self):
        self.show_description()
        self.show_price()


class ApartmentSale(Apartment, Sale, BaseClass):
    def show_detail(self):
        self.show_description()
        self.show_price()


class HouseRent(House, Rent, BaseClass):
    def show_detail(self):
        self.show_description()
        self.show_price()


class HouseSale(House, Sale, BaseClass):
    def show_detail(self):
        self.show_description()
        self.show_price()


class StoreSale(Store, Sale, BaseClass):
    def show_detail(self):
        self.show_description()
        self.show_price()


class StoreRent(Store, Rent, BaseClass):
    def show_detail(self):
        self.show_description()
        self.show_price()
