import random

# ಸೂಟ್ ಮತ್ತು ರ‍್ಯಾಂಕ್‌ಗಳ ವ್ಯಾಖ್ಯಾನ
suits = ['Heart', 'Diamond', 'Club', 'Spade']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# ಸಂಪೂರ್ಣ ಕಾರ್ಡ್ ಡೆಕ್ ಸಿದ್ಧಪಡಿಸುವುದು (52 ಕಾರ್ಡ್‌ಗಳು)
deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]

# ಕಾರ್ಡ್‌ಗಳನ್ನು ಯಾದೃಚ್ಛಿಕವಾಗಿ ಶಫಲ್ ಮಾಡುವುದು
random.shuffle(deck)

# ಇಬ್ಬರು ಆಟಗಾರರಿಗೆ ತಲಾ 13 ಕಾರ್ಡ್‌ಗಳನ್ನು ಹಂಚುವುದು
player1_hand = deck[:13]
player2_hand = deck[13:26]

# ಕಾರ್ಡ್‌ಗಳನ್ನು ವಿಂಗಡಿಸುವ (Sort ಮಾಡುವ) ವಿಧಾನ
player1_hand.sort()
player2_hand.sort()

print("--- ಆಟಗಾರ 1 ರ ರಮ್ಮಿ ಕಾರ್ಡ್‌ಗಳು ---")
for card in player1_hand:
    print(card)

print("\n--- ಆಟಗಾರ 2 ರ ರಮ್ಮಿ ಕಾರ್ಡ್‌ಗಳು ---")
for card in player2_hand:
    print(card)
import random

# ಸೂಟ್ ಮತ್ತು ರ‍್ಯಾಂಕ್‌ಗಳ ವ್ಯಾಖ್ಯಾನ
suits = ['Heart', 'Diamond', 'Club', 'Spade']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# ಸಂಪೂರ್ಣ ಕಾರ್ಡ್ ಡೆಕ್ ಸಿದ್ಧಪಡಿಸುವುದು (52 ಕಾರ್ಡ್‌ಗಳು)
deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]

# ಕಾರ್ಡ್‌ಗಳನ್ನು ಯಾದೃಚ್ಛಿಕವಾಗಿ ಶಫಲ್ ಮಾಡುವುದು
random.shuffle(deck)

# ಜೋಕರ್ ಕಾರ್ಡ್ ಅನ್ನು ಆಯ್ಕೆ ಮಾಡುವುದು (ಡೆಕ್‌ನಿಂದ ಕೊನೆಯ ಕಾರ್ಡ್ ಅಥವಾ ಯಾದೃಚ್ಛಿಕ ಕಾರ್ಡ್)
joker_card = deck.pop()

# ಇಬ್ಬರು ಆಟಗಾರರಿಗೆ ತಲಾ 13 ಕಾರ್ಡ್‌ಗಳನ್ನು ಹಂಚುವುದು
player1_hand = deck[:13]
player2_hand = deck[13:26]

# ಕಾರ್ಡ್‌ಗಳನ್ನು ವಿಂಗಡಿಸುವ (Sort ಮಾಡುವ) ವಿಧಾನ
player1_hand.sort()
player2_hand.sort()

print(f"★ ಆಟದ ಜೋಕರ್ ಕಾರ್ಡ್ (Joker): {joker_card} ★\n")

print("--- ಆಟಗಾರ 1 ರ ರಮ್ಮಿ ಕಾರ್ಡ್‌ಗಳು ---")
for card in player1_hand:
    print(card)

print("\n--- ಆಟಗಾರ 2 ರ ರಮ್ಮಿ ಕಾರ್ಡ್‌ಗಳು ---")
for card in player2_hand:
    print(card)
import random

# ಸೂಟ್ ಮತ್ತು ರ‍್ಯಾಂಕ್‌ಗಳ ವ್ಯಾಖ್ಯಾನ
suits = ['Heart', 'Diamond', 'Club', 'Spade']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# ಸಂಪೂರ್ಣ ಕಾರ್ಡ್ ಡೆಕ್ ಸಿದ್ಧಪಡಿಸುವುದು (52 ಕಾರ್ಡ್‌ಗಳು)
deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]

# ಕಾರ್ಡ್‌‌ಗಳನ್ನು ಯಾದೃಚ್ಛಿಕವಾಗಿ ಶಫಲ್ ಮಾಡುವುದು
random.shuffle(deck)

# ಜೋಕರ್ ಕಾರ್ಡ್ ಅನ್ನು ಆಯ್ಕೆ ಮಾಡುವುದು
joker_card = deck.pop()

# ಇಬ್ಬರು ಆಟಗಾರರಿಗೆ ತಲಾ 13 ಕಾರ್ಡ್‌ಗಳನ್ನು ಹಂಚುವುದು
player1_hand = deck[:13]
player2_hand = deck[13:26]

