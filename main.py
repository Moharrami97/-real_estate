from sample import create_sample
from advertisment import *


class Handler:
    ADVERTISMENT_TYPES = {
        1: ApartmentSale, 2: ApartmentRent,
        3: HouseSale, 4: HouseRent,
        5: StoreSale, 6: StoreRent,
    }

    SWITCHES = {
        "r": "get_report",
        "s": "show_all"
    }

    def get_report(self):
        for adv in self.ADVERTISMENT_TYPES.values():
            print(adv, adv.manager.count())

    def show_all(self):
        for adv in self.ADVERTISMENT_TYPES.values():
            for obj in adv.object_list:
                print(obj.show_detail())

    def run(self):
        print("Hello world!")
        for key in self.SWITCHES:
            print(f"press {key} for {self.SWITCHES[key]}")
        user_input = input("please Enter choice: ")
        switch = self.SWITCHES.get(user_input, None)
        if switch is None:
            print("Invalid input")
            self.run()
        choice = getattr(self, switch, None)
        choice()


if __name__ == "__main__":
    create_sample()
    handler = Handler()

    handler.run()
    search_result_manager = ApartmentSale.manager.search(price_per_meter=[40, 80])
    print(search_result_manager)
