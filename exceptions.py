import main

class AnimalNotFoundError():
    print("The Animal Was Not Found!")
    main.Main.user_menu()

class DuplicateAnimalMethod():
    print("Duplication Error!")
    main.Main.manager_menu()

class AnimalAlreadyAdoptedError():
    print("Sorry the Animal is Already Adopted! ")
    main.Main.user_menu()

class MaximumAdoptionReachedError():
    print("Maximum Adoption limit is 9 and you have surpassed the limit!")
    main.Main.user_menu()