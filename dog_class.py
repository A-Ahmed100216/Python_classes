# Classes, objects and instantiation

# Create a class called Dog
class Dog:
    # Defining a class variable - an attribute
    animal_kind="canine"

    def __init__(self,name,colour): # The __init__ method initialises the class
        self.name=name
        self.colour=colour

    # Defining a class funtion, self returns the class.
    def bark(self):
        # Return "woof" when the function is called
        return "woof"

# # Created an instance of the dog class and stored it in the variable fido
# fido = Dog()
# print(fido) #  Output  ---> <__main__.Dog object at 0x10d704040>


# We cannot use previous fido anymore because we need to supply afguments, we have initialise the class so it takes arguments.
fido2 =Dog("Fido","Brown") # Crreting an instance of the class with the arguments.
print(fido2.colour)

#  Why init?
# Behaviours, attributes are defined in the init


# # Once instantiated, attributes of the class can be called.
# print(fido.animal_kind) # This returns canine.
# print(fido.bark())  # This returns woof as the bark function is executed.
#
# # Created another instance of the Dog Class
# lassie=Dog()
# # lassie and fido are instances of the same class therefore same outputs.
# print(lassie.animal_kind) # Returns canine.
# print(lassie.bark())  # Returns woof
#
#
# # We can change a specific attribute
# fido.animal_kind="Loyal Dog"
# print(fido.animal_kind) # Returns "Loyal Dog"
#
# # This will not affect the class itself, the original value of the attribute animal_kind will remain the same
# print(lassie.animal_kind) # Returns "canine"