# ಉಳಿದ ಕಾರ್ಡ್‌ಗಳು ಕ್ಲೋಸ್ಡ್ ಡೆಕ್ ಆಗಿರುತ್ತವೆ, ಮತ್ತು ಒಂದನ್ನು ಡಿಸ್ಕಾರ್ಡ್ ಪೈಲ್‌ಗೆ ಹಾಕDಣ
closed_deck = deck[26:]
discard_pile = [closed_deck.pop()]

# ಕಾರ್ಡ್‌ಗಳನ್ನು ವಿಂಗಡಿಸುವ (Sort ಮಾಡುವ) ವಿಧಾನ
player1_hand.sort()
player2_hand.sort()

print(f"★ ಆಟದ ಜೋಕರ್ ಕಾರ್ಡ್ (Joker): {joker_card} ★\n")
print(f"♻️ ಡಿಸ್ಕಾರ್ಡ್ ಪೈಲ್ (Open Card): {discard_pile[0]}\n")

print("--- ಆಟಗಾರ 1 ರ ರಮ್ಮಿ ಕಾರ್ಡ್‌ಗಳು ---")
for card in player1_hand:
    print(card)

print("\n--- ಆಟಗಾರ 2 ರ ರಮ್ಮಿ ಕಾರ್ಡ್‌ಗಳು ---")
for card in player2_hand:
    print(card)
import random

# ಸೂಟ್ ಮತ್ತು ರ‍್ಯಾಂಕ್‌ಗಳ ವ್ಯಾಖ್ಯಾನ
suits = ['Heart', 'Diamond', 'Club', 'Spade']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# ಸಂಪೂರ್ಣ ಕಾರ್ಡ್ ಡೆಕ್ ಸಿದ್ಧಪಡಿಸುವುದು
deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
random.shuffle(deck)

# ಜೋಕರ್ ಕಾರ್ಡ್ ಆಯ್ಕೆ ಮತ್ತು ಆಟಗಾರರಿಗೆ ಕಾರ್ಡ್ ಹಂಚಿಕೆ
joker_card = deck.pop()
player1_hand = deck[:13]
player2_hand = deck[13:26]
closed_deck = deck[26:]
discard_pile = [closed_deck.pop()]

player1_hand.sort()
player2_hand.sort()

print(f"★ ಜೋಕರ್ ಕಾರ್ಡ್: {joker_card} ★\n")
print(f"♻️ ಡಿಸ್ಕಾರ್ಡ್ ಪೈಲ್ (Open Card): {discard_pile[-1]}\n")

print("--- ಆಟಗಾರ 1 ರ ಆರಂಭಿಕ ಕಾರ್ಡ್‌ಗಳು ---")
for card in player1_hand:
    print(card)

# ಆಟಗಾರ 1 ರ ಸರದಿ: ಕ್ಲೋಸ್ಡ್ ಡೆಕ್‌ನಿಂದ ಒಂದು ಕಾರ್ಡ್ ತೆಗೆಯುವುದು
drawn_card = closed_deck.pop()
player1_hand.append(drawn_card)
player1_hand.sort()

print(f"\n[!] ಆಟಗಾರ 1 ರವೀಗ ಪಡೆದ ಹೊಸ ಕಾರ್ಡ್: {drawn_card}")
print("\n--- ಕಾರ್ಡ್ ತೆಗೆದ ನಂತರ ಆಟಗಾರ 1 ರ ಕೈಯಲ್ಲಿರುವ ಕಾರ್ಡ್‌ಗಳು ---")
for card in player1_hand:
    print(card)
import random

# ಸೂಟ್ ಮತ್ತು ರ‍್ಯಾಂಕ್‌ಗಳ ವ್ಯಾಖ್ಯಾನ
suits = ['Heart', 'Diamond', 'Club', 'Spade']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# ಸಂಪೂರ್ಣ ಕಾರ್ಡ್ ಡೆಕ್ ಸಿದ್ಧಪಡಿಸುವುದು
deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
random.shuffle(deck)

# ಜೋಕರ್ ಕಾರ್ಡ್ ಆಯ್ಕೆ ಮತ್ತು ಆಟಗಾರರಿಗೆ ಕಾರ್ಡ್ ಹಂಚಿಕೆ
joker_card = deck.pop()
player1_hand = deck[:13]
player2_hand = deck[13:26]
closed_deck = deck[26:]
discard_pile = [closed_deck.pop()]

player1_hand.sort()
player2_hand.sort()

print(f"★ ಜೋಕರ್ ಕಾರ್ಡ್: {joker_card} ★\n")

# ಆಟಗಾರ 1 ಕಾರ್ಡ್ ಡ್ರಾ ಮಾಡುವುದು
drawn_card = closed_deck.pop()
player1_hand.append(drawn_card)
player1_hand.sort()

print(f"[!] ಆಟಗಾರ 1 ಪಡೆದ ಹೊಸ ಕಾರ್ಡ್: {drawn_card}")

