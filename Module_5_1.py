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

house1 = House('Urban', 32)
house2 = House('Python' , 15)

house1.go_to(33)
house2.go_to(6)

print(str(house1))
print(len(house1))

print(str(house2))
print(len(house2))

