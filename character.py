import random

class Character:
    def __init__(self):
        self._combat_strength = random.randint(1, 20)
        self._health_points = random.randint(1, 20)
        self._memory_shards = [] 

def __init__(self):
    self._combat_strength = random.randint(1, 20)
    self._health_points = random.randint(1, 20)
    self._memory_shards = []  # Initialize shard storage

@property
def memory_shards(self):  # Getter for shards
    return self._memory_shards

def add_shard(self, shard):  # Method to add shards
    if isinstance(shard, dict) and "tier" in shard:
        self._memory_shards.append(shard)
    
    def __del__(self):
        pass  # Empty parent destructor
    
    @property
    def combat_strength(self):
        return self._combat_strength
    
    @combat_strength.setter
    def combat_strength(self, value):
        self._combat_strength = max(0, value)
    
    @property
    def health_points(self):
        return self._health_points
    
    @health_points.setter
    def health_points(self, value):
        self._health_points = max(0, value)