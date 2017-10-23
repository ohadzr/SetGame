
from Card import Card, CARD_FEATURES
import random

class Deck(object):
    """
    A Deck class - create, shuffle and draw cards
    """

    def __init__(self):
        self.reset_deck()

    def reset_deck(self):
        self.cards_array = []
        for color in CARD_FEATURES["colors"]:
            for shape in CARD_FEATURES["shapes"]:
                for shade in CARD_FEATURES["shades"]:
                    for number_of_shapes in CARD_FEATURES["number_of_shapes"]:
                        self.cards_array.append(Card(color, shape, shade, number_of_shapes))

        random.shuffle(self.cards_array)

    def draw_card(self):
        return self.cards_array.pop(0)

