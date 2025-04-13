class Animal:
    def speak(self):
        return "Animal makes a sound"

class Mammal(Animal):
    def has_fur(self):
        return "Mammal has fur"

class Dog(Mammal): # inherited both functions speak and has_fur
    def bark(self):
        return "Dog barks"
    
dog = Dog() 

print(dog.speak())
print(dog.has_fur())
print(dog.bark())

"""
Output would be like:
    Animal makes a sound
    Mammal has fur
    Dog barks

This shows that dog has inherited the funcyion has_fur and
speak from mammal.! has_fur was the function of mammal and speak
was the function of Animal which was inherited to Mammal which in
turn was inherited to Dog
"""