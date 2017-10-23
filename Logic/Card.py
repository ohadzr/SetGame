
COLORS = ["red", "purple", "green"]
SHAPES = ["diamond" , "oval", "squiggle"]
SHADES = ["solid", "striped", "open"]
NUMBER_OF_SHAPES = [1, 2, 3]

class Card:
    """
    A Card class has a color, shape, # of shapes on the card
    """

    def __init__(self, color, shape,shading, number_of_shapes):
        """
        create a card object - raise an error if args are not currect

        :param color: string - should be "red" / "purple" / "green"
        :param shape: string - should be
        :param shading:
        :param number_of_shapes: string - should be "solid" / "striped" / "open"
        """

        if color not in COLORS or shape not in SHAPES \
            or shading not in SHADES \
            or number_of_shapes not in NUMBER_OF_SHAPES:
            raise CardArgsNotCurrect()

