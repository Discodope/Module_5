class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        print(f'Название {name}, этажей {number_of_floors} ')

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Неверный этаж')
        else:
            for i in range(1, new_floor + 1):
                print(i)

house1 = House('Urban', 32)
house1.go_to(33)