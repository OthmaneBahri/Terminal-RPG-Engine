from Element import Element
import theGame
from utils import getch

class Equipment(Element):
    """A piece of equipment"""

    def __init__(self, name, abbrv="", usage=None):
        Element.__init__(self, name, abbrv)
        self.usage = usage

    def meet(self, hero):
        """Makes the hero meet an element. The hero takes the element."""
        if self.abbrv =='$': #Ramasser les gold
            hero.gold = hero.gold + 1
            return True
        if len(hero._inventory) <= 1 and self.abbrv:
         hero.take(self)
         theGame.theGame().addMessage("You pick up a " + self.name)
         return True
        else: #Pour définir une limite max à l'inventory
          print("You're carrying too much objects ! Throw something from your inventory or destroy this object by pressing p")
          w=getch()
          if w == 'p':#Détruit l'objet en face
              return True
            
          
          

        
        

         
            

    def use(self, creature):
        """Uses the piece of equipment. Has effect on the hero according usage.
            Return True if the object is consumed."""
        if self.usage is None:
            theGame.theGame().addMessage("The " + self.name + " is not usable")
            return False
        else:
            theGame.theGame().addMessage("The " + creature.name + " uses the " + self.name)
            return self.usage(self, creature)
