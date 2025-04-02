from character import Character
import random
from lore_shard import LoreShard

class Monster(Character):
    def __init__(self, combat_strength=None, health_points=None):
        """
        Initialize a Monster instance.
        
        Args:
            combat_strength (int, optional): Override random combat strength. Defaults to None.
            health_points (int, optional): Override random health points. Defaults to None.
        """
        super().__init__()
        
        # Override default random values if specified
        if combat_strength is not None:
            self._combat_strength = combat_strength
        if health_points is not None:
            self._health_points = health_points
            
        self.lore_system = LoreShard()
        print(f"Monster created - Strength: {self.combat_strength}, Health: {self.health_points}")
    
    def __del__(self):
        """Destructor called when monster is garbage collected"""
        print("The Monster object is being destroyed by the garbage collector")
        super().__del__()
    
    def on_death(self):
        """
        Handle actions when monster dies.
        
        Returns:
            dict/None: Returns shard data if dropped, otherwise None
        """
        shard = self.lore_system.drop_shard(self.combat_strength)
        if shard:
            print("\nThe monster dropped a glowing lore shard!")
            return shard
        return None
    
    def monster_attacks(self):
        """Calculate monster's attack damage"""
        damage = random.randint(1, self.combat_strength)
        print(f"Monster attacks with {damage} damage!")
        return damage