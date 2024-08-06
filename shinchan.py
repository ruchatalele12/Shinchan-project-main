import random

class Shinchan:
    def __init__(self, name):
        self.name = name
        self.stamina = 100
        self.score = 0

    def play_with_nani(self):
        if self.stamina >= 20:
            self.stamina -= 20
            self.score += 10
            print(f"\n{self.name} is playing with Nani! Stamina is now {self.stamina}.")
            print(f"Score: {self.score}")
        else:
            print(f"\n{self.name} is too tired to play with Nani.")
        self.check_for_food()

    def watch_action_kamen(self):
        if self.stamina >= 10:
            self.stamina -= 10
            self.score += 5
            print(f"\n{self.name} is watching Action Kamen! Stamina is now {self.stamina}.")
            print(f"Score: {self.score}")
        else:
            print(f"\n{self.name} is too tired to watch Action Kamen.")
        self.check_for_food()

    def play_with_shiro(self):
        if self.stamina >= 15:
            self.stamina -= 15
            self.score += 7
            print(f"\n{self.name} is playing with Shiro! Stamina is now {self.stamina}.")
            print(f"Score: {self.score}")
        else:
            print(f"\n{self.name} is too tired to play with Shiro.")
        self.check_for_food()

    def dance(self):
        if self.stamina >= 25:
            self.stamina -= 25
            self.score += 15
            print(f"\n{self.name} is dancing! Stamina is now {self.stamina}.")
            print(f"Score: {self.score}")
        else:
            print(f"\n{self.name} is too tired to dance.")
        self.check_for_food()

     def go_to_park(self):
         if self.stamina >= 25:
             self.stamina -= 25
             self.score += 30
             print(f"\n{self.name} is going to the park! Stamina is now {self.stamina}.")
             print(f"Score: {self.score}")
        else:
            print(f"\n{self.name} is too tired to go to the park.")
            self.check_for_food()

    def eat_ramen(self):
        if self.stamina <= 80:
            self.stamina += 30
        else:
            self.stamina = 100
        print(f"\n{self.name} ate some ramen! Stamina is now {self.stamina}.")
    def drink_energy_drink(self):
        if self.stamina <= 50:
            self.stamina += 30
        else:
            self.stamina = 100  
        print(f"\n{self.name} drank an energy drink! Stamina is now {self.stamina}.")
    def rest(self):
        print(f"\n{self.name} is taking a rest to recover stamina.")
        self.stamina += 20
        if self.stamina > 100:
            self.stamina = 100
        print(f"Stamina is now {self.stamina}.")

    def check_for_food(self):
        if self.stamina < 50:
            print(f"\n{self.name} is feeling tired and hungry.")
            self.eat_ramen()
            self.rest()

    def check_status(self):
        print(f"\n{self.name}'s current status:")
        print(f"Stamina: {self.stamina}")
        print(f"Score: {self.score}")

    def random_event(self):
        events = [
            ("A cat steals some food! Lose 10 stamina.", -10),
            ("Shinchan found a hidden toy! Gain 10 stamina.", 10),
            ("Shinchan is feeling sleepy. Lose 5 stamina.", -5),
            ("Shinchan found some ice cream! Gain 15 stamina.", 15)
        ]
        event, stamina_change = random.choice(events)
        self.stamina += stamina_change
        if self.stamina > 100:
            self.stamina = 100
        elif self.stamina < 0:
            self.stamina = 0
        print(f"\nEvent: {event} Stamina is now {self.stamina}.")
