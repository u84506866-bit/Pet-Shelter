class Animal:

    def __init__(self, name, age, gender, breed, id, adopted= False ):

        self.name = str(name)
        self.age = int(age)
        self.gender = str(gender)
        self.breed = str(breed)
        self.adopted = bool(adopted)
        self.id = str(id)


    def show_info(self):
        print(f"{self.name}:{self.age} {self.gender} {self.breed}")


class Dog(Animal):

    def __init__(self, name, age, gender, breed, id,  adopted):
        super().__init__(name, age, gender, breed, id, adopted)

    def  make_sound(self):
        print("Woof woof")

class Cat(Animal):

    def __init__(self, name, age, gender, breed, id,  adopted):
        super().__init__(name, age, gender, breed, id,  adopted)

    def make_sound(self):
        print("Meow meow")

class Bird(Animal):

    def __init__(self, name, age, gender, breed, id,  adopted):
        super().__init__(name,age,gender,breed, id, adopted)

    def make_sound(self):
        print("Screech screech")

class Rabbit(Animal):

    def __init__(self, name, age, gender, breed, id,  adopted):
        super().__init__(name,age,gender,breed , id, adopted)

    def make_sound(self):
        print("Squeak squeak")