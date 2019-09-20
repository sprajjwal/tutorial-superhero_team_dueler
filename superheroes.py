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
        self.deaths = 0
        self.kills = 0

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
        if not self.is_alive():
            return 0
        return block

    def take_damage(self, damage):
        self.current_health -= damage

    def is_alive(self):
        return self.current_health > 0

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        self.deaths += num_deaths

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
            self.add_kill(1)
            opponent.add_deaths(1)
        else:
            print(f"{opponent.name} won!")
            self.add_deaths(1)
            opponent.add_kill(1)

class Weapon(Ability):
    def attack(self):
        return random.randint(self.max_damage//2, self.max_damage)

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
        return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        self.heroes.append(hero)

    @staticmethod
    def is_team_alive(self):
        ''' Helper function to check if everyone on team is alive '''
        for hero in self.heroes:
            if not hero.is_alive():
                return False
        return True

    @staticmethod
    def get_random_fighter(self):
        if not self.is_team_alive(self): 
            return 0
        else: 
            fighter = random.choice(self.heroes)
            if not fighter.is_alive():
                fighter = self.get_random_fighter(self)
            return fighter

    def attack(self, other_team):
        dead = 0 # dead = 1 => self is dead | dead = 2 => other_team is dead
        while dead == 0:
            self_fighter = self.get_random_fighter(self)
            other_team_fighter = other_team.get_random_fighter(other_team)
            self_fighter.fight(other_team_fighter)
            if self.is_team_alive(self):
                dead = 1
            elif other_team.is_team_alive(other_team):
                dead = 2

    def revive_heroes(self, health = 100):
        for hero in self.heroes:
            hero.current_health = health

    def stats(self):
        for hero in self.heroes:
            ratio = hero.kills/hero.deaths
            print(f"{hero.name}'s K/D ratio is: {ratio}'")

if __name__ == "__main__":
    team1 = Team("One")
    jodie = Hero("Jodie Foster")
    ab =Ability("eat ass", 200)
    jodie.add_ability(ab)
    team1.add_hero(jodie)

    team2 = Team("Two")
    ww = Hero("Wonder Woman")
    team2.add_hero(ww)

    team1.heroes[0].fight(team2.heroes[0])
    print(jodie.is_alive())
    print(jodie.kills)

    print(ww.is_alive())
    print(ww.kills)
    print(ww.deaths)