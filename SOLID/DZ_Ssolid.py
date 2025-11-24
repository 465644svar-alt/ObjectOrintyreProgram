from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def atack(self):
        pass

class Bow(Weapon):
    def atack(self):
        return "Герой стреляет из лука"

class Sword(Weapon):
    def atack(self):
        return "Герой наносит удар мечом"

class Fighter():
    def __init__(self, name):
        self.name = name
        self.current_weapon = None


    def change_weapon(self, weapon: Weapon):
        self.current_weapon = weapon
        weapon_name = weapon.__class__.__name__
        if weapon_name == "Bow":
            print(f"{self.name} выбирает лук.")
        elif weapon_name == "Sword":
            print(f"{self.name} выбирает меч.")
        else:
            print(f"{self.name} выбирает {weapon_name.lower()}.")

    def attack_monster(self):
        if self.current_weapon:
            print(self.current_weapon.attack())
            print("Монстр побежден!")
        else:
            print("Боец не выбрал оружие!")

class Monster:
    def __init__(self, name):
        self.name = name


# ---------- Демонстрация боя ----------
if __name__ == "__main__":
    # Создаем бойца и монстра
    fighter = Fighter("Алеша Попович")
    monster = Monster("Змей Горыныч")

    print("=== Бой начинается! ===\n")

    # Бой с мечом
    sword = Sword()
    fighter.change_weapon(sword)
    fighter.attack_monster()

    print("\n" + "=" * 30 + "\n")

    # Бой с луком
    bow = Bow()
    fighter.change_weapon(bow)
    fighter.attack_monster()

    print("\n" + "=" * 30 + "\n")

