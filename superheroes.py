import random
import os

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.max_damage = attack_strength

    def attack(self):
        ''' returns damage an ability does '''
        return random.randint(0, self.max_damage)

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        ''' returns damage a hero can block based of their armor '''
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
        ''' add ability to a hero'''
        self.abilities.append(ability)

    def attack(self):
        ''' returns how much damage a hero can do '''
        damage = 0
        for ability in self.abilities:
            damage += ability.attack()
        return damage

    def add_armor(self, armor):
        ''' add armor to list of armors for a hero'''
        self.armors.append(armor)

    def defend(self, damage_amt):
        ''' returns how much damage a hero blocks based on armor'''
        if not self.is_alive():
            return 0
        block = 0
        for armor in self.armors:
            block += armor.block()
        return block

    def take_damage(self, damage):
        ''' does damage to a hero's current health '''
        self.current_health -= damage - self.defend(damage)

    def is_alive(self):
        ''' checks if a hero is alive '''
        return self.current_health > 0

    def add_kill(self, num_kills):
        ''' adds number of kills a hero has '''
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        ''' adds number of deaths to a hero '''
        self.deaths += num_deaths

    #helper function for fight
    @staticmethod
    def fighting(self, opponent):
        ''' helper function that recursively fights until one hero is dead '''
        opponent.take_damage(self.attack())
        if not self.is_alive() or not opponent.is_alive():
            return
        self.fighting(opponent, self)

    def fight(self, opponent):
        ''' makes a hero fight another until one of them is dead '''
        self.fighting(self, opponent)
        if self.is_alive():
            print(f"{self.name} won!")
            self.add_kill(1)
            opponent.add_deaths(1)
        else:
            print(f"{opponent.name} won!")
            self.add_deaths(1)
            opponent.add_kill(1)

    def add_weapon(self, weapon):
        ''' add a weapon object to a hero '''
        self.abilities.append(weapon)

class Weapon(Ability):
    def attack(self):
        ''' returns attack damage between 50% to 100% of max strength '''
        return random.randint(self.max_damage//2, self.max_damage)

class Team:
    def __init__(self, name):
        ''' Team constructor '''
        self.name = name
        self.heroes = []

    def remove_hero(self, name):
        ''' removes hero object from heroes list from the team '''
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
        return 0

    def view_all_heroes(self):
        ''' prints the name of every hero on a team '''
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        ''' Adds hero to the team '''
        self.heroes.append(hero)

    def is_team_alive(self):
        ''' Helper function to check if everyone on team is alive '''
        for hero in self.heroes:
            if not hero.is_alive():
                return False
        return True

    @staticmethod
    def get_random_fighter(self):
        ''' randomly choses a fighter from the team and returns it if the hero
        is still alive '''
        if not self.is_team_alive(): 
            return 0
        else: 
            fighter = random.choice(self.heroes)
            if not fighter.is_alive():
                fighter = self.get_random_fighter(self)
            return fighter

    def attack(self, other_team):
        ''' object team attacks another team until one of the team is dead '''
        dead = 0 # dead = 1 => self is dead | dead = 2 => other_team is dead
        while dead == 0:
            self_fighter = self.get_random_fighter(self)
            other_team_fighter = other_team.get_random_fighter(other_team)
            self_fighter.fight(other_team_fighter)
            if self.is_team_alive():
                dead = 1
            elif other_team.is_team_alive():
                dead = 2

    def revive_heroes(self, health = 100):
        ''' revives every hero in a team to with health '''
        for hero in self.heroes:
            hero.current_health = health

    def stats(self):
        ''' prints K/D ratio for every hero in the team'''
        for hero in self.heroes:
            if hero.deaths == 0:
                ratio = 'Infinite'
            else:
                ratio = hero.kills/hero.deaths
            print(f"{hero.name}'s K/D ratio is: {ratio}")

class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        print("- - - " * 7)
        ability_name = input("Enter the name for your ability: ")
        max_strength = int(input(f"Enter the maximum strength for {ability_name}: "))
        return Ability(ability_name, max_strength)

    def create_weapon(self):
        print("- - - " * 7)
        weapon_name = input("Enter the name for your weapon: ")
        max_strength = int(input(f"Enter the maximum damage for {weapon_name}: "))
        return Weapon(weapon_name, max_strength)

    def create_armor(self):
        print("- - - " * 7)
        armor_name = input("Enter the name for your armor: ")
        max_block = int(input(f"Enter the maximum block for {armor_name}: "))
        return Armor(armor_name, max_block)

    @staticmethod
    def yes_or_no(self, purpose):
        return input(f"Do you want to {purpose}?(Y/N): ").upper()

    def create_hero(self):
        print("- - - " * 7)
        hero_name = input("Enter your hero's name: ")
        hero_health = int(input("Enter your hero's starting health: "))
        hero = Hero(hero_name, hero_health)
        while self.yes_or_no(self, "add an ability") == 'Y':
            hero.add_ability(self.create_ability())
        while self.yes_or_no(self, "add a weapon") == 'Y':
            hero.add_weapon(self.create_weapon())
        while self.yes_or_no(self, "add an armor") == 'Y':
            hero.add_armor(self.create_armor())
        return hero

    def build_team_one(self):
        os.system('clear')
        name = input("Enter team one's name: ")
        self.team_one = Team(name)
        num_heroes = int(input(f"How many heroes do you want on {self.team_one.name}: "))
        while num_heroes > 0:
            self.team_one.heroes.append(self.create_hero())
            num_heroes -= 1

    def build_team_two(self):
        os.system('clear')
        name = input("Enter team two's name: ")
        self.team_two = Team(name)
        num_heroes = int(input(f"How many heroes do you want on {self.team_two.name}: "))
        while num_heroes > 0:
            self.team_two.heroes.append(self.create_hero())
            num_heroes -= 1

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_stats(self):
        os.system('clear')
        if self.team_one.is_team_alive():
            print(f"{self.team_one.name.upper()} won")
            for hero in self.team_one.heroes:
                if hero.is_alive():
                    print(f"{hero.name.upper()} survived with {hero.current_health}hp.")
        else:
            print(f"{self.team_two.name.upper()} won")
            for hero in self.team_two.heroes:
                if hero.is_alive():
                    print(f"{hero.name.upper()} survived with {hero.current_health}hp.")
        print("- - - " * 7)
        print("Team Stats:")
        print("- - - " * 7)
        print(f"Team {self.team_one.name.upper()}:")
        self.team_one.stats()
        print(f"Team {self.team_two.name.upper()}:")
        self.team_two.stats()
        print("- - - " * 7)

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()