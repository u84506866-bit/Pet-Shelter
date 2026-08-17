class Animal:

    def __init__(self, name, age, gender, breed, adopted):

        self.name = str(name)
        self.age = int(age)
        self.gender = str(gender)
        self.breed = str(breed)
        self.adopted = bool(adopted)

    def show_info(self):
        print(f"{self.name}:{self.age}{self.gender}:{self.breed}")


class Dog(Animal):

    def __init__(self, name, age, gender, breed):
        super().__init__(self, name, age, gender, breed)

    def  make_sound():
        print("Woof woof")

class Cat(Animal):

    def __init__(self, name, age, gender, breed):
        super().__init__(self, name, age, gender, breed)

    def make_sound():
        print("Meow meow")

class Bird(Animal):

    def __init__(self, name, age, gender, breed):
        super().__init__(self,name,age,gender,breed)

    def make_sound():
        print("Screech screech")

class Rabbit(Animal):

    def __init__(self, name, age, gender, breed):
        super().__init__(self,name,age,gender,breed)

    def make_sound():
        print("Squeak squeak")