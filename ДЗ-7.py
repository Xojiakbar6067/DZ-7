class Animal:
    def __init__(self, size, weight, speed):
        self.size=size
        self.weight=weight
        self.speed=speed
    def make_sound(self, s):
        print(s)

class Dog(Animal):
    def __init__(self, size, weight, speed):
        super().__init__(size, weight, speed)
    def protect_house(self):
        print('зашишает дом')
class Cat(Animal):
    def __init__(self, size, weight, speed):
        super().__init__(size, weight, speed)
    def eat_mouse(self):
        print('очишает дом от гризунов')
class Cow(Animal):
    def __init__(self, size, weight, speed):
        super().__init__(size, weight, speed)
    def milk(self):
        print('даёт молоко')

alabay=Dog('big', '30kg', '35km/h')
siams_cat=Cat('little', '2.5kg', '30km/h')
golland=Cow('very big', '360kg', '20km/h')

while True:
    sound=input('animal sound: ')
    if sound=='dog':
        alabay.make_sound('гав-гав')
    elif sound=='cat':
        siams_cat.make_sound("мяууу")
    elif sound=='cow':
        golland.make_sound("мууу-мууу")
    else:
        print('такое животное не знаю')