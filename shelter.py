from animals import Animal


class Shelter:

    def __init__(self):

        self.__animal_list = list()

    def add_animal(self, Animal):

        self.__animal_list.append(Animal)

    def remove_animal(self,name):

        for animal in self.__animal_list:

            if animal.name == name:
                self.__animal_list.remove(animal)

    
    def search_animal(self, name):

        new_lst = list()

        for animal in self.__animal_list:
            if animal.name = name:
                new_lst.append(animal)


    def show_animals(self):

        for index in self.__animal_list:
            print (f"{index.name}: {index.gender} {index.age} {index.breed}")
