#!/usr/bin/env python3


class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed  # <-- You forgot this line!

    def bark(self):
        return "Woof!"

    def sit(self):
        return f"{self.name} is sitting"
