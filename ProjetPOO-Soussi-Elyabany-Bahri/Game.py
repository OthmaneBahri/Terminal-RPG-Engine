from Equipment import Equipment
from Creature import Creature
from Coord import Coord
from Hero import Hero
from Map import Map
from Stairs import Stairs
from handler import heal, throw, defense, attaque, teleport, miam, dormir
from utils import getch
import theGame

import random, copy

class Game(object):
    """ Class representing game state """

    """ available equipments """
    equipments ={ 0: [Equipment("Brioche",'B',usage=lambda self, hero : miam(hero)),Equipment("potion", "+", usage=lambda self, hero: heal(hero)),Equipment("Or", "$")], \
                  1: [Equipment("Armure Bronze",'M',usage=lambda self,hero: defense(hero,'M')),Equipment("Sword","S",usage=lambda self,hero: attaque(hero,'S')),Equipment("Epee Spoof",'ç',usage=lambda self,hero: attaque(hero,'ç'))], \
                  3: [Equipment("Hammer","Q",usage=lambda self,hero: attaque(hero,'Q'))], \
                  4: [Equipment("Armure Or","G",usage=lambda self,hero: defense(hero,'G'))], \
                  10: [Equipment("Magic Sword","C",usage=lambda self,hero: attaque(hero,'C'))]
                  }
    """ available monsters """
    monsters = { 0:[Creature(".Fantome",3,strength=3),Creature("Rapido",3,strength=1)],
                 1: [Creature("Marchand",1000,'I',strength=0)],2:[Creature("Araignée",3,'A',1), Creature("Gobelin",2,'#',strength=0)], 6: [Creature("Dragon", 20, strength=3)]
                 }

    """ available actions """ #Mouvements horizontaux du héros ajoutés
    _actions = {'z': lambda h: theGame.theGame()._floor.move(h, Coord(0, -1)), \
                'q': lambda h: theGame.theGame()._floor.move(h, Coord(-1, 0)), \
                's': lambda h: theGame.theGame()._floor.move(h, Coord(0, 1)), \
                'd': lambda h: theGame.theGame()._floor.move(h, Coord(1, 0)), \
                'w': lambda h: theGame.theGame()._floor.move(h, Coord(-1, 1)), \
                'a': lambda h: theGame.theGame()._floor.move(h, Coord(-1, -1)), \
                'r': lambda h: theGame.theGame()._floor.move(h, Coord(1, -1)), \
                'v': lambda h: theGame.theGame()._floor.move(h, Coord(1, 1)), \
                                                             
                'i': lambda h: theGame.theGame().addMessage(h.fullDescription()), \
                'k': lambda h: h.__setattr__('hp', 0), \
                'u': lambda h: h.use(theGame.theGame().select(h._inventory)), \
                ' ': lambda h: None, \
                'h': lambda hero: theGame.theGame().addMessage("Actions disponibles : " + str(list(Game._actions.keys()))), \
                'b': lambda hero: theGame.theGame().addMessage("I am " + hero.name), \
                'm': lambda h: h.magie('var'), \
                't': lambda h: h.destroy(theGame.theGame().select(h._inventory)), \
                'r' :lambda h: dormir(h)
                
                }  #Magie et destruction d'inventaire ajoutés avec 'm' et 't'

    def __init__(self, level=1, hero=None):
        self._level = level
        self._messages = []
        if hero == None:
            hero = Hero()
        self._hero = hero
        self._floor = None
        self._tour=0

    def buildFloor(self):
        """Creates a map for the current floor."""
        self._floor = Map(hero=self._hero)
        self._floor.put(self._floor._rooms[-1].center(), Stairs())
        self._level += 1

    def addMessage(self, msg):
        """Adds a message in the message list."""
        self._messages.append(msg)

    def readMessages(self):
        """Returns the message list and clears it."""
        s = ''
        for m in self._messages:
            s += m + '. '
        self._messages.clear()
        return s

    def randElement(self, collect):
        """Returns a clone of random element from a collection using exponential random law."""
        x = random.expovariate(1 / self._level)
        for k in collect.keys():
            if k <= x:
                l = collect[k]
        return copy.copy(random.choice(l))

    def modElement(self,collect,dep):
        a=self.randElement(collect) 
        
        

    def randEquipment(self):
        """Returns a random equipment."""
        return self.randElement(Game.equipments)

    def randMonster(self):
        """Returns a random monster."""
        return self.randElement(Game.monsters)
    
    def randNewpos(self):
        return self.modElement(Game.monsters)

    def select(self, l):
        print("Choose item> " + str([str(l.index(e)) + ": " + e.name for e in l]))
        c = getch()
        if c.isdigit() and int(c) in range(len(l)):
            return l[int(c)]

    def play(self):
        """Main game loop"""
        self.buildFloor()
        print("--- Welcome Hero! ---")
        while self._hero.hp > 0:
            print()
            print(self._floor)
            print(self._hero.description())
            print(self.readMessages())
            c = getch()
            if c in Game._actions:
                Game._actions[c](self._hero)
                self._hero.food=self._hero.food-1
                if self._hero.food <= 0:
                    self._hero.food=0
                    self._hero.hp = self._hero.hp - 1
                    print("You're hungry, eat or use magic to save yourself")
            self._floor.moveAllMonsters()
        if self._hero.hp <= 0 and self._hero.baroud ==0:
         print("--- Game Over ---")
         print("Do you want to play again ? o : Yes / n : No") #Pour recommencer une partie
         b=getch()
         while b != 'o' and b != 'n':
             b=getch()
         if b=='o':
             self._hero.hp=15
             self._hero.strength=3
             self._hero.sante=0
             self._hero.gold=3
             self._hero.niveau=0
             self._hero.experience=0
             self._hero.mana=15
             self._hero._inventory.clear()
             self._hero.voleur.clear()
             self._hero.weapon=0
             self._hero.food=20
             self._hero.repos=0
             self._hero.limRepos=0
             self.play()
