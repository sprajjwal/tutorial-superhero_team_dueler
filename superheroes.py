import random
import os

def input_validate(prompt, arg_type):
    ''' validaetes input based on type and returns valid input :
        type = 1 => integer
        type = 2 => string '''

    data_types = {1: 'integer', 2: 'name! Please use alhabets(A-Z, a-z) only'}  ##, 3: 'float'}
    assert 1 <= arg_type <= len(data_types), f"Unsupported input type: {arg_type}"
    data_type = data_types[arg_type]

    while True:
        user_input = input(prompt)
        if arg_type == 1 and user_input.isdigit():
            return user_input
        elif arg_type == 2 and user_input.isalpha():
            return user_input
        print(f"Please enter an {data_type}!")

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
        return sum(ability.attack() for ability in self.abilities)


    def add_armor(self, armor):
        ''' add armor to list of armors for a hero'''
        self.armors.append(armor)

    def defend(self, damage_amt):
        ''' returns how much damage a hero blocks based on armor'''
        if not self.is_alive():
            return 0
        # block = 0
        # for armor in self.armors:
        #     block += armor.block()
        # return block
        return sum(armor.block() for armor in self.armors)    

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
        if len(self.abilities) == 0  or len(opponent.abilities) == 0:
            print("Draw!")
            return
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
        # for hero in self.heroes:
        #     if hero.name == name:
        #         self.heroes.remove(hero)
        self.heroes.remove([hero for hero in self.heroes if hero.name == name][0])
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
            if hero.is_alive():
                return True
        return False

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
            if self.is_team_alive() or self_fighter == 0:
                dead = 1
            elif other_team.is_team_alive() or other_team_fighter == 0:
                dead = 2

    def revive_heroes(self, health = 100):
        ''' revives every hero in a team to with health '''
        for hero in self.heroes:
            hero.current_health = health

    def stats(self):
        ''' prints K/D ratio for every hero in the team'''
        for hero in self.heroes:
            print(f"{hero.name}'s K/D ratio is: {hero.kills}/{hero.deaths}")

class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def create_ability(self, name):
        ''' prompts user to create abilities for hero'''
        print("- - - " * 7)
        ability_name = input_validate(f"Enter the name for your ability to give to {name}: ", 2)
        max_strength = int(input_validate(f"Enter the maximum strength for {ability_name}: ", 1))
        return Ability(ability_name, max_strength)

    def create_weapon(self, name):
        ''' prompts user to create weapon for hero'''
        print("- - - " * 7)
        weapon_name = input_validate(f"Enter the name for your weapon to give to {name}: ", 2)
        max_strength = int(input_validate(f"Enter the maximum damage for {weapon_name}: ", 1))
        return Weapon(weapon_name, max_strength)

    def create_armor(self, name):
        ''' prompts user to create armor for hero'''
        print("- - - " * 7)
        armor_name = input_validate(f"Enter the name for your armor to give to {name}: ", 2)
        max_block = int(input_validate(f"Enter the maximum block for {armor_name}: ", 1))
        return Armor(armor_name, max_block)

    @staticmethod
    def yes_or_no(self, purpose):
        ''' helper function that prompts user to respond with Y/N
        for user to create more of something'''
        return input_validate(f"Do you want to {purpose}?(Y/N): ", 2).upper()

    def create_hero(self, team_number, hero_number):
        ''' prompts user to create a hero '''
        print("- - - " * 7)

        hero_name = input_validate(f"Enter hero number {hero_number}'s name for {team_number}: ", 2)
        hero_health = input_validate(f"Enter your hero number {hero_number}'s starting health: ", 1)
        hero = Hero(hero_name, hero_health)

        while self.yes_or_no(self, "add an ability") == 'Y': # create abilities
            hero.add_ability(self.create_ability(hero_name))
        while self.yes_or_no(self, "add a weapon") == 'Y': # create weapons
            hero.add_weapon(self.create_weapon(hero_name))
        while self.yes_or_no(self, "add an armor") == 'Y': # create armors
            hero.add_armor(self.create_armor(hero_name))
        return hero

    def build_team_one(self):
        ''' builds a team by creating multiple heros'''
        os.system('clear')

        name = input_validate("Enter team one's name: ", 2)
        self.team_one = Team(name)
        num_heroes = int(input_validate(f"How many heroes do you want on {self.team_one.name}: ", 1))
        ctr = 1
        while ctr <= num_heroes:
            self.team_one.heroes.append(self.create_hero("Team One", ctr))
            os.system('clear')
            ctr += 1

    def build_team_two(self):
        ''' builds a team by creating multiple heros'''
        os.system('clear')
        name = input_validate("Enter team two's name: ", 2)
        self.team_two = Team(name)
        num_heroes = int(input_validate(f"How many heroes do you want on {self.team_two.name}: ", 1))
        ctr = 1
        while ctr <= num_heroes :
            self.team_two.heroes.append(self.create_hero("Team Two", ctr))
            os.system('clear')
            ctr += 1

    def team_battle(self):
        ''' makes the teams battle each other'''
        self.team_one.attack(self.team_two)

    @staticmethod
    def team_avg_print(team):
        kills = 0
        deaths = 0
        for hero in team.heroes:
            kills+= hero.kills
            deaths += hero.deaths
        print(f"{team.name} had an average K/D of {kills}/{deaths}")
    def show_stats(self):
        ''' shows all the stats for each team'''
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
        self.team_avg_print(self.team_one)
        self.team_avg_print(self.team_two)
        print("- - - " * 7)
        print(f"Team {self.team_one.name.upper()}:")
        self.team_one.stats()
        print(f"Team {self.team_two.name.upper()}:")
        self.team_two.stats()
        print("- - - " * 7)

if __name__ == "__main__":
    ''' main function running the game '''
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input_validate("Play Again? Y or N: ", 2)

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()