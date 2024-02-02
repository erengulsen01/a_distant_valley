from main import shop, hero1
import os 


os.system('cls||clear')
input("Welcome to a new advanture game 'A Distant Valley'. Press enter to start.")
os.system('cls||clear')
input("You were a marauder who lived alone. However your life changed after you met a girl. While you are about to get married, King Jeffry kidnaps the girl and you go on an adventure to save the girl.\nPress enter to continue.")
os.system('cls||clear')

while True:
    main_menu=int(input("1.Inventory\n2.Shop\n3.Map\nChoice:"))
    if main_menu == 1:
        os.system('cls||clear')
        print(hero1)
        input("Press enter to exit")
        os.system('cls||clear')
        continue



    elif main_menu == 2:
        os.system('cls||clear')
        while main_menu ==2:
            os.system('cls||clear')
            v = shop()

            if v == 7:
                os.system('cls||clear')
                break

    elif main_menu == 3:
        pass

    else:
        print("Invalid choice. Please try again.")

