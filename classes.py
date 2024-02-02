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

class Enemys:
    def __init__ (self, health,damage,cooldown):
        self.damage=damage
        self.health=health
        self.cooldown=cooldown

class Hero:
    def __init__ (self,hero_health=100, hero_money=20, item=None):
        self.max_health = hero_health
        self.hero_health=hero_health
        self.hero_money=hero_money
        self.weapon = item

        if item:
            self.hero_damage = item.damage
            self.hero_cooldown = item.cooldown
        else:
            self.hero_damage = 0
            self.hero_cooldown = 0

    

    def changeWeapon(self, new_weapon):
        self.weapon = new_weapon
        self.hero_damage = new_weapon.damage

    def changeMoney(self, new_money):
        self.hero_money=new_money
    

    def weaponInfo(self):
        print("Weapon damage: ", self.weapon.damage, "Weapon cooldown: ", self.weapon.cooldown)

    def __str__(self):
        str1 = "Hero health:" + str(self.hero_health) + "\n"
        str1 += "Hero money:" + str(self.hero_money) + "\n"
        str1 += "Hero weapon:" + str(self.weapon.name) + "\n"

        return str1
    


class mobs:
    def __init__(self,mob_name,mob_health,mob_damage,mob_cooldown):
        self.mob_health=mob_health
        self.mob_damage=mob_damage
        self.mob_cooldown=mob_cooldown
        self.mob_name=mob_name