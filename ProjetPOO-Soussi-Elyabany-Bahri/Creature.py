from Element import Element
import theGame
from utils import getch
from Equipment import Equipment
from handler import attaque , teleport



class Creature(Element):
    """A creature that occupies the dungeon.
        Is an Element. Has hit points and strength."""

    def __init__(self, name, hp, abbrv="", strength=1,defense=1,experience=0,niveau=0,weapon=0,sante=0,gold=3,mana=15,baroud=0,invisibilite=0,voleur=[],food=30,repos=0,limRepos=0):
        Element.__init__(self, name, abbrv)
        self.hp = hp
        self.strength = strength
        self.sante=sante
        self.gold=gold
        self.mana=mana
        self.baroud=baroud
        self.invisibilite=invisibilite
        self.voleur=voleur
        self.defense=defense
        self.food=30
        self.repos=0
        self.limRepos=limRepos
        #Toutes les caractéristiques des créatures qui ont servi à créer/modifier les méthodes, et limRepos sert à ne pas tricher en dormant à l'infini dans une salle vide
        

    def description(self):
        """Description of the creature"""
        if self.abbrv=='@':
         return Element.description(self) + "(HP: " + str(self.hp) + ")" + "(XP: " + str(self.experience)+ ")" + "(LV: " + str(self.niveau) + ")" + "(POW: " + str(self.strength) + ")" + " (DEF: " + str(self.defense) + ")" +"(Faim: " + str(self.food) + ")"
        else:
         return Element.description(self)

    def meet(self, other):
        """The creature is encountered by an other creature.
        "" The other one hits the creature. Return True if the creature is dead."""
        if (other.strength - self.defense) > 0: #Pour ne pas avoir des pv qui s'ajoutent quand on est frappé
         self.hp = self.hp  - other.strength + self.defense - self.sante 
        if other.abbrv=='@' and other.weapon==4 and self.abbrv != 'I': #Pour ne pas téléporter le marchand avec l'épée spoof
            self.hp = 0
            teleport(self,False)
            theGame.theGame().addMessage("You teleported the monster away !")
            return False 
        if self.abbrv=='#':
            for k in other.voleur: #Rajoute les objets volés dans l'inventaire du héro
                other._inventory.append(k)
            other.voleur.clear()
            other.gold +=10
            theGame.theGame().addMessage("You recovered your inventory !")
            
         
        if other.abbrv == '#' : #Pour que le gobelin nous vole notre inventaire et se tp
            if len(other.voleur) ==0:
                for k in self._inventory:
                    other.voleur.append(k)
                self._inventory.clear()
                theGame.theGame().addMessage("The Goblin stole all your inventory, chase him !")

            teleport(other,False)

        
            
            
                
    
        
            
            
            
            

        if other.abbrv=='I' or self.abbrv =='I': #Marchand itinérant qui nous demande de taper sur une touche
            print("Gold : " + str(other.gold) + " The shop is open! You can buy 1 item between these : a : Hammer (Prix : 5 gold), b :Sword (Prix : 2 gold), c: I will diseappear !")
            z=getch() 
            if z =="a" and other.gold >= 5:
                other._inventory.append(Equipment("Hammer","Q",usage=lambda self,hero: attaque(hero,'Q')))
                other.gold = other.gold - 5
                return True
            if z == "b" and other.gold >= 2:
                 other._inventory.append(Equipment("Sword","S",usage=lambda self,hero: attaque(hero,'S')))
                 other.gold = other.gold - 2
                 return True
            if z=='c':
                theGame.theGame().addMessage("Bye Bye aventurer !")          
                return True
            
        if self.experience == 4 : #Les valeurs d'xp/lvl pour nous rajouter des pv/force
            self.niveau= 1
            self.experience = 6
            self.strength+=3
            self.hp=17
            theGame.theGame().addMessage("The " + self.name + " gain 1 lvl, 3 strength and has 17 hp")             

        if self.experience == 12:
            self.niveau= 2
            self.experience=14
            self.strength+=3
            self.hp=19
            theGame.theGame().addMessage("The " + self.name + " gain 1 lvl, 3 strength and has 19 hp")             
            
        if self.experience == 20:
            self.niveau=3
            self.experience=24
            self.strength+=3
            self.hp=23
            theGame.theGame().addMessage("The " + self.name + " gain 1 lvl, 3 strength and has 23 hp")
        if (other.strength - self.defense) > 0:
         self.hp = self.hp  - other.strength + self.defense - self.sante
        if other.abbrv=='.': #Fais apparaitre le fantome quand on le croise
            other.name='Fantome'
            other.abbrv='F'
        if other.abbrv=='A':
            self.sante=1
        if self.hp <=0: #Pour looter le monster
            other.experience += 2
            other.mana += 0.5
            other.gold +=1
            

        
        
                     

            
        theGame.theGame().addMessage("The " + other.name + " hits the " + self.description())
        if self.hp > 0:
            return False
        if self.hp <= 0 and self.baroud ==1: #Pouvoir Last Hope qui nous permet de revenir à la vie
            self.baroud = 0
            self.hp=1
            self.sante=0
            self.food=20
            teleport(self,False)           
            theGame.theGame().addMessage("Your Last Hope saved you. Now run !")
            return False
        return True


                 
    def magie(self,a): #Les différents sorts
      print("Mana :" + str(self.mana) + " Choose your spell.  ! : heal 2 hp(2 mana) / * : Convert 3 hp into 3 strength (3 mana) /  é : Anti-poison (1 mana) / p : Magic Sword ! (10 Mana) / & : Last Hope (15 Mana) / i : Be Invisible for 10 turns ! (10 Mana) / o: Eat a magic apple (2 mana) / t : Teleport yourself")
      a=getch()
      if a == "!" and self.mana >=2:
       self.hp=self.hp + 2
       self.mana= self.mana - 2
      if a =="*" and self.mana >= 3:
         self.strength = self.strength + 3
         self.hp = self.hp - 3
         self.mana = self.mana - 3
      if a == "é" and self.mana >= 1:
          self.sante = 0
          self.mana = self.mana - 1
      if a=='p' and self.mana >=10:
          self._inventory.append(Equipment("Magic Sword","C",usage=lambda self,hero: attaque(hero,'C')))
          self.mana = self.mana - 10
      if a=='&' and self. mana >= 15:
          self.baroud = 1
          self.mana = self.mana - 15
      if a=='i' and self.mana >=10:
          self.mana = self.mana -10
          self.invisibilite = 10
      if a=='t' and self.mana >= 5:
          teleport(self, False)
          self.mana = self.mana - 5
      if a == 'o' and self.mana >= 2:
          self.food+=30
          self.mana=self.mana-2
          
          
      
