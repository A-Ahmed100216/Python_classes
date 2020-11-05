# Python Classes 
### *Objectives*
* *Introduction to OOP*
* *What are classes?*
* *Why do we use classes?*
* *How do we create classes?*

## Object Oriented Programming (OOP)
There are 4 pillars:
1. Inheritance - Eliminates redundant code
  * Enables new classes to take on properties of existing classes.
  * We can use all the behaviours and attributes assocaited with the parent class. 
2. Encapsulation - Reduce complexity and increase re-usability.
  * Collating data and functions together 
3. Abstraction - Reduce complexity and isolate impact of changes 
4. Polymorphism - Refactor code or case statements.
  * Refers to programming language's ability to process objects differently depending on their date type or class. More specifically, it is the ability to redefine methods for derived classes.
  * Allows us to change behaviours or attributes.

## What are Classes?
* In object oriented programming, everything is an object. 
* A class is used to define attributes and create objects. 
* Classes are a way to bring data and functionality together.

## Why do we use Classes?
**Classes are used to implement the pillars of OOP.**

## How do we create a Class?
* Syntax - We use the ```class``` keyword followed by the name and a colon.
```python 
class <Name_of_class>:
```
* **The name of the class must be capitalised.**
* Make sure good naming convention is applied - the name should be logical and not reserved in Python.

### Example
* This example creates a class titled Dog. 
* Within the class, a variable is created called ```animal_kind```. This is assigned a value "canine". 
* A function is then created. This function takes the argument **self** which **returns the current class.** 
```python
class Dog:
    # Create a class variable
    animal_kind="canine" 
    # Create a class function which returns woof when executed
    def bark(self):
        return "woof"
```

## Instances 
* In order to execute a class, we have to create an object of the class - this is known as instantiating the class- we are creating an instance of the class.
* Returning to the dog example:
```python
fido = Dog() 
```
* We have created an instance of the dog class and stored it in the variable ```fido```.
* If we print this instance, the memory location of the instance is returned:
```python
print(fido)
```
* The output will look something like this:
```
<__main__.Dog object at 0x10d704040>
``` 

* We have transferred all the attributes to fido. Just as we could do ```.upper``` or ```.lower``` etc. in python, we can do the same to ```fido```. But only with attributes which exist in the class i.e. ```animal_kind``` and the function ```bark```.
```python
print(fido.animal_kind) # Returns canine.
print(fido.bark())  # Returns woof.
```
* The class can be used as much as we want to create other instances of the Dog class. 
```python
lassie=Dog()
print(lassie.animal_kind)
print(lassie.bark())
```
* The outputs of the print statement will be the same as ```fido``` as both dog variables are instances of the same class, the Dog class.

* We can change a specific attribute as shown:
```python
fido.animal_kind="Loyal Dog"
print(fido.animal_kind)
```
* This will not affect the class itself, the original value of the attribute ```animal_kind``` will remain the same.
* Recall ```lassie``` uses the same class, but we have not changed the original class, so the animal kind variable should be "canine" for ```lassie```
```python
print(lassie.animal_kind) # Returns "canine"
```
* ***Any change we make to an object, does not impact the original class***

# OOP 
Methods and Functions accomplish the same job but functions exist in classes 

