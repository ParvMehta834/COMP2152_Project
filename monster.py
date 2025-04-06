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
            dict or None: Returns shard data if dropped, otherwise None
        """
        shard = self.lore_system.drop_shard(self.combat_strength)
        if shard:
            print("\nThe monster dropped a glowing lore shard!")
            return shard
        return None

    def monster_attacks(self):
        """
        Basic monster attack (non-adaptive).
        
        Returns:
            int: Random damage based on combat strength.
        """
        damage = random.randint(1, self.combat_strength)
        print(f"Monster attacks with {damage} damage!")
        return damage
<<<<<<< HEAD

    def dynamic_attack(self, hero_health, hero_loot):
        """
        Monster adapts attack based on hero's health and loot using list comprehension and conditionals.

        Args:
            hero_health (int): Hero's current health.
            hero_loot (list): Items hero is carrying.

        Returns:
            int: Calculated adaptive attack damage
        """
        # Define how each loot item influences the monster’s attack
        loot_modifiers = {
            "Poison Potion": 3,
            "Leather Boots": 1,
            "Health Potion": -2,
            "Flimsy Gloves": 2
        }

        # Apply modifiers based on hero's loot using list comprehension
        modifier = sum(
            loot_modifiers[item] if item in loot_modifiers else 0
            for item in hero_loot
        )

        # Determine base damage
        base_damage = random.randint(1, self.combat_strength)

        # Modify damage based on hero's health
        if hero_health < 5:
            base_damage += 2
        elif hero_health > 15:
            base_damage -= 1

        # Final damage calculation
        final_damage = max(1, base_damage + modifier)
        print(f"Monster uses dynamic AI and deals {final_damage} damage!")
        return final_damage
=======
    
def evolve_monster(monster, kill_count):
    """Enhance monster stats based on how many monsters the hero has defeated"""
    if kill_count >= 3:
        print("    |    !! Monster senses your strength and evolves!")
        monster.combat_strength += 2
        monster.health_points += 5
        print(f"    |    Evolved Monster - Strength: {monster.combat_strength}, Health: {monster.health_points}")
    elif kill_count >= 1:
        print("    |    Monster evolves slightly due to your success.")
        monster.combat_strength += 1
        print(f"    |    Slightly Evolved Monster - Strength: {monster.combat_strength}, Health: {monster.health_points}")


>>>>>>> 8b30b91fc05df7b3cf2c540a36ee9d9c74d6d728
