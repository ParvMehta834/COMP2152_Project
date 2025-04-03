import random
from textwrap import wrap

LORE_DATABASE = [
    "The king's sword was forged from a fallen star.",
    "Ancient demons sleep beneath these castle walls.",
    "The forest remembers every life it has taken.",
    "Silver bells keep the shadow creatures at bay.",
    "The old gods speak through the cracks in reality.",
    "Beware the moon when it shines crimson red.",
    "Dragons hoard not just gold, but forgotten truths.",
    "The royal bloodline carries a dark secret."
]

class LoreShard:
    def __init__(self):
        self.collected_lore = []
        self._current_shard = None

    def drop_shard(self, enemy_level):
        """Generate a lore shard with probability based on enemy level"""
        drop_chance = min(0.5, 0.3 + (enemy_level * 0.02))  # Scales with level up to 50%
        if random.random() < drop_chance:
            lore = random.choice(LORE_DATABASE)
            self._current_shard = {
                "encrypted": self._advanced_cipher(lore),
                "original": lore,
                "difficulty": min(5, max(1, enemy_level // 5)),
                "revealed_letters": set()
            }
            return self._current_shard
        return None

    def _advanced_cipher(self, text):
        """Better encryption using multiple techniques"""
        # Reverse the words
        words = text.split()
        reversed_words = [word[::-1] for word in words]
        
        # Apply Caesar cipher with alternating shifts
        result = []
        shift_direction = 1
        for word in reversed_words:
            encrypted_word = []
            for char in word:
                if char.isalpha():
                    base = ord('A') if char.isupper() else ord('a')
                    shift = 5 * shift_direction
                    new_char = chr((ord(char) - base + shift) % 26 + base)
                    encrypted_word.append(new_char)
                    shift_direction *= -1  # Alternate shift direction
                else:
                    encrypted_word.append(char)
            result.append(''.join(encrypted_word))
        
        return ' '.join(result)

    def decrypt_minigame(self, shard=None):
        """Interactive decryption minigame with progressive hints"""
        shard = shard or self._current_shard
        if not shard:
            print("No shard available to decrypt!")
            return False

        print(f"\n=== Decrypting Lore Shard (Difficulty: {shard['difficulty']}/5 ===")
        print("Encrypted Text:")
        print(self._display_encrypted(shard))
        
        attempts = 5 - shard['difficulty']  # More attempts for harder shards
        print(f"\nYou have {attempts} attempts to guess letters.")

        for attempt in range(1, attempts + 1):
            guess = input(f"\nAttempt {attempt}/{attempts}: Guess a letter: ").lower()
            
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter!")
                continue
                
            if guess in shard['original'].lower():
                shard['revealed_letters'].add(guess)
                print(f"Correct! The letter '{guess}' appears {shard['original'].lower().count(guess)} times.")
            else:
                print(f"Wrong! The letter '{guess}' is not in the text.")
            
            print("\nCurrent decryption progress:")
            print(self._display_encrypted(shard))
            
            if self._is_fully_decrypted(shard):
                print("\nYou've fully decrypted the lore!")
                break

        print(f"\n=== The hidden lore was ===")
        print(shard['original'])
        self.collected_lore.append(shard['original'])
        return True

    def _display_encrypted(self, shard):
        """Show encrypted text with revealed letters"""
        display = []
        for char in shard['encrypted'].lower():
            if char.isalpha() and char in shard['revealed_letters']:
                display.append(char.upper())
            elif char == ' ':
                display.append(' ')
            elif not char.isalpha():
                display.append(char)
            else:
                display.append('_')
        return ' '.join(wrap(''.join(display), width=50))

    def _is_fully_decrypted(self, shard):
        """Check if all letters have been revealed"""
        original_letters = {c.lower() for c in shard['original'] if c.isalpha()}
        return original_letters.issubset(shard['revealed_letters'])

    def show_collected_lore(self):
        """Display all collected lore fragments"""
        print("\n=== Your Collected Lore ===")
        if not self.collected_lore:
            print("You haven't collected any lore yet!")
            return
        
        for i, lore in enumerate(self.collected_lore, 1):
            print(f"{i}. {lore}")
        print()