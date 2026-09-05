from domain.heroes import Cloud, Aerith, Tifa
from domain.enemy import Reno
from ui.console import ConsoleUI
import random

class Game:
    def __init__(self):
        # Creamos la interfaz de usuario
        self.ui = ConsoleUI()

        # Creamos los personajes 
        self.cloud = Cloud()
        self.tifa = Tifa()
        self.aerith = Aerith()

        # Creamos el enemigo
        self.enemy = Reno()

        # Definimos el orden de turnos 
        self.turn_order = [
            self.cloud,   # turno de Cloud
            self.enemy,   # turno de Reno
            self.tifa,    # turno de Tifa
            self.enemy,   # turno de Reno
            self.aerith,  # turno de Aerith
            self.enemy    # turno de Reno
        ]

    # Método principal del juego
    def run(self):
        self.ui.show_message("Reno Fight")
        
        while self.enemy.is_alive() and any(h.is_alive() for h in [self.cloud, self.tifa, self.aerith]):

            for actor in self.turn_order:
                if not self.enemy.is_alive():
                    break
                    
                if actor != self.enemy and not actor.is_alive():
                    continue
                    
                self.execute_turn(actor)
                
        self.end_game()

    # Ejecuta el turno de un personaje
    def execute_turn(self, actor):
        if actor == self.enemy:
            self.enemy_turn()
            return  
            
        self.ui.show_status(actor, self.enemy)

        # Pedimos acción al jugador
        choice = self.ui.choose_action(actor)

        # Si elige ataque básico
        if choice == "1":
            log = actor.perform_action(self.enemy)

        # Si elige habilidad y tiene una
        elif choice == "2" and actor.skill:
            log = actor.skill.use(actor, self.enemy)

        # Si elige magia y tiene hechizos
        elif choice == "3" and actor.spells:
            log = self.cast_spell(actor)

        # Si no eligió algo válido
        else:
            log = "Acción inválida."

        # Mostramos resultado
        self.ui.show_message(log)

    # Maneja lanzamiento de hechizos
    def cast_spell(self, hero):
        spell = self.ui.choose_spell(hero)
        if spell is None:
            return "Cancelado."

        if spell.__class__.__name__ == "Cure":
            target = self.ui.choose_ally([self.cloud, self.tifa, self.aerith])
        else:
            target = self.enemy
        return spell.cast(hero, target)

    # Turno del enemigo
    def enemy_turn(self):
        heroes_alive = [h for h in [self.cloud, self.tifa, self.aerith] if h.is_alive()]
        target = random.choice(heroes_alive)
        log = self.enemy.perform_action(target)
        self.ui.show_message(f"\n[Enemigo] {log}")

    # Final del juego
    def end_game(self):
        if self.enemy.is_alive():
            self.ui.show_message("Derrota.")

        else:
            self.ui.show_message("Victoria!")
