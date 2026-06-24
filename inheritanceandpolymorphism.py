class Animal:
    def make_sound(self):
        print("Some generic sound")


class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meoww!")


def make_sound(ais):
        ais.make_sound()    

my_dog = Dog()
my_cat = Cat()
make_sound(my_dog)
make_sound(my_cat)