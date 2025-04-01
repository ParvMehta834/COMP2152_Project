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
    # Add to the Monster class:
    def __init__(self):
        super().__init__()
        self._shard = self._generate_shard()  # Each monster carries a shard

    def _generate_shard(self):  #  Shard creation logic
        return {
            1: {"type": "Common", "lore": "Combat patterns"},
            2: {"type": "Rare", "lore": "Secret weakness"},
            3: {"type": "Legendary", "lore": "Treasure map"}
        }[random.choices([1,2,3], weights=[70,25,5])[0]]

    def drop_shard(self):  # Shard drop mechanic
        return self._shard if random.random() < 0.4 else None