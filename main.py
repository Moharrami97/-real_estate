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


class Rent:
    def __init__(self, fixed_amount, monthly_amount):
        self.fixed_amount = fixed_amount
        self.monthly_amount = monthly_amount


class Sale:
    def __init__(self, fee):
        self.fee = fee


class ApartmentRent(Apartment, Rent):
    def __str__(self):
        return f"floor: {self.floor} \t fixed_amount: {self.fixed_amount}"


class ApartmentSale(Apartment, Sale):
    def __str__(self):
        return f"floor: {self.floor} \t fee: {self.fee}"


class HouseRent(House, Rent):
    pass


class HouseSale(House, Sale):
    pass
