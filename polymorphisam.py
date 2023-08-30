from oops.inheritance import Cat, Dog


def animal_sound(animal):
    return animal.speak()

cat = Cat()
dog = Dog()

print(animal_sound(cat))  # Calls the 'speak' method of the Cat class
print(animal_sound(dog))  # Calls the 'speak' method of the Dog class
