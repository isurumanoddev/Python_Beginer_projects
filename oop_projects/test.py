class Person:
    x = 10

    def non_static_method(self):
        print("non_static_method")

    @staticmethod
    def static_method():
        print("static_method")


person = Person()
person1 = Person()
person2 = Person()
person1.x = 20
person2.x = 40
print("person1.x ", person1.x)
print("person2.x ", person2.x)
# person1.static_method()
