from animals import Animal
from exceptions import Exception

class Shelter:

    def __init__(self):

        self.__animal_list = list()
        self.__adopted_animals = list()

    def add_animal(self, Animal):

        self.__animal_list.append(Animal)

    def remove_animal(self,name):

        for animal in self.__animal_list:

            if animal.name == name:
                self.__animal_list.remove(animal)

    
    def search_animal(self, name):

        for animal in self.__animal_list:
            if animal.name == name:
                print(f"{animal.name}: {animal.age} {animal.gender} {animal.breed}")



    def show_animals(self):

        for index in self.__animal_list:
            print (f"{index.name}: {index.gender} {index.age} {index.breed}")


    def adopt_animal(self, Animal, Adopter):
         # here i will take the person name and then turn the animal.adopted true and then append it to the adopted animals list
         if Animal.adopted == False:
            if Adopter.adopted_animals:
                self.__adopted_animals.append([Animal,Adopter])
                Animal.adopted = True

            else:
                Exception.MaximumAdoptionReachedError()

         else:
            Exception.AnimalAlreadyAdoptedError()

        
    def returning_animal(self):
        pass


    def  show_animals_adopted(self):
        pass
