# Classes, objects and instantiation


# Classes are a way to bring data and functionality together.
class Dog:
    animal_kind="canine"

    # Defining a class variable - an attribute
    # Self returns to the current class
    def bark(self):
        return "woof"

# in order to execute a class, we have to create an object of the class - this is known as instantiating the class- we are creating an instance of the class.
# To call the function, we must instantiate
fido = Dog() #We have created an instance of the dog class and stored it in the variable fido.
print(fido)
# The output will look something like this
# <__main__.Dog object at 0x10d704040>
# This is the memory location of the instance fido.
# We have transferred all the attributes to fido. Just as we could do .upper or .lower etc in normal python, we can do the same to fido. But only with attributes which exist in the class i.e. animal_kind and the function bark.
print(fido.animal_kind) # This returns canine.
print(fido.bark())  # This returns woof as this function is executed.

#  We can create another insatnce of our Dog Class
lassie=Dog()
print(lassie.animal_kind)
print(lassie.bark())
#  The outputs of the print statement will be the same as fido as both dog variables are instances of the same class, the Dog class.

# We can change a specific attribute as shown below
fido.animal_kind="Loyal Dog"
print(fido.animal_kind)
# But this will not affect the class itself, the original value of the attribute animal_kind will remain the same
# recall lassie uses the same class, but we have not changed the original class, so the animal kind variabe should be canine for lassie
print(lassie.animal_kind)

# any change we make to an object, does not impact the oriignal class
