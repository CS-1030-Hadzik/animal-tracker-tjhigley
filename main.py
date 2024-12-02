from animal import Animal
from dog import Dog

if __name__ == "__main__":
    animal = Animal("Pan", "Cat")
    print(animal)
    animal.speak()

    dog = Dog("Jake","Canine","Australian Cow Dog")
    print(dog)
    dog.speak()

    print(Animal.all_animals)