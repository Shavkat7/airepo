class Animal:
    energy = 0
    weight = 0
    voice = ''

    def __init__(self, name):
        self.name = name

    def feed(self):
        self.weight += 1

    def sleep(self):
        self.energy += 1

    def voice(self):
        pass


class Cow(Animal):
    def milk(self):
        self.weight -= 1

    def voice(self):
        return 'Moooo'

class Goat(Animal):
    
    def milk(self):
        self.weight -= 1

    def voice(self):
        return 'Meeee'    


class Sheep(Animal):
    
    def heard(self):
        self.energy -= 1

    def voice(self):
        return 'Beeee'
    

sheepy = Sheep('Sheepy')
print(sheepy.voice())