# ಆಟಗಾರನು ಕೊನೆಯ ಕಾರ್ಡ್ ಅನ್ನು ಡಿಸ್ಕಾರ್ಡ್ ಪೈಲ್‌ಗೆ ಹಾಕುವುದು (ಉದಾಹರಣೆಗೆ)
discarded_card = player1_hand.pop()
discard_pile.append(discarded_card)

print(f"♻️ ಡಿಸ್ಕಾರ್ಡ್ ಪೈಲ್‌ಗೆ ಹಾಕಿದ ಕಾರ್ಡ್: {discarded_card}\n")

print("--- ಕಾರ್ಡ್ ಹೊರಹಾಕಿದ ನಂತರ ಆಟಗಾರ 1 ರ ಕೈಯಲ್ಲಿರುವ ಕಾರ್ಡ್‌ಗಳು ---")
for card in player1_hand:
    print(card)
import random

class RummyGame:
    def __init__(self):
        # ಸೂಟ್ ಮತ್ತು ರ‍್ಯಾಂಕ್‌ಗಳ ವ್ಯಾಖ್ಯಾನ
        self.suits = ['Heart', 'Diamond', 'Club', 'Spade']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        
        # ಡೆಕ್ ಸಿದ್ಧಪಡಿಸುವುದು ಮತ್ತು ಶಫಲ್ ಮಾಡುವುದು
        self.deck = [f"{rank} of {suit}" for suit in self.suits for rank in self.ranks]
        random.shuffle(self.deck)
        
        # ಜೋಕರ್ ಕಾರ್ಡ್ ಆಯ್ಕೆ
        self.joker = self.deck.pop()
        
        # ಆಟಗಾರರಿಗೆ ಕಾರ್ಡ್ ಹಂಚಿಕೆ
        self.player_hand = sorted(self.deck[:13])
        self.computer_hand = sorted(self.deck[13:26])
        
        # ಕ್ಲೋಸ್ಡ್ ಡೆಕ್ ಮತ್ತು ಡಿಸ್ಕಾರ್ಡ್ ಪೈಲ್
        self.closed_deck = self.deck[26:]
        self.discard_pile = [self.closed_deck.pop()]

    def show_table_status(self):
        print(f"\n{'='*35}")
        print(f"★ ಜೋಕರ್ ಕಾರ್ಡ್ (Joker): {self.joker} ★")
        print(f"♻️ ಡಿಸ್ಕಾರ್ಡ್ ಪೈಲ್ (Open Card): {self.discard_pile[-1]}")
        print(f"{'='*35}\n")

    def show_player_hand(self):
        print("--- ನಿಮ್ಮ ಕೈಯಲ್ಲಿರುವ ಕಾರ್ಡ್‌ಗಳು ---")
        for index, card in enumerate(self.player_hand):
            print(f"[{index}] {card}")

    def player_turn(self):
        self.show_table_status()
        self.show_player_hand()
        
        print("\nಕಾರ್ಡ್ ಎಲ್ಲಿಂದ ತೆಗೆದುಕೊಳ್ಳಲು ಬಯಸುತ್ತೀರಿ?")
        print("1. ಕ್ಲೋಸ್ಡ್ ಡೆಕ್ (Closed Deck)")
        print("2. ಡಿಸ್ಕಾರ್ಡ್ ಪೈಲ್ (Open Pile)")
        
        choice = input("ನಿಮ್ಮ ಆಯ್ಕೆ (1 ಅಥವಾ 2): ")
        
        if choice == '2':
            drawn_card = self.discard_pile.pop()
            print(f"\n[+] ನೀವು ಡಿಸ್ಕಾರ್ಡ್ ಪೈಲ್‌ನಿಂದ ತೆಗೆದ ಕಾರ್ಡ್: {drawn_card}")
        else:
            drawn_card = self.closed_deck.pop()
            print(f"\n[+] ನೀವು ಕ್ಲೋಸ್ಡ್ ಡೆಕ್‌ನಿಂದ ತೆಗೆದ ಕಾರ್ಡ್: {drawn_card}")
            
        self.player_hand.append(drawn_card)
        self.player_hand.sort()
        
        print("\n--- ಹೊಸ ಕಾರ್ಡ್ ಸೇರಿಸಿದ ನಂತರದ ನಿಮ್ಮ ಕಾರ್ಡ್‌ಗಳು ---")
        for index, card in enumerate(self.player_hand):
            print(f"[{index}] {card}")
            
        # ಕಾರ್ಡ್ ಹೊರಹಾಕುವುದು (Discard)
        while True:
            try:
                discard_idx = int(input("\nಹೊರಹಾಕಲು ಬಯಸುವ ಕಾರ್ಡ್‌ನ ನಂಬರ್ (Index) ನಮೂದಿಸಿ: "))
                if 0 <= discard_idx < len(self.player_hand):
                    discarded_card = self.player_hand.pop(discard_idx)
                    self.discard_pile.append(discarded_card)
                    print(f"♻️ ನೀವು ಹೊರಹಾಕಿದ ಕಾರ್ಡ್: {discarded_card}")
                    break
                else:
                    print("ತಪ್ಪು ನಂಬರ್! ದಯವಿಟ್ಟು ಸರಿಯಾದ ನಂಬರ್ ನೀಡಿ.")
                print("ತಪ್ಪು ನಂಬರ್! ದಯವಿಟ್ಟು ಸರಿಯಾದ ನಂಬರ್ ನೀಡಿ.")
            except ValueError:
                print("ದಯವಿಟ್ಟು ಮಾನ್ಯವಾದ ಸಂಖ್ಯೆಯನ್ನು ನಮೂದಿಸಿ.")

