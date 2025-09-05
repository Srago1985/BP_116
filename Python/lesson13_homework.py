# part 1
class Car:
    pass
car1 = Car()
car1.model = "Mazda CX-5"
car1.year = 2023
car1.color = "Blue"
car1.engine = 2.5

car2 = Car()
car2.model = "Toyota RAV4"
car2.year = 2022
car2.color = "Red"
car2.engine = 2.5

car3 = Car()
car3.model = "Honda CR-V"
car3.year = 2021
car3.color = "Gray"
car3.engine = 1.5

car4 = Car()
car4.model = "Ford Escape"
car4.year = 2020
car4.color = "Black"
car4.engine = 2.0

car5 = Car()
car5.model = "Chevrolet Equinox"
car5.year = 2023
car5.color = "White"
car5.engine = 1.5
garage = [car1, car2, car3, car4, car5]

for car in garage:
    print(f"Model: {car.model}, Year: {car.year}, Color: {car.color}, Engine: {car.engine}L")
    
# part 2
class Arsenal_squad:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def display_players(self):
        for player in self.players:
            print(f"Player: {player}")

arsenal = Arsenal_squad()
arsenal.add_player("Bukayo Saka")
arsenal.add_player("Gabriel Martinelli")
arsenal.add_player("Martin Ødegaard")
arsenal.display_players()