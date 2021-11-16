from base import BaseClass


class EstateAbstract(BaseClass):
    def __init__(self, user, area, room_count, built_year, region, address, *args, **kwargs):
        self.user = user
        self.area = area
        self.room_count = room_count
        self.built_year = built_year
        self.region = region
        self.address = address
        super().__init__(*args, **kwargs)


class Apartment(EstateAbstract):
    pass


class House(EstateAbstract):
    pass


class Store(EstateAbstract):
    pass
