import random
import os
from classes import Swords, Wands, Weapons, Hero




class mobs:
    def __init__(self,mob_name,mob_health,mob_damage,mob_cooldown):
        self.mob_health=mob_health
        self.mob_damage=mob_damage
        self.mob_cooldown=mob_cooldown
        self.mob_name=mob_name

















os.system('cls||clear')
input("Gameplay:\nThere are 4 maps. Improve yourself in the maps you can and enter the castle by obtaining the castle badge found on the knights in the 3th map named Town Center.\nWrite attack to attack mobs. You can attack only when your cooldown is up.\nPress enter to continue.")
os.system('cls||clear')
map_choice=int(input("MAPS\n1.The Dark Swamp\n2.The Enchanted Forest\n3.Town Center\n4.The Castle\nChoice: "))






if map_choice == 1:
    input("There are three mobs in the The Dark Swamp.")
    for i in range(random.randint(3,5)):
        giant_fly=mobs(mob_name="Giant fly",mob_health=25,mob_damage=random.randint(5, 10),mob_cooldown=5)
        scorpion=mobs(mob_name="Scorpion",mob_health=40,mob_damage=random.randint(5, 20),mob_cooldown=5)
    
        mobs_list = [giant_fly,scorpion]
        idx = random.randint(0, 1)
        print("There is a", mobs_list[idx].mob_name,"!")
        input("Start to fight")
        print("Your health:",hero1.hero_health," "*50,"Enemy health:",mobs_list[idx].mob_health)


