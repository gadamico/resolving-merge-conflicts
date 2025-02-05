class Snake:
    """A dangerous and/or harmless serpent."""
    pass


class Cobra(Snake):
    """Definitely dangerous, yup."""
    
    def bite(self, other):
        """Deliver a dose of venom."""
        return str(other) + ' was bitten!'

    
class BoaConstrictor(Snake):
    """This one gives really good hugs."""
    
    def squeeze(self, other):
        """Give a hug."""
        print(str(other) + ' has been squozen!')

    
class BoatConstrictor(BoaConstrictor):
    """Loose snakes sink ships?"""
    pass
