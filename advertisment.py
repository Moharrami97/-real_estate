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
