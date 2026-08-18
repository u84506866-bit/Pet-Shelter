from animals import Dog, Cat, Bird, Rabbit
from people import Adopter
from shelter import Shelter

from decorators import introduction

class Main:

    def __init__(self):

        self. shelter = Shelter()
        self.__animal_list = list()
        self.__person_list = list()

        self.id = 0

        self.main_menu()


    def main_menu(self):

        print("=======================================\n  🐾 Welcome to Animal Shelter CLI 🐾\n=======================================\n")
        
        print("What you want to do?\n1. Add Animal\n2. Show Animals\n3. Search Animal\n4. Adopting Animal\n5. Return Animal\n6. Show Available Animals\n7. Show Adopted Animals\n8. Exit ")

        try:

            choice = int(input("\nEnter Choice: "))

            while choice not in range(1,9):
                choice = int(input("⚠️ Invalid Option Please Try Again: "))

        except ValueError:
            
            print("❌ Error! You Didn't Enter a Number!")
            return self.main_menu()
            

        match choice:

            case 1:
                self.add_animal()

            case 2:
                self.show_animals()

            case 3:
                self.search_animal()

            case 4:
                self.adopt_animal()

            case 5:
                self.return_animal()

            case 6:
                self.show_available_animals()

            case 7:
                self.show_adopted_animals()

            case 8:
                exit()

    @introduction("Adding Animal")
    def add_animal(self):
        try :
            breed = str(input("Enter animal's breed:(Dog, Cat, Bird, Rabbit)"))
            name = str(input("Enter animal's name: "))
            age = int(input("Enter animal's age: "))
            gender = str(input("Enter animal's gender: (Female, Male)"))
        except:
            print("an Error has occured! Please try again...")
            return self.add_animal()
            

        self.id += 1  

        match breed.lower():

            case "dog":
                self.animal = Dog(name=name, age= age, gender= gender, breed= "Dog", id= self.id)

            case "cat":
                self.animal = Cat(name= name, age= age, gender= gender, breed= "Cat", id= self.id)

            case "bird":
                self.animal = Bird(name= name, age= age, gender= gender, breed= "Bird", id= self.id)

            case "rabbit":
                self.animal = Rabbit(name= name, age= age, gender= gender, breed= "Rabbit", id= self.id)

            case _:
                        print("⚠️ Unknown breed.")
                        return self.add_animal()

        self.add_animal(self.animal)    
        self.main_menu()

    @introduction("Showing All Animals")
    def show_animals(self,  animals_list):
        pass

        self.main_menu()

    @introduction("Searching Animal")
    def search_animal(self, name):
        pass

        self.main_menu()

    @introduction("Animal Adoption")    
    def adopt_animal(self,name,id):

        pass

        self.main_menu()


    @introduction("Return Animal to Shelter")
    def return_animal(self):
        pass

        self.main_menu()

    @introduction("Showing All Available Animals")
    def show_available_animals(self):
        pass

        self.main_menu()

    @introduction("Show Adopted Animals")
    def show_adopted_animals(self):
        pass

        self.main_menu()

if __name__ == "__main__":

    Main()