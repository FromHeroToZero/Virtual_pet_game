# Import the random module for generating random events
import json
# Define the Pet class

# Method to print the current status of the pet

# Method to increase the pet's hunger level

# Method to increase the pet's happiness level

# Method to increase the pet's cleanliness level

# Method to introduce random events that affect the pet's status


import random


class Pet:
    def __init__(self, name: str):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.cleanliness = 50

    def status(self):
        print(f"Name: {self.name}")
        print(f"Hunger level: {self.hunger}")
        print(f"Happiness level: {self.happiness}")
        print(f"Cleanliness level: {self.cleanliness}")

    def feed(self):
        self.hunger += 10
        print(f"You fed {self.name}. Hunger increased to {self.hunger}.")

    def play(self):
        self.happiness += 10
        print(f"You played with {self.name}. Happiness increased to {self.happiness}.")

    def clean(self):
        self.cleanliness += 10
        print(f"You cleaned {self.name}. Cleanliness increased to {self.cleanliness}.")

    def random_event(self):
        event = random.choice(["hunger", "happiness", "cleanliness"])
        print(event)
        if event == 'hunger':
            self.hunger -= 5
            print(f"{self.name} got a little hungry. Hunger decreased to {self.hunger}.")
        elif event == 'happiness':
            self.happiness -= 5
            print(f"{self.name} is feeling a bit lonely. Happiness decreased to {self.happiness}.")
        elif event == 'cleanliness':
            self.cleanliness -= 5
            print(f"{self.name} got a bit dirty. Cleanliness decreased to {self.cleanliness}.")

    def save(self):
        pass

    def load(self):
        pass
