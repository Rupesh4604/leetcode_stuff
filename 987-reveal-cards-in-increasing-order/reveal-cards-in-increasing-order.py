from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck):
        # Sort the deck
        deck.sort()
        
        # Initialize a deque to simulate the deck
        deck_deque = deque(deck)
        
        # Initialize an empty list to store the result
        result = []
        
        # Simulate the process of revealing cards
        while deck_deque:
            # Move the last revealed card to the bottom
            if result:
                result.insert(0, result.pop())
            
            # Append the top card to the result
            result.insert(0, deck_deque.pop())
        
        return result