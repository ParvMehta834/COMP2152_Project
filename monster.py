from character import Character
import random

class Monster(Character):
    def __init__(self):
        """Monster character class"""
        super().__init__()
        print(f"Monster created - Strength: {self.combat_strength}, Health: {self.health_points}")
    
    def __del__(self):
        """Monster destructor"""
        print("The Monster object is being destroyed by the garbage collector")
        super().__del__()
    
    def monster_attacks(self):
        """Monster attack method"""
        return random.randint(1, self.combat_strength)