class Parent:
    def __init__(self):
        print("I am parent class")

class Child(Parent):  # make the parent argument a child class
    def __init__(self):
        super().__init__()  # call the parent class constructor
        print("I am child class")

# Grandchild
class GrandChild(Parent):
    def __init__(self):
        super().__init__() # it can call all the classes with relative of that parent class
        print("I am grandchild class")

grandchild = GrandChild()
print(grandchild)