from abc import ABC, abstractmethod


class Apartment:
    def __init__(self, floor, elevator, *args, **kwargs):
        self.floor = floor
        self.elevator = elevator
        super().__init__(*args, **kwargs)


class House:
    def __init__(self, age, address, *args, **kwargs):
        self.age = age
        self.address = address
        super().__init__(*args, **kwargs)


class Rent(ABC):
    def __init__(self, fixed_amount, monthly_amount):
        self.fixed_amount = fixed_amount
        self.monthly_amount = monthly_amount

    @abstractmethod
    def show_banner(self):
        pass


class Sale(ABC):
    def __init__(self, fee):
        self.fee = fee

    @abstractmethod
    def show_banner(self):
        pass


class ApartmentRent(Apartment, Rent):
    def __str__(self):
        return f"floor: {self.floor} \t fixed_amount: {self.fixed_amount}"

    def show_banner(self):
        return "show banner in ApartmentRent"


class ApartmentSale(Apartment, Sale):
    def __str__(self):
        return f"floor: {self.floor} \t fee: {self.fee}"

    def show_banner(self):
        return "show banner in ApartmentSale"


class HouseRent(House, Rent):
    def __str__(self):
        return f"address: {self.address} \t fixed_amount: {self.fixed_amount}"

    def show_banner(self):
        return "show banner in HouseRent"


class HouseSale(House, Sale):
    def __str__(self):
        return f"address: {self.address} \t fixed_amount: {self.fee}"

    def show_banner(self):
        return "show banner in HouseSale"
