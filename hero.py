from character import Character

class Hero(Character):
    def __init__(self):
        super().__init__()
        print(f"Hero created with CS: {self.combat_strength}, HP: {self.health_points}")
    
    def __del__(self):
        print("The Hero object is being destroyed by the garbage collector")
        super().__del__()
    
    # This matches your existing function.py's hero_attacks(combat_strength, m_health_points)
    def hero_attacks(self):
        from function import hero_attacks as original_hero_attack
        return original_hero_attack(self.combat_strength, 0)  # m_health_points will be handled in main.py