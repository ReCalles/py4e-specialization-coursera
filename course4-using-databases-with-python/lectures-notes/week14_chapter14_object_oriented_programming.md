# Chapter 14: Object-Oriented Programming (OOP)

* **Object-Oriented Programming (OOP):** A programming paradigm based on the concept of "objects", which can contain data (attributes) and code (methods). It aims to model real-world entities.

* **Classes:**
    * A blueprint or template for creating objects.
    * Defines the attributes and methods that all objects of that class will have.
    * Defined using the `class` keyword.
    ```python
    class PartyAnimal:
        x = 0 # An attribute (data)

        def party(self): # A method (code)
            self.x = self.x + 1
            print("So far", self.x)
    ```

* **Objects (Instances):**
    * An individual instance of a class.
    * Created by calling the class like a function: `an = PartyAnimal()`.
    * Each object has its own unique set of attributes.

* **Methods:**
    * Functions defined inside a class that operate on the object's data.
    * The first parameter of any method is conventionally named `self`, which refers to the instance of the class itself.

* **Constructor (`__init__` Method):**
    * A special method that is automatically called when a new object of the class is created.
    * Used to initialize the object's attributes.
    ```python
    class PartyAnimal:
        x = 0
        name = ""

        def __init__(self, nam): # Constructor with a parameter
            self.name = nam
            print(self.name, "constructed")

        def party(self):
            self.x = self.x + 1
            print(self.name, "so far", self.x)
    ```

* **`self` Parameter:**
    * A convention (not a keyword) referring to the instance of the object itself.
    * It allows methods to access and modify the object's own attributes.

* **Inheritance (Briefly):**
    * Allows a new class (subclass/derived class) to inherit attributes and methods from an existing class (superclass/base class).
    * Promotes code reuse and creates an "is-a" relationship (e.g., a Dog *is a* PartyAnimal).
    ```python
    class CricketFan(PartyAnimal): # CricketFan inherits from PartyAnimal
        points = 0
        def six(self):
            self.points = self.points + 6
            self.party() # Can call methods from the base class
            print(self.name, "points", self.points)
    ```

* **Why OOP?**
    * **Organization:** Groups related data and functions.
    * **Reusability:** Classes can be reused to create many objects.
    * **Modeling:** Helps model real-world concepts and relationships.
    * **Encapsulation:** Bundles data and methods that operate on the data within one unit.