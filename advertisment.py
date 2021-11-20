from estate import *
from deal import Rent, Sale
from base import BaseClass


class ApartmentRent(Apartment, Rent, BaseClass):
    def show_detail(self):
        print("------------------------------------------------------")
        print("#" * 5, f" \t ApartmentRent{self.id} \t", "#" * 5)
        self.show_description()
        self.show_price()


class ApartmentSale(Apartment, Sale, BaseClass):
    def show_detail(self):
        print("------------------------------------------------------")
        print("#" * 5, f" \t ApartmentSale{self.id} \t", "#" * 5)
        self.show_description()
        self.show_price()


class HouseRent(House, Rent, BaseClass):
    def show_detail(self):
        print("------------------------------------------------------")
        print("#" * 5, f" \t HouseRent{self.id} \t", "#" * 5)
        self.show_description()
        self.show_price()


class HouseSale(House, Sale, BaseClass):
    def show_detail(self):
        print("------------------------------------------------------")
        print("#" * 5, f" \t HouseSale{self.id} \t", "#" * 5)
        self.show_description()
        self.show_price()


class StoreSale(Store, Sale, BaseClass):
    def show_detail(self):
        print("------------------------------------------------------")
        print("#" * 5, f" \t StoreSale{self.id} \t", "#" * 5)
        self.show_description()
        self.show_price()


class StoreRent(Store, Rent, BaseClass):
    def show_detail(self):
        print("------------------------------------------------------")
        print("#" * 5, f" \t StoreRent{self.id} \t", "#" * 5)
        self.show_description()
        self.show_price()
