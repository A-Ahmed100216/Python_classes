# TASK:
# Create a cat class with:
# One function that returns "meow"
# 2 classes level variables
# 3 objects
# Display all information with each object
# Change class level variables in each object and dipalys


# Create a cat called Class
class Cat:
    # Create class variables
    animal_kind="Feline"
    colour="Brown"
    # Define a class funtion which returns meow
    def meow(self):
        return "Meowww"

# Create an instance of the class Cat named Garfield
Garfield=Cat()
print(Garfield)
# print the animal_kind attribute of Garfield
print(Garfield.animal_kind)
# print the colour attribute of Garfield
print(Garfield.colour)
# print the meow function of Garfield
print(Garfield.meow())
# Chnage Garfield's colour to orange
Garfield.colour="Orange"
# print out the ammended colour attribute of Garfield
print(Garfield.colour)


# Create another instance of the Cat class named Tom
Tom=Cat()
print(Tom)
# print the animal_kind attribute of Tom
print(Tom.animal_kind)
# print the colour attribute of Tom
print(Tom.colour)
# print the meow function of Tom
print(Tom.meow())
# Change Tom's colour to Grey
Tom.colour="Grey and white"
# print out the ammended colour attribute of Tom
print(Tom.colour)

# Create another instance of the Cat class named Cheshire
Cheshire=Cat()
print(Cheshire)
# print the animal_kind attribute of Cheshire
print(Cheshire.animal_kind)
# print the colour attribute of Cheshire
print(Cheshire.colour)
# print the meow function of Cheshire
print(Cheshire.meow())
# Change Cheshire's colour to Pink and purple
Cheshire.colour="Pink and Purple"
# print out the amended colour attribute of Cheshire
print(Cheshire.colour)
# Change animal Kind attribute of cheshire to imagination
Cheshire.animal_kind="Imagination"
# print out the amended animal kind attribute of Cheshire
print(Cheshire.animal_kind)
