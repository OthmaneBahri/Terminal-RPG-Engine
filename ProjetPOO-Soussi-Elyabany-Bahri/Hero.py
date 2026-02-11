from Creature import Creature
from Equipment import Equipment
from utils import getch

class Hero(Creature):
    """The hero of the game.
        Is a creature. Has an inventory of elements. """

    def __init__(self, name="Hero", hp=15, abbrv="@", strength=2,defense=0,experience=0,niveau=0,weapon=0,sante=0,gold=3,mana=15,baroud=0,invisibilite=0,food=20):
        Creature.__init__(self, name, hp, abbrv, strength)
        self._inventory = []
        self.experience=experience
        self.niveau=niveau
        self.weapon=weapon
        self.sante=sante
        self.gold=gold
        self.mana=mana
        self.baroud = baroud
        self.invisibilite=invisibilite
        self.defense=defense
        self.food=food

    




    def description(self):
        """Description of the hero"""
        return Creature.description(self) + str(self._inventory)

    def fullDescription(self):
        """Complete description of the hero"""
        res = ''
        for e in self.__dict__:
            if e[0] != '_':
                res += '> ' + e + ' : ' + str(self.__dict__[e]) + '\n'
        res += '> INVENTORY : ' + str([x.name for x in self._inventory])
        return res

    def checkEquipment(self, o):
        """Check if o is an Equipment."""
        if not isinstance(o, Equipment):
            raise TypeError('Not a Equipment')

    def take(self, elem):
        """The hero takes adds the equipment to its inventory"""
        
        if len(self._inventory) <= 10 :
            if elem.abbrv=='$':
                self.gold=self.gold + 1
                return True
            self.checkEquipment(elem)
            self._inventory.append(elem)
            

    def destroy(self,elem):
            self._inventory.remove(elem)
            print("You have destroyed " +str(elem))
    def use(self, elem):
        """Use a piece of equipment"""
        if elem is None:
            return
        self.checkEquipment(elem)
        if elem not in self._inventory:
            raise ValueError('Equipment ' + elem.name + 'not in inventory')
        if (elem in self._inventory) and (elem.abbrv == 'M'):
            self.defense= self.defense + 1
        if elem.use(self):
            self._inventory.remove(elem)
    


