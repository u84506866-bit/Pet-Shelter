import animals
import people
import shelter


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
                add_animal()

            case 2:
                show_animals()

            case 3:
                search_animal()

            case 4:
                adopt_animal()

            case 5:
                return_animal()

            case 6:
                show_available_animals()

            case 7:
                show_adopted_animals()

            case 8:
                exit()


        def add_animal(self):
            self.Shelter.append

        def show_animals(self,  animals_list):
            pass

        def search_animal(self, name):
            pass

        def adopt_animal(self,name,id):
            pass

        def return_animal(self):
            pass

        def show_available_animals(self):
            pass

        def show_adopted_animals(self):
            pass 

if __name__ == "__main__":

    Main()