class Airport:
    def __init__(self, code, name, city, country, lat, lon, rate):
        self.code = code
        self.name = name
        self.city = city
        self.country = country
        self.lat = float(lat)
        self.lon = float(lon)
        self.rate = float(rate)

    def __repr__(self):
        return f'Airport name: {self.name} country: {self.country} lat: {self.lat} long: {self.long} rent: {self.rent}'