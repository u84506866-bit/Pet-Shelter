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
    def  authentication(self):

        choice = input("👋 Welcome! Please select your role: \n1. 🖆Shelter Manager\n2.👤 Adopter\n3.✖️Exit Program\nEnter choice: ")

        match choice:

            case 1:

                username = str(input("Enter Your Username: "))
                password = str(input("Enter Your password:  "))

                if username == "admin" and password == "1234":
                    self.manager_menu()

            case 2:

                try:
                    choice_ = int(input("1. Login\n2. Signup"))
                except:
                    print("not a number!")
                    self.authentication()
                    
                match choice_:

                    case 1:

                        introduction(header="Login", Symbol="🖑")
                        name = input("Please Enter Your Name: ")
                        phone_number = input("Please Enter Your Phone: ")
                        
                        for person in self.__person_list:
                            if person.name == name:
                                if person.phone == phone_number:

                                    print("\n✅ Signup was successful!")
                                    self.user_menu()
                                    break

                        print ("⛔No Person Was Found!")
                        self.authentication()

                    case 2:

                      try:

                        introduction(header="Signup", Symbol="🖑")

                        name = str(input("✒️ Enter Your Name:"))

                        phone = str(input("☎️Enter Your Phone Number: "))

                        national_id = str(input("🪪 Enter Your National ID: "))
                        
                        person = Adopter(name = name, phone=phone, national_id=national_id)

                        self.__person_list.append(person)

                      except:

                        print("There is a mismatch type in your data! please try again with correct data")                        
                        self.authentication()
                            
                        print("\n✅ Signup was successful!")

                    case _:
                        print("❌ Irrelevent Option!")

    @bold_introduction(header="Management System",Symbol="🖆")
    def manager_menu(self):

            try:
                choice = int(input("What you want to do?\n1. Add Animal\n2. Show Animals\n3. Exit"))
            except:
                print("not a number!")
                self.manager_menu

            match choice:

                case 1:
                    self.add_animal()

                case 2:
                    self.show_animals()

                case _:
                    print("❌ Irrelevent option!")
                    self.manager_menu()

    @bold_introduction(header="Adoption System", Symbol="👤")
    def user_menu(self):
        
        print("What you want to do?\n1. Search Animal\n2. Adopting Animal\n3. Return Animal\n4. Show Available Animals\n5. Show Adopted Animals\n6. Exit ")

        try:

            choice = int(input("\nEnter Choice: "))

            while choice not in range(1,8):
                choice = int(input("⚠️ Invalid Option Please Try Again: "))

        except:
            
            print("❌ Error! You Didn't Enter a Number!")
            return self.user_menu()
            

        match choice:

            case  1:
                self.show_animals()

            case 2:
                self.search_animal()

            case 3:
                self.adopt_animal()

            case 4:
                self.return_animal()

            case 5:
                self.show_available_animals()

            case 6:
                self.show_adopted_animals()

            case 7:
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
            return self.manager_menu()
            

        self.id += 1  

        if gender.lower() not in ["male","female"]:
            print("Invalid Gender!!")
            self.user_menu()


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
                        return self.user_menu()
                        
        self.shelter.add_animal(self.animal)
        # self.__animals_list.append(self.animal)    
        self.manager_menu()

    @introduction(header="Showing All Animals",Symbol="🐾")
    def show_animals(self):
        self.shelter.show_animals()
        self.user_menu()

    @introduction(header="Searching Animal", Symbol="🐾")
    def search_animal(self):

        try:
            name_ = str(input())
            self.shelter.search_animal(name_)
        except:
            print("An Error has Occured!")   
        
        self.user_menu()

    @introduction(header="Animal Adoption", Symbol="🐾")    
    def adopt_animal(self, person, animal):

        self.shelter.adopt_animal([animal,person])

        self.user_menu()


    @introduction(header="Return Animal to Shelter", Symbol="🐾")
    def return_animal(self,id):

        self.shelter.returning_animal(id)

        self.user_menu()

    @introduction(header="Showing All Available Animals", Symbol="🐾")
    def show_available_animals(self):
        
        self.shelter.show_animals()
        
        self.user_menu()

    @introduction(header="Show Adopted Animals", Symbol="🐾")
    def show_adopted_animals(self):
        
        self.shelter.show_animals_adopted()
        
        self.user_menu()

if __name__ == "__main__":

    Main()