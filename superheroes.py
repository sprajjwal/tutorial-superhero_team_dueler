import random

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.max_damage = attack_strength

    def attack(self):
        return random.randint(0, self.max_damage)

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        return random.randint(0, self.max_block)

class Hero:
    def __init__(self, name, starting_health = 100):
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        damage = 0
        for ability in self.abilities:
            damage += ability.attack()
        return damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self, damage_amt):
        block = 0
        for armor in self.armors:
            block += armor.block()
        return block

    def take_damage(self, damage):
        self.current_health -= damage

    def is_alive(self):
        return self.current_health > 0

    #helper function for fight
    @staticmethod
    def fighting(self, opponent):
        opponent.take_damage(self.attack())
        if not self.is_alive() or not opponent.is_alive():
            return
        self.fighting(opponent, self)

    def fight(self, opponent):
        self.fighting(self, opponent)
        if self.is_alive():
            print(f"{self.name} won!")
        else:
            print(f"{opponent.name} won!")

class Weapon(Ability):
    def attack(self):
        return random.randint(0, self.max_damage)

class Team:
    heros = []
    def __init__(self, name, heros):
        self.name = name
        for hero in heros:
            self.heros.append(hero)
    def remove_hero(self, name):
        if name in self.
            self.heros.remove(name)
        
    def show_heros(self):
        print(self.heros[0].name, '\n',self.heros[1].name)


if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    # ability1 = Ability("Super Speed", 300)
    # ability2 = Ability("Super Eyes", 130)
    # ability3 = Ability("Wizard Wand", 80)
    # ability4 = Ability("Wizard Beard", 20)
    # hero1.add_ability(ability1)
    # hero1.add_ability(ability2)
    # hero2.add_ability(ability3)
    # hero2.add_ability(ability4)
    # hero1.fight(hero2)

    team1 = Team("Team A", [hero1, hero2])
    team1.show_heros()