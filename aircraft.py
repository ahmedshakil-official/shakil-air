class Aircraft:
    def __init__(self, brand, code, type, flight_range):
        self.brand = brand
        self.code = code
        self.type = type
        self.flight_range = float(flight_range)

    def get_brand(self):
        return self.brand

    def get_range(self):
        return self.flight_range

    def __repr__(self):
        return f'Aircraft brand: {self.brand} code: {self.code} type: {self.type} range: {self.flight_range}'