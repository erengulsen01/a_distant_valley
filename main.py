from classes import Swords, Wands, Weapons, Hero , mobs , Armors
import os , time
import random

print("A distant valley game")

Wooden_sword = Swords(damage="5-10",cooldown=5,cost=20,name="Wooden sword")

golden_sword = Swords(damage="50-100",cooldown=3,cost=150,name="Silver_sword")
Full_moon_sword = Swords(damage="200-400",cooldown=2,cost=1000,name="Full moon sword")

fists = Weapons(1, 5, 0, "fists")

wooden_stick = Wands(damage="0-20",cooldown=7,cost=50,name="Wooden stick")
classic_wand = Wands("50-300",5,100,"Classic wand")
harry_potter_wand = Wands("400-1000",3,1000,"Harry Potter wand")

hero1 = Hero(item=fists)
wooden_armor = Armors("Wooden armor",100,250)
golden_armor = Armors("Golden armor",300,500)
holy_armor=Armors("Armor blessed by the gods",500,1000)



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
            input("You died.\nPress enter.")
            
        
        if mob.mob_health <= 0:
            print("Mob died.")
            print("You won",mobs_list[idx].mob_money,"gold.")
            hero1.changeMoney(hero1.hero_money+mobs_list[idx].mob_money)
            time.sleep(1.5)

def shop():
    value = 70
    print("-"*value,"SHOP", "-"*value, "\nSwords:", " "*(value*2-12), "Money:", hero1.hero_money)
    swords = [Wooden_sword, golden_sword,Full_moon_sword]
    for i in range(3):
        print(i+1, end=". ")
        swords[i].info()

    print("Wands:")
    wands = [wooden_stick,classic_wand,harry_potter_wand]
    for i in range (4,7):
        print(i, end=".")
        wands[i-4].info()

    print("Armors:")
    armors=[wooden_armor,golden_armor,holy_armor]
    for i in range (7,10):
        print(i, end=".")
        armors[i-7].info()
    print("10. Health potion:\n Restores health completely. Cost is 10 gold.")
    print("11.Exit")

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


    elif 6<x<10:
        if hero1.hero_money >= armors[x-7].armor_cost:
            hero1.changeArmor(armors[x-7])
            hero1.changeMoney(armors[x-7].armor_cost)
            os.system('cls||clear')
            print("You bought", hero1.armor.armor_name)
            input()
    elif x == 10:
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
    os.system('cls||clear')
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

            if v == 11:
                os.system('cls||clear')
                break

    elif main_menu == 3:
        os.system('cls||clear')
        input("Gameplay:\nThere are 4 maps. Improve yourself in the maps you can and enter the castle by obtaining the castle badge found on the knights in the 3th map named Town Center.\nWhen you start a fight, indefinite number of mobs will attack you in turn.If you killed one, you move to another. \nPress enter to continue.")
        os.system('cls||clear')
        try:
            map_choice=int(input("MAPS\n1.The Dark Swamp\n2.The Enchanted Forest\n3.Town Center\n4.The Castle\nChoice: "))
        except Exception as e:
            os.system('cls||clear')
            continue


        if map_choice == 1:
            giant_fly=mobs(mob_name="Giant fly",mob_health=10,mob_damage=random.randint(1, 10),mob_cooldown=4,mob_money=random.randint(30,50))
            scorpion=mobs(mob_name="Scorpion",mob_health=15,mob_damage=random.randint(1, 10),mob_cooldown=4,mob_money=random.randint(20,40))
            mobs_list = [giant_fly,scorpion]
            episode(mobs_list)

        elif map_choice == 2:
            forest_spirit=mobs(mob_name="Forest Spirit",mob_health=50,mob_damage=random.randint(10,30),mob_cooldown=4,mob_money=random.randint(40,80))
            wild_wolf=mobs(mob_name="Wild Wolf",mob_health=100,mob_damage=random.randint(10,40),mob_cooldown=4,mob_money=random.randint(40,80))
            mobs_list = [forest_spirit,wild_wolf]
            episode(mobs_list)

        elif map_choice== 3:
            os.system('cls||clear')
            for _ in range(random.randint(1,3)):
                knight=mobs(mob_name="Knight",mob_health=200,mob_damage=random.randint(40,60),mob_cooldown=2,mob_money=random.randint(100,150))
                assasin=mobs(mob_name="Assasin",mob_health=300,mob_damage=random.randint(50,60),mob_cooldown=2,mob_money=random.randint(100,200))
                mob_list=[knight,assasin]
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
                    input()
                
                if mob.mob_health <= 0:
                    print("Mob died.")
                    value = random.random()
                    
                    if random.choices([True, False], [0.1, 0.9])[0]:
                        print("You obtained key.")
                        hero1.key=True
                    else:
                        pass
                    print("You won",mobs_list[idx].mob_money,"gold.")
                    hero1.changeMoney(hero1.hero_money+mobs_list[idx].mob_money)
                    time.sleep(1.5)
        if map_choice == 4:
            if hero1.key== False:
                print("You have to find a castle badge")
            if hero1.key ==True:
                king_jeff=mobs("King Jeffry",1000,random.randint(100,150),2,None)
                os.system('cls||clear')
                input("-Where is my wife?\nPress enter")
                os.system('cls||clear')
                input("King Jeffry:\nShe is here with me. She wants to stay here\nPress enter")
                os.system('cls||clear')
                input("-You are lying!\nPress enter")
                os.system('cls||clear')
                input("Lille:\nHe is right.\nHe did not kidnapped me. I want it.\nPress enter")
                os.system('cls||clear')
                input("What...?\nPress enter")
                os.system('cls||clear')
                input("Start to fight")
                mob_time = 0
                player_time = 0
                os.system('cls||clear')
                print("Your health:",hero1.hero_health," "*120,"Enemy health:", king_jeff.mob_health)
                while hero1.hero_health > 0 and king_jeff.mob_health > 0:
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
                            king_jeff.mob_health -= dmg
                        else:
                            dmg = hero1.hero_damage
                            king_jeff.mob_health -= dmg
                        print("You hit with", dmg)
                        time.sleep(1.5)
                        os.system('cls||clear')
                        print("Your health:",hero1.hero_health," "*120,"Enemy health:", king_jeff.mob_health)
                        player_time = 0
                    
                    mob_time += time.time()
                    if mob_time >= king_jeff.mob_cooldown:
                        hero1.hero_health -= king_jeff.mob_damage
                        print(king_jeff.mob_name, "hit with", king_jeff.mob_damage)
                        time.sleep(1.5)
                        os.system('cls||clear')
                        print("Your health:",hero1.hero_health," "*120,"Enemy health:", king_jeff.mob_health)
                        mob_time = 0
                
                if hero1.hero_health <= 0:
                    print("You died.")
                    input()
                    os.system('cls||clear')
                
                if king_jeff.mob_health <= 0:
                    input("You killed King Jeffry.\nPress enter.")
                    os.system('cls||clear')
                    input("Lillie:\nI am sorry.\nPress enter.")
                    os.system('cls||clear')
                    end=int(input("1.Kill Lillie\n2.Leave"))
                    if end == 1:
                        input("You killed Lillie.")
                    if end ==2:
                        input("You left the castle.")
                    print("Game over. Thanks for playing.")
    else:
        continue

                    

                

            
        



