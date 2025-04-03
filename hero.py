from character import Character

class Hero(Character):
    """Player-controlled hero character"""
    
    def __init__(self, combat_strength=None, health_points=None):
        """
        Initialize hero character
        Args:
            combat_strength (int, optional): Override random combat strength
            health_points (int, optional): Override random health points
        """
        super().__init__(combat_strength, health_points)
        print(f"Hero created - Combat Strength: {self.combat_strength}, Health: {self.health_points}")
    
    def __del__(self):
        """Hero destructor"""
        print("The Hero object is being destroyed by the garbage collector")
        super().__del__()
    
    def hero_attacks(self, target_health=0):
        """Execute hero's attack"""
        from functions import hero_attacks  # Local import to prevent circular imports
        return hero_attacks(self.combat_strength, target_health)