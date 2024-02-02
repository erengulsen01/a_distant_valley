from classes import Swords, Wands, Weapons, Hero , mobs
import os , time
import random

print("A distant valley game")

Wooden_sword = Swords(damage="5-10",cooldown=5,cost=20,name="Wooden sword")

Silver_sword = Swords(damage="10-20",cooldown=4,cost=50,name="Silver_sword")
Golden_sword = Swords(damage="30-50",cooldown=3,cost=200,name="Golden_sword")
Full_moon_sword = Swords(damage=100,cooldown=1,cost=1000,name="Full_moon_sword")

fists = Weapons(1, 5, 0, "fists")

wooden_stick = Wands(damage="0,20",cooldown=10,cost=50,name="Wooden stick")
classic_wand = Wands("10,50",3,100,"Classic wand")
harry_potter_wand = Wands("100-500",5,1000,"Harry Potter wand")

hero1 = Hero(item=fists, hero_money=200)



class Episodes():
    def __init__ (self,name,level,):
        self.name=name
        self.level=level


def episode(mob_list):
    os.system('cls||clear')
    for _ in range(random.randint(1,3)):
        idx = random.randint(0, len(mob_list)-1)
        mob = mobs_list[idx]
        print("There is a", mobs_list[idx].mob_name,"!")
        input("Start to fight")
        mob_time = 0
        player_time = 0
        os.system('cls||clear')
        print("Your health:",hero1.hero_health," "*120,"Enemy health:", mobs_list[idx].mob_health)
        while hero1.hero_health > 0 and mob.mob_health > 0:
            mob_time -= time.time()
            player_time -= time.time()
            
            time.sleep(0.01)

            player_time += time.time()
            if player_time >= hero1.weapon.cooldown:
                time1 = time.time()
                # attack = input("Write attack to attack!:")
                time2 = time.time()
                mob_time -= (time2 - time1)
                player_time -= (time2 - time1)
                dmg = 0
                if type(hero1.hero_damage) == str:
                    dmg0, dmg1 = [int(i) for i in hero1.hero_damage.split("-")]
                    dmg = random.randint(dmg0, dmg1)
                    mob.mob_health -= dmg
                else:
                    dmg = hero1.hero_damage
                    mob.mob_health -= dmg
                print("You hit with", dmg)
                time.sleep(1.5)
                os.system('cls||clear')
                print("Your health:",hero1.hero_health," "*120,"Enemy health:", mobs_list[idx].mob_health)
                player_time = 0
            
            mob_time += time.time()
            if mob_time >= mob.mob_cooldown:
                hero1.hero_health -= mob.mob_damage
                print(mob.mob_name, "hit with", mob.mob_damage)
                time.sleep(1.5)
                os.system('cls||clear')
                print("Your health:",hero1.hero_health," "*120,"Enemy health:", mobs_list[idx].mob_health)
                mob_time = 0
        
        if hero1.hero_health <= 0:
            print("You died.")
        
        if mob.mob_health <= 0:
            print("Mob died.")
            gain=random.randint(2,5)
            print("You won", gain,"gold.")
            hero1.changeMoney(hero1.hero_money+gain)
            time.sleep(1.5)

def shop():
    value = 70
    print("-"*value,"SHOP", "-"*value, "\nSwords:", " "*(value*2-12), "Money:", hero1.hero_money)
    swords = [Wooden_sword, Silver_sword, Golden_sword]
    for i in range(3):
        print(i+1, end=". ")
        swords[i].info()

    print("Wands:")
    wands = [wooden_stick,classic_wand,harry_potter_wand]
    for i in range (4,7):
        print(i, end=".")
        wands[i-4].info()
    print("7. Health potion, cost: 5 (Restores health completely.)")
    print("8.Exit")

    x=int(input("Choice:"))

    if x < 4:
        if hero1.weapon.name == swords[x-1].name:
            os.system('cls||clear')
            print("You already have one.")
            input()
        else:
            if hero1.hero_money >= swords[x-1].cost:
                hero1.changeWeapon(swords[x-1])
                hero1.changeMoney(hero1.hero_money-swords[x-1].cost)
                os.system('cls||clear')
                print("You bought", hero1.weapon.name)
                input()
            else:
                os.system('cls||clear')
                print("You don't have enough money")
                input()

    elif 3<x<7:
        if hero1.weapon.name == wands[x-4].name:
            os.system('cls||clear')
            print("You already have one.")
            input()
        else:
            if hero1.hero_money >= wands[x-4].cost:
                print(wands[x-4].name)
                hero1.changeWeapon(wands[x-4])
                hero1.changeMoney(hero1.hero_money-wands[x-4].cost)
                os.system('cls||clear')
                print("You bought", hero1.weapon.name)
                input()
                
            else:
                os.system('cls||clear')
                print("You don't have enough money")
                input()
    elif x == 7:
        hero1.hero_health = hero1.max_health
        hero1.changeMoney(hero1.hero_money-5)
    else:
        pass

    return x



os.system('cls||clear')
input("Welcome to a new advanture game 'A Distant Valley'. Press enter to start.")
os.system('cls||clear')
input("You were a marauder who lived alone. However your life changed after you met a girl. While you are about to get married, King Jeffry kidnaps the girl and you go on an adventure to save the girl.\nPress enter to continue.")
os.system('cls||clear')

while True:
    try:
        main_menu=int(input("1.Inventory\n2.Shop\n3.Map\nChoice:"))
    except Exception as e:
        os.system('cls||clear')
        main_menu=0

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

            if v == 8:
                os.system('cls||clear')
                break

    elif main_menu == 3:
        os.system('cls||clear')
        input("Gameplay:\nThere are 4 maps. Improve yourself in the maps you can and enter the castle by obtaining the castle badge found on the knights in the 3th map named Town Center.\nWrite attack to attack mobs. You can attack only when your cooldown is up.\nPress enter to continue.")
        os.system('cls||clear')
        map_choice=int(input("MAPS\n1.The Dark Swamp\n2.The Enchanted Forest\n3.Town Center\n4.The Castle\nChoice: "))


        if map_choice == 1:
            giant_fly=mobs(mob_name="Giant fly",mob_health=50,mob_damage=random.randint(1, 5),mob_cooldown=2)
            scorpion=mobs(mob_name="Scorpion",mob_health=75,mob_damage=random.randint(1, 10),mob_cooldown=2)
            mobs_list = [giant_fly,scorpion]
            episode(mobs_list)
