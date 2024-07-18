from pet import Pet
from db import DatabaseManager


if __name__ == '__main__':
    database = DatabaseManager()

    name = input("What is the name of your pet? Write here: ")
    pet = Pet(name) # pet "arya, 50, 50, 50"
    pet = database.load_pet(pet) # arya, 65, 70, 85

    while True:
        print("1. Feed your pet")
        print("2. Play with your pet")
        print("3. Groom your pet")
        print("4. Exit")
        choice = int(input("Choose an action: "))
        if choice == 1:
            pet.feed()
        elif choice == 2:
            pet.play()
        elif choice == 3:
            pet.clean()
        elif choice == 4:
            database.save_pet(pet)
            print("Goodbye!")
            database.close()
            break

        else:
            print("Fuck off moron!")
        pet.random_event()
