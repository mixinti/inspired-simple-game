from abc import ABC, abstractmethod  

class Character(ABC):  
    def __init__(self, name, hp, attack, mp):
        self._name = name      # Nombre del personaje
        self._hp = hp          # Vida actual
        self._attack = attack  # Ataque base
        self._mp = mp          # Mana 

    @abstractmethod
    def perform_action(self, target):
        pass  

    def take_damage(self, amount):
        self._hp -= amount  # Reduce la vida
        if self._hp < 0:    # Evita valores negativos
            self._hp = 0

    def heal(self, amount):
        self._hp += amount  # Cura al personaje

    def use_mana(self, amount):
        if self._mp >= amount:  # Verifica si hay suficiente MP
            self._mp -= amount  # Resta el MP
            return True         # Indica que se pudo usar
        return False            # No había suficiente MP

    def is_alive(self):
        return self._hp > 0  

    @property
    def name(self):
        return self._name  

    @property
    def hp(self):
        return self._hp

    @property
    def mp(self):
        return self._mp
