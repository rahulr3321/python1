class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"
class cat(Animal):
    def speak(self):
        return "meow"

dog = Dog()
print(dog.speak())  # Calls the 'speak' method of the Dog class
Cat=cat()
print(Cat.speak())