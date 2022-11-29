class Trip:
    def __init__(self, aircraft, trip_cities, start_date, cost, trip_route=''):
        self.trip_cities = trip_cities
        self.start_date = start_date
        self.aircraft = aircraft
        self.trip_route = trip_route
        self.cost = float(cost)

    def __repr__(self):
        return f'Trip: {self.trip_cities} Cost: {self.cost}'