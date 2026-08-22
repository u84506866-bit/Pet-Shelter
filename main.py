from animals import Dog, Cat, Bird, Rabbit
from people import Adopter
from shelter import Shelter

from decorators import introduction, bold_introduction

class Main:

    def __init__(self):

        self.shelter = Shelter()
        self.__person_list = list()

        self.id = 0

        self.authentication()

    @bold_introduction(header="Authentication",Symbol="🫆")
    def  authentication():

        choice = input("👋 Welcome! Please select your role: \n1. Shelter Manager\n2. Adopter\n3.Exit Program\nEnter choice: ")

        match choice:

            case 1:

                username = str(input("Enter Your Username: "))
                password = str(input("Enter Your Password:  "))

                if username == "admin" and password == "1234":
                    self.manager_menu()

            case 2:
                self.user_menu()

    @bold_introduction(header="Management System",Symbol="👑")
    def manager_menu(self):

            choice = input("What you want to do?\n1. Add Animal\n2. Show Animals\n3. Exit")

            match choice:

                case 1:
                    self.add_animal()

                case 2:
                    self.show_animals()

    @bold_introduction(header="Adoption System", Symbol="👤")
    def user_menu(self):
        
        print("What you want to do?\n1. Search Animal\n2. Adopting Animal\n3. Return Animal\n4. Show Available Animals\n5. Show Adopted Animals\n6. Exit ")

        try:

            choice = int(input("\nEnter Choice: "))

            while choice not in range(1,9):
                choice = int(input("⚠️ Invalid Option Please Try Again: "))

        except ValueError:
            
            print("❌ Error! You Didn't Enter a Number!")
            return self.main_menu()
            

        match choice:

            case 1:
                self.search_animal()

            case 2:
                self.adopt_animal()

            case 3:
                self.return_animal()

            case 4:
                self.show_available_animals()

            case 5:
                self.show_adopted_animals()

            case 6:
                exit()

    @introduction(header="Adding Animal", Symbol="🐾")
    def add_animal(self):
        try :
            breed = str(input("Enter animal's breed(Dog, Cat, Bird, Rabbit): "))
            name = str(input("Enter animal's name: "))
            age = int(input("Enter animal's age: "))
            gender = str(input("Enter animal's gender(Female, Male): "))


            
        except:
            print("an Error has occured! Please try again...")
            return self.main_menu()
            

        self.id += 1  

        if gender.lower() not in ["male","female"]:
            print("Invalid Gender!!")
            self.main_menu()


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
                        return self.main_menu()
                        
        self.shelter.add_animal(self.animal)
        # self.__animals_list.append(self.animal)    
        self.manager_menu()

    @introduction(header="Showing All Animals",Symbol="🐾")
    def show_animals(self):
        self.shelter.show_animals()
        self.main_menu()

    @introduction(header="Searching Animal", Symbol="🐾")
    def search_animal(self):

        try:
            name_ = str(input())
            self.shelter.search_animal(name_)
        except:
            print("An Error has Occured!")   
        
        self.main_menu()

    @introduction(header="Animal Adoption", Symbol="🐾")    
    def adopt_animal(self,name,id):

        pass
        # not implemented
        self.main_menu()


    @introduction(header="Return Animal to Shelter", Symbol="🐾")
    def return_animal(self):
        pass
        # not implemented
        self.main_menu()

    @introduction(header="Showing All Available Animals", Symbol="🐾")
    def show_available_animals(self):
        pass
        #not implemented
        self.main_menu()

    @introduction(header="Show Adopted Animals", Symbol="🐾")
    def show_adopted_animals(self):
        pass
        # not implemented
        self.main_menu()

if __name__ == "__main__":

    Main()