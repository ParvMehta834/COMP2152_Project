# Import the random library to use for the dice later
import random
import os
import platform

#Print system info when imported
print(f"Operating System: {os.name}")
print(f"Python Version: {platform.python_version()}")

# Will the line below print when you import function.py into main.py?
# print("Inside function.py")

def use_loot(belt, health_points):
    good_loot_options = ["Health Potion", "Leather Boots"]
    bad_loot_options = ["Poison Potion"]

    print("    |    !!You see a monster in the distance! So you quickly use your first item:")
    first_item = belt.pop(0)
    if first_item in good_loot_options:
        health_points = min(20, (health_points + 2))
        print("    |    You used " + first_item + " to up your health to " + str(health_points))
    elif first_item in bad_loot_options:
        health_points = max(0, (health_points - 2))
        print("    |    You used " + first_item + " to hurt your health to " + str(health_points))
    else:
        print("    |    You used " + first_item + " but it's not helpful")
    return belt, health_points

def collect_loot(loot_options, belt):
    ascii_image3 = """
                      @@@ @@                
             *# ,        @              
           @           @                
                @@@@@@@@                
               @   @ @% @*              
            @     @   ,    &@           
          @                   @         
         @                     @        
        @                       @       
        @                       @       
        @*                     @        
          @                  @@         
              @@@@@@@@@@@@          
              """
    print(ascii_image3)
    loot_roll = random.choice(range(1, len(loot_options) + 1))
    loot = loot_options.pop(loot_roll - 1)
    belt.append(loot)
    print("    |    Your belt: ", belt)
    return loot_options, belt

# Hero's Attack Function
def hero_attacks(combat_strength, m_health_points):
    ascii_image = """
                                @@   @@ 
                                @    @  
                                @   @   
               @@@@@@          @@  @    
            @@       @@        @ @@     
           @%         @     @@@ @       
            @        @@     @@@@@     
               @@@@@        @@       
               @    @@@@                
          @@@ @@                        
       @@     @                         
   @@*       @                          
   @        @@                          
           @@                                                    
         @   @@@@@@@                    
        @            @                  
      @              @                  

  """
    print(ascii_image)
    print("    |    Player's weapon (" + str(combat_strength) + ") ---> Monster (" + str(m_health_points) + ")")
    if combat_strength >= m_health_points:
        # Player was strong enough to kill monster in one blow
        m_health_points = 0
        print("    |    You have killed the monster")
    else:
        # Player only damaged the monster
        m_health_points -= combat_strength
        print("    |    You have reduced the monster's health to: " + str(m_health_points))
    return m_health_points

# Monster's Attack Function
def monster_attacks(m_combat_strength, health_points):
    ascii_image2 = """                                                                 
           @@@@ @                           
      (     @*&@  ,                         
    @               %                       
     &#(@(@%@@@@@*   /                      
      @@@@@.                                
               @       /                    
                %         @                 
            ,(@(*/           %              
               @ (  .@#                 @   
                          @           .@@. @
                   @         ,              
                      @       @ .@          
                             @              
                          *(*  *      
             """
    print(ascii_image2)
    print("    |    Monster's Claw (" + str(m_combat_strength) + ") ---> Player (" + str(health_points) + ")")
    if m_combat_strength >= health_points:
        # Monster was strong enough to kill player in one blow
        health_points = 0
        print("    |    Player is dead")
    else:
        # Monster only damaged the player
        health_points -= m_combat_strength
        print("    |    The monster has reduced Player's health to: " + str(health_points))
    return health_points

# Improved dream levels with validation
def get_dream_level():
    """Helper function for validated dream level input"""
    while True:
        try:
            level = input("How many dream levels do you want to go down? (0-3): ")
            level = int(level)
            if 0 <= level <= 3:
                return level
            print("Please enter a number between 0-3")
        except ValueError:
            print("Invalid input. Please enter a number.")

def inception_dream(num_dream_lvls):
    """Modified to use validation"""
    try:
        num_dream_lvls = int(num_dream_lvls)
        if not 0 <= num_dream_lvls <= 3:
            raise ValueError("Dream level must be 0-3")
    except ValueError as e:
        print(f"Error: {e}")
        num_dream_lvls = 0  # Default to 0 on invalid input

    # Base Case
    if num_dream_lvls == 1:
        print("    |    You are in the deepest dream level now")
        print("    |", end="    ")
        input("Start to go back to real life? (Press Enter)")
        print("    |    You start to regress back through your dreams to real life.")
        return 2

    # Recursive Case
    elif num_dream_lvls > 1:
        return 1 + int(inception_dream(num_dream_lvls - 1))
    return 0

# Modified save/load with monsters killed tracking
def save_game(winner, hero_name="", num_stars=0, monsters_killed=0):
    """Now saves monsters killed count"""
    with open("save.txt", "w") as file:  # Changed to 'w' to overwrite
        file.write(f"MonstersKilled:{monsters_killed}\n")  # First line
        if winner == "Hero":
            file.write(f"Hero {hero_name} has killed a monster and gained {num_stars} stars.\n")
        elif winner == "Monster":
            file.write("Monster has killed the hero previously\n")

def load_game():
    """Now returns (last_line, monsters_killed)"""
    try:
        with open("save.txt", "r") as file:
            lines = file.readlines()
            if lines:
                # Get monsters killed from first line
                monsters_killed = int(lines[0].split(":")[1].strip())
                last_line = lines[-1].strip() if len(lines) > 1 else ""
                return last_line, monsters_killed
    except (FileNotFoundError, IndexError, ValueError):
        pass  # File doesn't exist or is corrupted
    return None, 0  # Default values

def adjust_combat_strength(combat_strength, m_combat_strength):
    """Updated to work with new load_game() return"""
    last_game, monsters_killed = load_game()
    if last_game:
        if "Hero" in last_game and "gained" in last_game:
            num_stars = int(last_game.split()[-2])
            if num_stars > 3:
                print("    |    ... Increasing the monster's combat strength since you won so easily last time")
                m_combat_strength += 1
        elif "Monster has killed the hero" in last_game:
            combat_strength += 1
            print("    |    ... Increasing the hero's combat strength since you lost last time")
        else:
            print("    |    ... Based on your previous game, neither the hero nor the monster's combat strength will be increased")
    return combat_strength, m_combat_strength, monsters_killed