# wap where 2 different classes dog and cat has same method speak().
# create objects of both classes and call speak() method.
class Dog:
    def speak(self):
        print("BARK")


class Cat:
    def speak(self):
        print("MEOW")


obj1=Dog()
obj2=Cat()
obj1.speak()
obj2.speak()
