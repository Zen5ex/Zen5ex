import tkinter as tk
import random

class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.level = 1
        self.inventory = []

    def level_up(self):
        self.level += 1
        self.health += 20
        print(f"{self.name} поднялся на уровень {self.level}!")

class Game:
    def __init__(self, root):
        self.root = root
        self.player = None
        self.current_enemy = None
        self.enemies = self.create_enemies()
        self.create_widgets()

    def create_enemies(self):
        # Создание списка врагов с разным именем и здоровьем
        enemy_names = [
            "Скелет", "Зомби", "Демон", "Гоблин", "Тролль",
            "Оборотень", "Вампир", "Привидение", "Дракон", "Гидра",
            "Чудовище из болота", "Бандит", "Призрак", "Медуза", "Грифон",
            "Кентавр", "Минотавр", "Лежащая тень", "Паук-разведчик", "Ледяной голем",
            "Пиромант"
        ]
        return [Enemy(name, random.randint(50, 150)) for name in enemy_names]

    def create_widgets(self):
        self.root.title("Ролевая игра")

        self.name_label = tk.Label(self.root, text="Введите имя игрока:")
        self.name_label.pack()

        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        self.start_button = tk.Button(self.root, text="Начать игру", command=self.start_game)
        self.start_button.pack()

        self.status_label = tk.Label(self.root, text="", wraplength=300)
        self.status_label.pack()

        self.attack_button = tk.Button(self.root, text="Атаковать", command=self.player_attack, state=tk.DISABLED)
        self.attack_button.pack()

        self.inventory_label = tk.Label(self.root, text="Инвентарь: ")
        self.inventory_label.pack()

        self.enemy_label = tk.Label(self.root, text="")
        self.enemy_label.pack()

        self.player_label = tk.Label(self.root, text="")
        self.player_label.pack()

    def start_game(self):
        player_name = self.name_entry.get()
        self.player = Player(player_name)
        self.status_label.config(text=f"Добро пожаловать, {self.player.name}!")
        self.name_entry.delete(0, tk.END)
        self.start_button.config(state=tk.DISABLED)
        self.attack_button.config(state=tk.NORMAL)
        self.spawn_enemy()

    def spawn_enemy(self):
        self.current_enemy = random.choice(self.enemies)
        self.enemy_label.config(text=f"Вы встретили: {self.current_enemy.name} с {self.current_enemy.health} здоровьем.")
        self.update_player_status()

    def player_attack(self):
        if self.current_enemy:
            # Наносим урон врагу
            damage = random.randint(10, 30)
            self.current_enemy.health -= damage
            self.status_label.config(text=f"{self.player.name} атакует {self.current_enemy.name} и наносит {damage} урона.")

            if self.current_enemy.health <= 0:
                self.status_label.config(text=f"{self.player.name} победил {self.current_enemy.name}!")
                self.player.level_up()
                self.spawn_enemy()  # Новый враг после победы
            else:
                # Враг атакует обратно
                enemy_damage = random.randint(5, 15)
                self.player.health -= enemy_damage
                self.update_player_status()

    def update_player_status(self):
        self.player_label.config(text=f"{self.player.name}: {self.player.health} здоровья, уровень {self.player.level}.")
        if self.player.health <= 0:
            self.status_label.config(text=f"{self.player.name} пал в бою!")
            self.attack_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()