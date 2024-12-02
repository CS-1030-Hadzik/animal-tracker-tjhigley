class Animal:
    """
    Base class representing a generic animal.
    """

    kingdom = "Animalia"
    all_animals = []

    def __init__(self, name, species):
        self.name = name
        self.species = species
        Animal.all_animals.append(self)

    def speak(self):
        print('The animal makes a noise.')

    def __str__(self):
        return "Kingdom: '"+self.kingdom+"', Name: '"+self.name+"', Species: '"+self.species+"'"
