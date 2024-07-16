from pet import Pet


if __name__ == '__main__':
    name = input("What is the name of your pet? Write here: ")
    pet = Pet(name)
    print(pet.name)
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
            print("Goodbye!")
            break
        else:
            print("Fuck off moron!")
        pet.random_event()
