import random

class Character:
    """Base class for all characters in the game"""
    
    def __init__(self, combat_strength=None, health_points=None):
        """
        Initialize character attributes
        Args:
            combat_strength (int, optional): Override random combat strength
            health_points (int, optional): Override random health points
        """
        self._combat_strength = combat_strength if combat_strength is not None else random.randint(1, 20)
        self._health_points = health_points if health_points is not None else random.randint(1, 20)
    
    def __del__(self):
        """Destructor for cleanup"""
        pass
    
    @property
    def combat_strength(self):
        """Get the character's combat strength"""
        return self._combat_strength
    
    @combat_strength.setter
    def combat_strength(self, value):
        """Set combat strength (minimum 0)"""
        self._combat_strength = max(0, value)
    
    @property
    def health_points(self):
        """Get the character's health points"""
        return self._health_points
    
    @health_points.setter
    def health_points(self, value):
        """Set health points (minimum 0)"""
        self._health_points = max(0, value)
    
    def is_alive(self):
        """Check if character is alive"""
        return self.health_points > 0