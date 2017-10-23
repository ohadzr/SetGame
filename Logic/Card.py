
CARD_FEATURES = {"colors": ["red", "purple", "green"],
                 "shapes": ["diamond" , "oval", "squiggle"],
                 "shades": ["solid", "striped", "open"],
                 "number_of_shapes": [1, 2, 3]}




class Card(object):
    """
    A Card class has a color, shape, # of shapes on the card
    """

    def __init__(self, color, shape, shading, number_of_shapes):
        """
        create a card object - raise an error if args are not currect

        :param color: string - should be "red" / "purple" / "green"
        :param shape: string - should be "diamond" / "oval" / "squiggle"
        :param shading: string - should be "solid" / "striped" / "open"
        :param number_of_shapes: int - should be 1 / 2 / 3
        """

        if color not in CARD_FEATURES["colors"]:
            raise WrongColorException
        if shape not in CARD_FEATURES["shapes"]:
            raise WrongShapeException
        if shading not in CARD_FEATURES["shades"]:
            raise WrongShaingException
        if number_of_shapes not in CARD_FEATURES["number_of_shapes"]:
            raise WrongNumberOfShapesException

        self.color = color
        self.shape = shape
        self.shading = shading
        self.number_of_shapes = number_of_shapes

        self.photo = self.find_card_photo()

    def find_card_photo(self):
        """
        Find the card's photo based on his features

        :return: string - the path of the photo
        """
        #TODO: implement this when GUI is ready
        return None



class CardArgsException(Exception):
    pass

class WrongColorException(CardArgsException):
    pass

class WrongShapeException(CardArgsException):
    pass

class WrongShaingException(CardArgsException):
    pass

class WrongNumberOfShapesException(CardArgsException):
    pass