# ಆಟವನ್ನು ಪ್ರಾರಂಭಿಸುವುದು
game = RummyGame()
game.player_turn()
import random

class RummyGame:
    def __init__(self):
        # ಸೂಟ್ ಮತ್ತು ರ‍್ಯಾಂಕ್‌ಗಳ ವ್ಯಾಖ್ಯಾನ
        self.suits = ['Heart', 'Diamond', 'Club', 'Spade']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        
        # ಡೆಕ್ ಸಿದ್ಧಪಡಿಸುವುದು ಮತ್ತು ಶಫಲ್ ಮಾಡುವುದು
        self.deck = [f"{rank} of {suit}" for suit in self.suits for rank in self.ranks]
        random.shuffle(self.deck)
        
        # ಜೋಕರ್ ಕಾರ್ಡ್ ಆಯ್ಕೆ
        self.joker = self.deck.pop()
        
        # ಆಟಗಾರನಿಗೆ ಕಾರ್ಡ್ ಹಂಚಿಕೆ
        self.player_hand = sorted(self.deck[:13])
        
        # ಕ್ಲೋಸ್ಡ್ ಡೆಕ್ ಮತ್ತು ಡಿಸ್ಕಾರ್ಡ್ ಪೈಲ್
        self.closed_deck = self.deck[13:]
        self.discard_pile = [self.closed_deck.pop()]

    def show_table_status(self):
        print(f"\n{'='*35}")
        print(f"★ ಜೋಕರ್ ಕಾರ್ಡ್ (Joker): {self.joker} ★")
        print(f"♻️ ಡಿಸ್ಕಾರ್ಡ್ ಪೈಲ್ (Open Card): {self.discard_pile[-1]}")
        print(f"{'='*35}\n")

    def show_player_hand(self):
        print("--- ನಿಮ್ಮ ಕೈಯಲ್ಲಿರುವ ಕಾರ್ಡ್‌ಗಳು ---")
        for index, card in enumerate(self.player_hand):
            print(f"[{index}] {card}")

    def player_turn(self):
        # ಡೆಕ್ ಖಾಲಿಯಾಗಿದ್ದರೆ ಮರುಜೋಡಣೆ
        if not self.closed_deck:
            self.closed_deck = self.discard_pile[:-1]
            self.discard_pile = [self.discard_pile[-1]]
            random.shuffle(self.closed_deck)

        self.show_table_status()
        self.show_player_hand()
        
        print("\nಕಾರ್ಡ್ ಎಲ್ಲಿಂದ ತೆಗೆದುಕೊಳ್ಳಲು ಬಯಸುತ್ತೀರಿ?")
        print("1. ಕ್ಲೋಸ್ಡ್ ಡೆಕ್ (Closed Deck)")
        print("2. ಡಿಸ್ಕಾರ್ಡ್ ಪೈಲ್ (Open Pile)")
        print("ಆಟದಿಂದ ಹೊರಬರಲು 'q' ಒತ್ತಿ.")
        
        choice = input("ನಿಮ್ಮ ಆಯ್ಕೆ (1 ಅಥವಾ 2): ")
        if choice.lower() == 'q':
            return False
            
        if choice == '2':
            drawn_card = self.discard_pile.pop()
            print(f"\n[+] ನೀವು ಡಿಸ್ಕಾರ್ಡ್ ಪೈಲ್‌ನಿಂದ ತೆಗೆದ ಕಾರ್ಡ್: {drawn_card}")
        else:
            drawn_card = self.closed_deck.pop()
            print(f"\n[+] ನೀವು ಕ್ಲೋಸ್ಡ್ ಡೆಕ್‌ನಿಂದ ತೆಗೆದ ಕಾರ್ಡ್: {drawn_card}")
            
        self.player_hand.append(drawn_card)
        self.player_hand.sort()
        
        print("\n--- ಹೊಸ ಕಾರ್ಡ್ ಸೇರಿಸಿದ ನಂತರದ ನಿಮ್ಮ ಕಾರ್ಡ್‌ಗಳು ---")
        for index, card in enumerate(self.player_hand):
            print(f"[{index}] {card}")
            
        # ಕಾರ್ಡ್ ಹೊರಹಾಕುವುದು (Discard)
        while True:
            try:
                discard_input = input("\nಹೊರಹಾಕಲು ಬಯಸುವ ಕಾರ್ಡ್‌ನ ನಂಬರ್ (Index) ನಮೂದಿಸಿ: ")
                if discard_input.lower() == 'q':
                    return False
                discard_idx = int(discard_input)
                if 0 <= discard_idx < len(self.player_hand):
                    discarded_card = self.player_hand.pop(discard_idx)
                    self.discard_pile.append(discarded_card)
                    print(f"♻️ ನೀವು ಹೊರಹಾಕಿದ ಕಾರ್ಡ್: {discarded_card}\n")
                    break
                else:
                    print("ತಪ್ಪು ನಂಬರ್! ದಯವಿಟ್ಟು ಸರಿಯಾದ ನಂಬರ್ ನೀಡಿ.")
            except ValueError:
                print("ದಯವಿಟ್ಟು ಮಾನ್ಯವಾದ ಸಂಖ್ಯೆಯನ್ನು ನಮೂದಿಸಿ.")
        return True

