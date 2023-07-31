class Vehicle:
    def __init__(self, brand, year):
        self.brand=brand
        self.year=year
    def display_info(self):
        print(self.__dict__)
class Car(Vehicle):
    def __init__(self, brand, year, count_balon, type):
        super().__init__(brand, year)
        self.count_balon=count_balon
        self.type=type
class Motorcycle(Vehicle):
    def __init__(self, brand, year, count_balon):
        super().__init__(brand, year)
        self.count_balon = count_balon

impala=Car('chevrolet', 2020, 4, 'sedan')
r1_roberts=Motorcycle('yamaha', 2017, 2)

impala.display_info()
r1_roberts.display_info()