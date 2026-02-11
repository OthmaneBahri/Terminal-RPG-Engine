import theGame
from Equipment import Equipment
from utils import getch

def heal(creature):
    """Heal the creature"""
    creature.hp += 3
    creature.sante=0
    return True
def dormir(creature):
    creature.repos=1
    if creature.limRepos>3:
       theGame.theGame().addMessage(" You have already slept too much today, you'll be late for school ! :)")

        
def miam(creature):
    creature.food+=20

def throw(creature,loss, direction):
    creature._inventory.append(loss)
def monnaie(creature):
    creature.gold = creature.gold + 1
    return True

    
def teleport(creature, unique):

    """Teleport the creature"""

    r = theGame.theGame()._floor.randRoom()

    c = r.randCoord()

    if theGame.theGame()._floor.get(c) != theGame.theGame()._floor.ground:
        return teleport(creature,unique)
    theGame.theGame()._floor.rm(theGame.theGame()._floor.pos(creature))

    theGame.theGame()._floor.put(c, creature)

    return unique 
    
    
def defense(creature,metal):
    if metal == 'G':
        if creature.defense==3:
         creature.take(Equipment("Armure Or","G",usage=lambda self,hero: defense(hero,'G')))
        if creature.defense==1:
            creature.take(Equipment("Armure Bronze","M",usage=lambda self,hero: defense(hero,'M')))            
        creature.defense=3
        return True
    if metal == 'M':
        if creature.defense==3:
         creature.take(Equipment("Armure Or","G",usage=lambda self,hero: defense(hero,'G')))
        if creature.defense==1:
          creature.take(Equipment("Armure Bronze","M",usage=lambda self,hero: defense(hero,'M'))) #Gère le changement d'armure
        creature.defense=1
        return True

         
    
def attaque(person,arme):
    epee=Equipment("Sword","S",usage=lambda self,hero: attaque(hero,'S')) #Gère le changement d'armes
    marteau=Equipment("Hammer","H",usage=lambda self,hero: attaque(hero,'Q'))
    Epeem=Equipment("Magic Sword","C",usage=lambda self,hero: attaque(hero,'C'))
    if arme=='S':
        if person.weapon==3 :
            theGame.theGame().addMessage(" But the hero already equiped the sword !")
            person.strength = person.strength-3
            person._inventory.append(epee)
        if person.weapon==5:
            person._inventory.append(marteau)
            person.strength=person.strength-5
        if person.weapon ==10:
            person._inventory.append(Epeem)
            person.strength = person.strength - 10
        if person.weapon==4:
            person._inventory.append(Equipment("Epee Spoof","ç",usage=lambda self,hero: attaque(hero,'ç')))
            person.strength=person.strength-1

        person.strength+=3
        person.weapon=3
        return True
    if arme=='ç':
        if person.weapon==5:
            theGame.theGame().addMessage("But the hero already equiped the hammer !")
            person._inventory.append(marteau)
            person.strength=person.strength-5
            
        if person.weapon==3:
            person.strength = person.strength-3
            person._inventory.append(epee)
        if person.weapon ==10:
            person._inventory.append(Epeem)
            person.strength = person.strength - 10
        if person.weapon==4:
            person._inventory.append(Equipment("Epee Spoof","ç",usage=lambda self,hero: attaque(hero,'ç')))
            person.strength=person.strength-1
        person.weapon=4
        person.strength+=1
        
        return True
    
    if arme == 'Q':
        if person.weapon==5:
            theGame.theGame().addMessage("But the hero already equiped the hammer !")
            person._inventory.append(marteau)
            person.strength=person.strength-5
            
        if person.weapon==3:
            person.strength = person.strength-3
            person._inventory.append(epee)
        if person.weapon ==10:
            person._inventory.append(Epeem)
            person.strength = person.strength - 10
        if person.weapon==4:
            person._inventory.append(Equipment("Epee Spoof","ç",usage=lambda self,hero: attaque(hero,'ç')))
            person.strength=person.strength-1

        person.weapon=5

        person.strength+=5        
        return True
  
    if arme == 'C':
        if person.weapon==3 :
            person._inventory.append(epee)
            person.strength = person.strength - 3
        if person.weapon==5:
            person._inventory.append(marteau)
            person.strength=person.strength-5
        if person.weapon ==10:
            theGame.theGame().addMessage("But the hero already equiped the hammer !")
            person.strength= person.strength-10
            person._inventory.append(Epeem)
        if person.weapon==4:
            person._inventory.append(Equipment("Epee Spoof","ç",usage=lambda self,hero: attaque(hero,'ç')))
            person.strength=person.strength-1
        person.strength +=10
        person.weapon=10
        return True
        
        
    
        
        


    
                        
            

        
                                 
        
