class Weapons:
    def __init__(self,damage,cooldown,cost,name):
        self.damage=damage
        self.cooldown=cooldown
        self.cost=cost
        self.name=name

class Swords(Weapons):
    def __init__ (self,damage,cooldown,cost,name):
        super().__init__(damage,cooldown,cost,name)
    def info(self):
        print(self.name,":\nThis sword has {} damage, {} cooldown. Cost is {}.".format(self.damage,self.cooldown,self.cost))

class Wands(Weapons):
    def __init__(self, damage, cooldown, cost,name,):
        super().__init__(damage, cooldown, cost,name)


    def info(self):
        print(self.name,":\nThis wand has {} damage, {} cooldown. Cost is {}.".format(self.damage,self.cooldown,self.cost))

class Hero:
    def __init__ (self,hero_health=100, hero_money=20, item=None , item2=None):
        self.max_health = hero_health
        self.hero_health=hero_health
        self.hero_money=hero_money
        self.weapon = item
        self.armor = item2
        self.key = True

        if item:
            self.hero_damage = item.damage
            self.hero_cooldown = item.cooldown
        else:
            self.hero_damage = 0
            self.hero_cooldown = 5

        if item2:
            self.max_health += item2.health
            self.hero_health = self.max_health
        else:
            pass



    

    def changeWeapon(self, new_weapon):
        self.weapon = new_weapon
        self.hero_damage = new_weapon.damage

    def changeMoney(self, new_money):
        self.hero_money=new_money
    
    def changeArmor(self, new_armor):
        if self.armor:
            self.max_health -= self.armor.armor_health
            self.max_health += new_armor.armor_health
            self.hero_health = self.max_health
            self.armor = new_armor
        else:
            self.max_health += new_armor.armor_health
            self.hero_health = self.max_health
            self.armor = new_armor
    

    def weaponInfo(self):
        print("Weapon damage: ", self.weapon.damage, "Weapon cooldown: ", self.weapon.cooldown)

    def __str__(self):
        str1 = "Hero health:" + str(self.hero_health) + "\n"
        str1 += "Hero money:" + str(self.hero_money) + "\n"
        str1 += "Hero weapon:" + str(self.weapon.name) + "\n"

        return str1
    


class mobs:
    def __init__(self,mob_name,mob_health,mob_damage,mob_cooldown,mob_money):
        self.mob_health=mob_health
        self.mob_damage=mob_damage
        self.mob_cooldown=mob_cooldown
        self.mob_name=mob_name
        self.mob_money=mob_money

class Armors:
    def __init__(self,armor_name,armor_health,armor_cost):
        self.armor_name=armor_name
        self.armor_health=armor_health
        self.armor_cost=armor_cost
    def info(self):
        print(self.armor_name,":\nThis armor increases your max health by {}, Cost is {}.".format(self.armor_health,self.armor_cost))