# ಆಟವನ್ನು ನಿರಂತರವಾಗಿ ಚಲಾಯಿಸುವ ಗೇಮ್ ಲೂಪ್
game = RummyGame()
while True:
    is_continuing = game.player_turn()
    if not is_continuing:
        print("\nಆಟ ಮುಕ್ತಾಯಗೊಂಡಿದೆ. ಧನ್ಯವಾದಗಳು!")
        break
import random

class RummyGame:
    def __init__(self):
        # ಸೂಟ್ ಮತ್ತು ರ‍್ಯಾಂಕ್‌ಗಳ ವ್ಯಾಖ್ಯಾನ
        self.suits = ['Heart', 'Diamond', 'Club', 'Spade']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        
        # ಡೆಕ್ ಸಿದ್ಧಪಡಿಸುವುದು ಮತ್ತು ಶಫಲ್ ಮಾಡುವುದು
        self.deck = [f"{rank} of {suit}" for suit in self.suits for rank in self.ranks]
        random.shuffle(self.deck)
        
        # ಜೋಕರ್ ಕಾರ್ಡ್ ಆಯ್ಕೆ
        self.joker = self.deck.pop()
        
        # ಆಟಗಾರ ಮತ್ತು ಕಂಪ್ಯೂಟರ್‌ಗೆ ತಲಾ 13 ಕಾರ್ಡ್‌ಗಳ ಹಂಚಿಕೆ
        self.player_hand = sorted(self.deck[:13])
        self.computer_hand = sorted(self.deck[13:26])
        
        # ಕ್ಲೋಸ್ಡ್ ಡೆಕ್ ಮತ್ತು ಡಿಸ್ಕಾರ್ಡ್ ಪೈಲ್
        self.closed_deck = self.deck[26:]
        self.discard_pile = [self.closed_deck.pop()]

    def show_table_status(self):
        print(f"\n{'='*35}")
        print(f"★ ಜೋಕರ್ ಕಾರ್ಡ್ (Joker): {self.joker} ★")
        print(f"♻️ ಡಿಸ್ಕಾರ್ಡ್ ಪೈಲ್ (Open Card): {self.discard_pile[-1]}")
        print(f"{'='*35}\n")

    def show_player_hand(self):
        print("--- ನಿಮ್ಮ ಕೈಯಲ್ಲಿರುವ ಕಾರ್ಡ್‌ಗಳು ---")
        for index, card in enumerate(self.player_hand):
            print(f"[{index}] {card}")

    def calculate_score(self, hand):
        # ಸರಳ ಸ್ಕೋರ್ ಲೆಕ್ಕಾಚಾರ: ಮುಖಬೆಲೆ ಅಥವಾ ಫೇಸ್ ಕಾರ್ಡ್‌ಗಳಿಗೆ ಅಂಕಗಳು
        score = 0
        for card in hand:
            rank = card.split()[0]
            if rank in ['J', 'Q', 'K', 'A']:
                score += 10
            elif rank.isdigit():
                score += int(rank)
        return score

    def player_turn(self):
        if not self.closed_deck:
            self.closed_deck = self.discard_pile[:-1]
            self.discard_pile = [self.discard_pile[-1]]
            random.shuffle(self.closed_deck)

        self.show_table_status()
        self.show_player_hand()
        
        print("\n--- ನಿಮ್ಮ ಸರದಿ (Player's Turn) ---")
        print("ಕಾರ್ಡ್ ಎಲ್ಲಿಂದ ತೆಗೆದುಕೊಳ್ಳಲು ಬಯಸುತ್ತೀರಿ?")
        print("1. ಕ್ಲೋಸ್ಡ್ ಡೆಕ್ (Closed Deck)")
        print("2. ಡಿಸ್ಕಾರ್ಡ್ ಪೈಲ್ (Open Pile)")
        print("ಆಟದಿಂದ ಹೊರಬರಲು 'q' ಒತ್ತಿ.")
        
        choice = input("ನಿಮ್ಮ ಆಯ್ಕೆ (1 ಅಥವಾ 2): ")
        if choice.lower() == 'q':
            return False
            
        if choice == '2':
            drawn_card = self.discard_pile.pop()
            print(f"\n[+] ನೀವು ಡಿಸ್ಕಾರ್ಡ್ ಪೈಲ್‌ನಿಂದ ತೆಗೆದ ಕಾರ್ಡ್: {drawn_card}")
        else:
            drawn_card = self.closed_deck.pop()
            print(f"\n[+] ನೀವು ಕ್ಲೋಸ್ಡ್ ಡೆಕ್‌ನಿಂದ ತೆಗೆದ ಕಾರ್ಡ್: {drawn_card}")
            
        self.player_hand.append(drawn_card)
        self.player_hand.sort()
        
        print("\n--- ಹೊಸ ಕಾರ್ಡ್ ಸೇರಿಸಿದ ನಂತರದ ನಿಮ್ಮ ಕಾರ್ಡ್‌ಗಳು ---")
        for index, card in enumerate(self.player_hand):
            print(f"[{index}] {card}")
            
        while True:
            try:
                discard_input = input("\nಹೊರಹಾಕಲು ಬಯಸುವ ಕಾರ್ಡ್‌ನ ನಂಬರ್ (Index) ನಮೂದಿಸಿ: ")
                if discard_input.lower() == 'q':
                    return False
                discard_idx = int(discard_input)
                if 0 <= discard_idx < len(self.player_hand):
                    discarded_card = self.player_hand.pop(discard_idx)
                    self.discard_pile.append(discarded_card)
                    print(f"♻️ ನೀವು ಹೊರಹಾಕಿದ ಕಾರ್ಡ್: {discarded_card}\n")
                    break
                else:
                    print("ತಪ್ಪು ನಂಬರ್! ದಯವಿಟ್ಟು ಸರಿಯಾದ ನಂಬರ್ ನೀಡಿ.")
            except ValueError:
                print("ದಯವಿಟ್ಟು ಮಾನ್ಯವಾದ ಸಂಖ್ಯೆಯನ್ನು ನಮೂದಿಸಿ.")
        return True

    def computer_turn(self):
        print("\n--- ಕಂಪ್ಯೂಟರ್ ಸರದಿ (Computer's Turn) ---")
        # ಕಂಪ್ಯೂಟರ್ ಯಾದೃಚ್ಛಿಕವಾಗಿ (Randomly) ಕ್ಲೋಸ್ಡ್ ಡೆಕ್ ಅಥವಾ ಡಿಸ್ಕಾರ್ಡ್ ಪೈಲ್‌ನಿಂದ ಕಾರ್ಡ್ ತೆಗೆದುಕೊಳ್ಳುತ್ತದೆ
        if random.choice([True, False]) and self.discard_pile:
            comp_card = self.discard_pile.pop()
            print(f"🤖 ಕಂಪ್ಯೂಟರ್ ಡಿಸ್ಕಾರ್ಡ್ ಪೈಲ್‌ನಿಂದ ಕಾರ್ಡ್ ತೆಗೆದುಕೊಂಡಿದೆ.")
        else:
            if not self.closed_deck:
                self.closed_deck = self.discard_pile[:-1]
                self.discard_pile = [self.discard_pile[-1]]
                random.shuffle(self.closed_deck)
            comp_card = self.closed_deck.pop()
            print(f"🤖 ಕಂಪ್ಯೂಟರ್ ಕ್ಲೋಸ್ಡ್ ಡೆಕ್‌ನಿಂದ ಕಾರ್ಡ್ ತೆಗೆದುಕೊಂಡಿದೆ.")
            
        self.computer_hand.append(comp_card)
        # ಕಂಪ್ಯೂಟರ್ ತನ್ನ ಕೈಯಲ್ಲಿರುವ ಯಾದೃಚ್ಛಿಕ ಕಾರ್ಡ್ ಅನ್ನು ಹೊರಹಾಕುತ್ತದೆ
        discarded_comp_card = self.computer_hand.pop(random.randint(0, len(self.computer_hand) - 1))
        self.discard_pile.append(discarded_comp_card)
        print(f"🤖 ಕಂಪ್ಯೂಟರ್ ಒಂದು ಕಾರ್ಡ್ ಅನ್ನು ಡಿಸ್ಕಾರ್ಡ್ ಮಾಡಿದೆ.")
        print("-" * 35)

