# Personagem: Classe mãe
# Herói: Controlado pelo usuário
# Inimigo: Adversário do usuário

class Character:
    def __init__(self, name, life, level):
        self.__name = name
        self.__life = life
        self.__level = level

    def get_name(self):
        return self.__name
    
    def get_life(self):
        return self.__life
    
    def get_level(self):
        return self.__level
    
    def display_details(self):
        return f"Name: {self.get_name()}\nLife: {self.get_life()}\nLevel: {self.get_level()}"
    
    def suffering_damage(self, damage):
        self.__life -= damage
        if self.__life <= 0:
            self.__life = 0
    
    def attack(self, target):
        damage = self.__level * 2
        target.suffering_damage(damage)
        print(f"{self.get_name()} attacked {target.get_name()} and did {damage} damage!")

class Hero(Character):
    def __init__(self, name, life, level, ability):
        super().__init__(name, life, level)
        self.__ability = ability

    def get_ability(self):
        return self.__ability
    
    def display_details(self):
        return f"{super().display_details()}\nAbility: {self.get_ability()}\n"
    
class Enemy(Character):
    def __init__(self, name, life, level, kind):
        super().__init__(name, life, level)
        self.__kind = kind

    def get_kind(self):
        return self.__kind
    
    def display_details(self):
        return f"{super().display_details()}\nKind: {self.get_kind()}\n"
        
class Game:
    """ Classe orquestradora do jogo """
    
    def __init__(self) -> None:
        self.hero = Hero(name="Hero", life=100, level=5, ability="Super power")
        self.enemy = Enemy(name="Flittermouse", life=50, level=3, kind="Flying")

    def start_battle(self):
        """ Fazer a gestão da batalha em turnos """
        print("Starting battle!")
        while self.hero.get_life() > 0 and self.enemy.get_life() > 0:
            print("\nCharacter details:")
            print(self.hero.display_details())
            print(self.enemy.display_details())

            input("Press Enter to attack...")
            choice = input("Choice (1 - Normal attack, 2 - Special attack)")

            if choice == '1':
                self.hero.attack(self.enemy)
            else:
                print("Invalid choice. Choose again.")

        if self.hero.get_life() > 0:
            print("\nCongratulations, you won the battle!")
        else:
            print("\nYou were defeated!")

# Criar instancia do jogo e iniciar batalhar
game = Game()
game.start_battle()
