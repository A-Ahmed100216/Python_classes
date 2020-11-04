# Classes, objects and instantiation

# Create a class called Dog
class Dog:
    # Defining a class variable - an attribute
    animal_kind="canine"


    # Defining a class funtion, self returns the class.
    def bark(self):
        # Return "woof" when the function is called
        return "woof"

# Created an instance of the dog class and stored it in the variable fido
fido = Dog()
print(fido) #  Output  ---> <__main__.Dog object at 0x10d704040>


# Once instantiated, attributes of the class can be called.
print(fido.animal_kind) # This returns canine.
print(fido.bark())  # This returns woof as the bark function is executed.

# Created another instance of the Dog Class
lassie=Dog()
# lassie and fido are instances of the same class therefore same outputs.
print(lassie.animal_kind) # Returns canine.
print(lassie.bark())  # Returns woof


# We can change a specific attribute
fido.animal_kind="Loyal Dog"
print(fido.animal_kind) # Returns "Loyal Dog"

# This will not affect the class itself, the original value of the attribute animal_kind will remain the same
print(lassie.animal_kind) # Returns "canine"


