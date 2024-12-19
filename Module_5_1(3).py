class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        print(f'Название {name}, этажей : {number_of_floors} ')

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Неверный этаж!')
        else:
            for i in range(1, new_floor + 1):
                print(i)
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
       return f'ЖК {self.name}'

    def __eq__(self, other):
        return self.number_of_floors == other

    def __lt__(self, other):
        return self.number_of_floors < other

    def __le__(self, other):
        return self.number_of_floors <= other

    def __gt__(self, other):
        return self.number_of_floors > other

    def __ge__(self, other):
        return self.number_of_floors >= other

    def __ne__(self, other):
        return self.number_of_floors != other

    def __add__(self, value):
        return self.number_of_floors + value

h1 = House('Urban', 5)
h2 = House('Python' , 6)

h1.go_to(33)
h2.go_to(6)

print(str(h1))
print(len(h1))

print(str(h2))
print(len(h2))

print(h1 == h2) # __eq__


h1 = h1 + 10 # __add__

print(h1)

print(h1 == h2)

print(h1 > h2) # __gt__

print(h1 >= h2) # __ge__

print(h1 < h2) # __lt__

print(h1 <= h2) # __le__

print(h1 != h2) # __ne__