# ಆಟವನ್ನು ನಿರಂತರವಾಗಿ ಚಲಾಯಿಸುವ ಗೇಮ್ ಲೂಪ್
game = RummyGame()
while True:
    # ಆಟಗಾರನ ಸರದಿ
    is_continuing = game.player_turn()
    if not is_continuing:
        print("\nಆಟದಿಂದ ಹೊರಬಂದಿದ್ದೀರಿ.")
        break
        
    # ಆಟಗಾರ ಜಯಗಳಿಸಿದೆಯೇ ಅಥವಾ ಸ್ಕೋರ್ ಪರಿಶೀಲನೆಗೆ ಅವಕಾಶ
    p_score = game.calculate_score(game.player_hand)
    c_score = game.calculate_score(game.computer_hand)
    print(f"📊 ಪ್ರಸ್ತುತ ಸ್ಕೋರ್ -> ನಿಮ್ಮ ಹ್ಯಾಂಡ್ ಸ್ಕೋರ್: {p_score} | ಕಂಪ್ಯೂಟರ್ ಸ್ಕೋರ್: {c_score}")

    # ಕಂಪ್ಯೂಟರ್ ಸರದಿ
    game.computer_turn()
import random

class RummyGame:
    def __init__(self):
        # ಸೂಟ್ ಮತ್ತು ರ‍್ಯಾಂಕ್‌ಗಳ ವ್ಯಾಖ್ಯಾನ
        self.suits = ['Heart', 'Diamond', 'Club', 'Spade']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        
        # ಡೆಕ್ ಸಿದ್ಧಪಡಿಸುವುದು ಮತ್ತು ಶಫಲ್ ಮಾಡುವುದು
        self.deck = [f"{rank} of {suit}" for suit in self.suits for rank in self.ranks]
        random.shuffle(self.deck)
        
        # ಜೋಕರ್ ಕಾರ್ಡ್ ಆಯ್ಕೆ
        self.joker = self.deck.pop()
        
        # ಆಟಗಾರ ಮತ್ತು ಕಂಪ್ಯೂಟರ್‌ಗೆ ತಲಾ 13 ಕಾರ್ಡ್‌ಗಳ ಹಂಚಿಕೆ
        self.player_hand = sorted(self.deck[:13])
        self.computer_hand = sorted(self.deck[13:26])
        
        # ಕ್ಲೋಸ್ಡ್ ಡೆಕ್ ಮತ್ತು ಡಿಸ್ಕಾರ್ಡ್ ಪೈಲ್
        self.closed_deck = self.deck[26:]
        self.discard_pile = [self.closed_deck.pop()]

    def show_table_status(self):
        print(f"\n{'='*35}")
        print(f"★ ಜೋಕರ್ ಕಾರ್ಡ್ (Joker): {self.joker} ★")
        print(f"♻️ ಡಿಸ್ಕಾರ್ಡ್ ಪೈಲ್ (Open Card): {self.discard_pile[-1]}")
        print(f"{'='*35}\n")

    def show_player_hand(self):
        print("--- ನಿಮ್ಮ ಕೈಯಲ್ಲಿರುವ ಕಾರ್ಡ್‌ಗಳು ---")
        for index, card in enumerate(self.player_hand):
            print(f"[{index}] {card}")

    def calculate_score(self, hand):
        # ಸರಳ ಸ್ಕೋರ್ ಲೆಕ್ಕಾಚಾರ: ಮುಖಬೆಲೆ ಅಥವಾ ಫೇಸ್ ಕಾರ್ಡ್‌ಗಳಿಗೆ ಅಂಕಗಳು
        score = 0
        for card in hand:
            rank = card.split()[0]
            if rank in ['J', 'Q', 'K', 'A']:
                score += 10
            elif rank.isdigit():
                score += int(rank)
        return score

    def player_turn(self):
        if not self.closed_deck:
            self.closed_deck = self.discard_pile[:-1]
            self.discard_pile = [self.discard_pile[-1]]
            random.shuffle(self.closed_deck)

        self.show_table_status()
        self.show_player_hand()
        
        print("\n--- ನಿಮ್ಮ ಸರದಿ (Player's Turn) ---")
        print("ಕಾರ್ಡ್ ಎಲ್ಲಿಂದ ತೆಗೆದುಕೊಳ್ಳಲು ಬಯಸುತ್ತೀರಿ?")
        print("1. ಕ್ಲೋಸ್ಡ್ ಡೆಕ್ (Closed Deck)")
        print("2. ಡಿಸ್ಕಾರ್ಡ್ ಪೈಲ್ (Open Pile)")
        print("ಆಟದಿಂದ ಹೊರಬರಲು 'q' ಒತ್ತಿ.")
        
        choice = input("ನಿಮ್ಮ ಆಯ್ಕೆ (1 ಅಥವಾ 2): ")
        if choice.lower() == 'q':
            return False
            
        if choice == '2':
            drawn_card = self.discard_pile.pop()
            print(f"\n[+] ನೀವು ಡಿಸ್ಕಾರ್ಡ್ ಪೈಲ್‌ನಿಂದ ತೆಗೆದ ಕಾರ್ಡ್: {drawn_card}")
        else:
            drawn_card = self.closed_deck.pop()
            print(f"\n[+] ನೀವು ಕ್ಲೋಸ್ಡ್ ಡೆಕ್‌ನಿಂದ ತೆಗೆದ ಕಾರ್ಡ್: {drawn_card}")
            
        self.player_hand.append(drawn_card)
        self.player_hand.sort()
        
        print("\n--- ಹೊಸ ಕಾರ್ಡ್ ಸೇರಿಸಿದ ನಂತರದ ನಿಮ್ಮ ಕಾರ್ಡ್‌ಗಳು ---")
        for index, card in enumerate(self.player_hand):
            print(f"[{index}] {card}")
            
        while True:
            try:
                discard_input = input("\nಹೊರಹಾಕಲು ಬಯಸುವ ಕಾರ್ಡ್‌ನ ನಂಬರ್ (Index) ನಮೂದಿಸಿ: ")
                if discard_input.lower() == 'q':
                    return False
                discard_idx = int(discard_input)
                if 0 <= discard_idx < len(self.player_hand):
                    discarded_card = self.player_hand.pop(discard_idx)
                    self.discard_pile.append(discarded_card)
                    print(f"♻️ ನೀವು ಹೊರಹಾಕಿದ ಕಾರ್ಡ್: {discarded_card}\n")
                    break
                else:
                    print("ತಪ್ಪು ನಂಬರ್! ದಯವಿಟ್ಟು ಸರಿಯಾದ ನಂಬರ್ ನೀಡಿ.")
            except ValueError:
                print("ದಯವಿಟ್ಟು ಮಾನ್ಯವಾದ ಸಂಖ್ಯೆಯನ್ನು ನಮೂದಿಸಿ.")
        return True

    def computer_turn(self):
        print("\n--- ಕಂಪ್ಯೂಟರ್ ಸರದಿ (Computer's Turn) ---")
        # ಕಂಪ್ಯೂಟರ್ ಯಾದೃಚ್ಛಿಕವಾಗಿ (Randomly) ಕ್ಲೋಸ್ಡ್ ಡೆಕ್ ಅಥವಾ ಡಿಸ್ಕಾರ್ಡ್ ಪೈಲ್‌ನಿಂದ ಕಾರ್ಡ್ ತೆಗೆದುಕೊಳ್ಳುತ್ತದೆ
        if random.choice([True, False]) and self.discard_pile:
            comp_card = self.discard_pile.pop()
            print(f"🤖 ಕಂಪ್ಯೂಟರ್ ಡಿಸ್ಕಾರ್ಡ್ ಪೈಲ್‌ನಿಂದ ಕಾರ್ಡ್ ತೆಗೆದುಕೊಂಡಿದೆ.")
        else:
            if not self.closed_deck:
                self.closed_deck = self.discard_pile[:-1]
                self.discard_pile = [self.discard_pile[-1]]
                random.shuffle(self.closed_deck)
            comp_card = self.closed_deck.pop()
            print(f"🤖 ಕಂಪ್ಯೂಟರ್ ಕ್ಲೋಸ್ಡ್ ಡೆಕ್‌ನಿಂದ ಕಾರ್ಡ್ ತೆಗೆದುಕೊಂಡಿದೆ.")
            
        self.computer_hand.append(comp_card)
        # ಕಂಪ್ಯೂಟರ್ ತನ್ನ ಕೈಯಲ್ಲಿರುವ ಯಾದೃಚ್ಛಿಕ ಕಾರ್ಡ್ ಅನ್ನು ಹೊರಹಾಕುತ್ತದೆ
        discarded_comp_card = self.computer_hand.pop(random.randint(0, len(self.computer_hand) - 1))
        self.discard_pile.append(discarded_comp_card)
        print(f"🤖 ಕಂಪ್ಯೂಟರ್ ಒಂದು ಕಾರ್ಡ್ ಅನ್ನು ಡಿಸ್ಕಾರ್ಡ್ ಮಾಡಿದೆ.")
        print("-" * 35)

# ಆಟವನ್ನು ನಿರಂತರವಾಗಿ ಚಲಾಯಿಸುವ ಗೇಮ್ ಲೂಪ್
game = RummyGame()
while True:
    # ಆಟಗಾರನ ಸರದಿ
    is_continuing = game.player_turn()
    if not is_continuing:
        print("\nಆಟದಿಂದ ಹೊರಬಂದಿದ್ದೀರಿ.")
        break
        
    # ಆಟಗಾರ ಜಯಗಳಿಸಿದೆಯೇ ಅಥವಾ ಸ್ಕೋರ್ ಪರಿಶೀಲನೆಗೆ ಅವಕಾಶ
    p_score = game.calculate_score(game.player_hand)
    c_score = game.calculate_score(game.computer_hand)
    print(f"📊 ಪ್ರಸ್ತುತ ಸ್ಕೋರ್ -> ನಿಮ್ಮ ಹ್ಯಾಂಡ್ ಸ್ಕೋರ್: {p_score} | ಕಂಪ್ಯೂಟರ್ ಸ್ಕೋರ್: {c_score}")

    # ಕಂಪ್ಯೂಟರ್ ಸರದಿ
    game.computer_turn()
