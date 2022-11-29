class TravelAgent:
    def __init__(self, name):
        self.name = name
        self.trips = None

    def set_one_city_one_way(self):
        pass

    def set_one_city_two_way(self):
        pass

    def set_multi_city_city_one_way(self):
        pass

    def set_multi_city_round(self):
        pass

    def __repr__(self):
        return f'Name {self.name} Trips: {self.trips}'
