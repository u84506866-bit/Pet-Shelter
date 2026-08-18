import animals
import people
import shelter

from decorators import introduction

class Main:

    def __init__(self):

        self. shelter = shelter
        self.__animal_list = list()
        self.__person_list = list()

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
            self.main_menu()

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
        # self.Shelter.add_animal()
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

    def show_adopted_animals(self):
        pass

        self.main_menu()

if __name__ == "__main__":

    Main()