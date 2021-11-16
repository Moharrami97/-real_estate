class Rent:
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
