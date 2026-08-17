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

    def __init__(self, name, age, gender, breed, adopted):
        super().__init__(self, name, age, gender, breed, adopted=False)

    def  make_sound(self):
        print("Woof woof")

class Cat(Animal):

    def __init__(self, name, age, gender, breed):
        super().__init__(self, name, age, gender, breed)

    def make_sound(self):
        print("Meow meow")

class Bird(Animal):

    def __init__(self, name, age, gender, breed):
        super().__init__(self,name,age,gender,breed)

    def make_sound(self):
        print("Screech screech")

class Rabbit(Animal):

    def __init__(self, name, age, gender, breed):
        super().__init__(self,name,age,gender,breed)

    def make_sound(self):
        print("Squeak squeak")