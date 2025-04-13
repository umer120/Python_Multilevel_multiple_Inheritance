# Python_Multilevel_multiple_Inheritance
Describes how multi-level and multiple inheritance works in Python

**_Multilevel_Inheritance_example1.py:_**

- Demonstrated the multi-level inheritance concept through three classes

- Dog has inherited the function has_fur and speak from mammal.!

- has_fur was the function of mammal and speak was the function of Animal which was inherited to Mammal which in turn was inherited to Dog

**_Multilevel_Inheritance_example2.py:_**

- It's another example of Multilevel inheritance in which three classes have been made

- First class is the Vehicle which has two attributes and a function

- Second class is Car which is Child class of Vehicle class. It has inherited the attributes of class Vehicle and adds another attribute which is of the Car class itself

- Third class is ElectricCar which is Child class of Car class. It has inherited the attributes of Car class: two of the Vehicle class and one of the Car class.. Fourth attribute is of ElectricCar itself

- In this file, function overriding also occurs i.e. Instead of inheriting the function display_info of the base class, child class have made their own function with the same name

**_Multiple_Inheritance_Example.py:_**

- In this program, I have created two class named Phone and Camera, each having two functions

- After that, I have created the third class named SmartPhone which have inherited the two classes: Phone and Camera.

- This class has inherited the four functions: two, two of each parent class. It has its own one function

- I have created a instance of the SmartPhone class and prints the outputs of the functions which this class had either inherited or made its own.
