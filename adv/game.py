import random
from adv.battle import Battle

testinput = 1

class BuildHero(object):
	
	def __init__(self, classIn):
		"""
		Assign hero attributes
		"""
		self.attributes = self.buildHero(classIn)
		self.Name = self.attributes[0]
		self.Health = self.attributes[1]
		self.Damage = self.attributes[2]
		self.nextLocation = ''
		
	def buildHero(self, classIn):
		"""
		Generate stats to be assigned to the hero.
		"""
		attributes = []
		
		if classIn == 'Paperboy':
			attributes.append('Paperboy Johnny')      #name
			attributes.append(random.randrange(175,225))	          #health
			attributes.append(random.randrange(100,225))		      #damage
		elif classIn == 'Mailman Roger':
			attributes.append('Pravus')       #name
			attributes.append(random.randrange(225,275))	          #health
			attributes.append(110)		      #damage
		else:
			attributes.append('Plumber Jim')   #name
			attributes.append(random.randrange(275,350))	          #health
			attributes.append(160)		      #damage
		
		return attributes
		
		
	def printStats(self):
		"""
		Print stats of character
		"""
		print "\nWelcome %s" % self.Name
		print "Health is: %d" % self.Health
		print "Damage is: %d" % self.Damage		
			
class Engine(object):
	
	choiceAll = 0
	charAll = ''
	
	def __init__(self, choiceIn, charIn):
		"""
		Track locations and choices of main game events
		"""
		choiceAll = choiceIn
		charAll = charIn
		self.nextLocation = 'Start'
		nextLocation = self.nextLocation
								
	def Run(self, choiceIn, charIn):
		"""
		Function that does the running
		of the game engine
		"""

		if choiceIn == 1:
			heroDepart = Depart(charIn)
			nextLocation = heroDepart.Action()
		elif choiceIn == 2:
			heroShop = Shop(charIn)
			nextLocation = heroShop.Action()
		elif choiceIn == 3:
			heroRest = Rest(charIn)
			nextLocation = heroRest.Action()

		#move through map
		while(nextLocation != ''):
			if nextLocation == "Outskirts":
				act = Outskirts(charIn)
			elif nextLocation == "Downtown":
				act = Downtown(charIn,"Outskirts")
			elif nextLocation == "Subway":
				act = Subway(charIn,"Downtown")
			elif nextLocation == "Tunnels":
				act = Tunnels(charIn,"Subway")
			nextLocation = act.Action()

			
class Depart(BuildHero):

	def __init__(self, hero):
		#setting location
		self.nextLocation = "Outskirts"

	def Action(self):
		print "\nYou depart on your Journey"
		return self.nextLocation
		
	
class Shop(BuildHero):

	def __init__(self, hero, location):
		"""
		Bring in needed hero info
		"""
		self.location = location
		BuildHero.__init__(self, 'Paperboy')
		
	def Action(self):
		print "What would you like to purchase?\n"
		print "1. Attack Boost 2. Damage Boost"
		choice = 1##int(raw_input("<  "))
		
		if choice == 1:
			self.Damage = self.Damage + 50
			print "Damage boosted by 50!"
		elif choice == 2:
			self.Health = self.Health + 50
			print "Health boosted by 50!"
			
		return self.location
		#pass
		
class Rest(BuildHero):

	def __init__(self, hero, location):
		#setting location
		self.nextLocation = location
		BuildHero.__init__(self, 'Paperboy')
		
	def Action(self):
		print "You decide to nap...\n"
		self.Health = self.Health + 25
		print "You gained 25 health!"
		return self.nextLocation
		
class Outskirts(BuildHero):

	def __init__(self, hero):
		#setting location
		self.nextLocation = "Downtown"

	def Action(self):
		"""
		Actions that can be performed when in Outskirts object
		"""
		
		print "\nDeath is upon the city..."
		print "They say the Downtown is a start...\n"
		print "Depart to the Downtown? (1.Yes 2.No)"
		choice = testinput#int(raw_input("<  "))
		
		if choice == 1:
			return self.nextLocation
		else:
			print "uhhh"
			
class Downtown(BuildHero):

	def __init__(self,hero,location):
		#set locations
		self.prevLocation = location
		self.nextLocation = "Subway"
		self.currentLocation = "Downtown"
		self.hero = hero

	
	def Action(self):
		"""
		Handle possible actions in downtown object
		"""
		print "\nThe Downtown..."
		print "What would you like to do?"
		print "1.Continue 2.Return to %s" % self.prevLocation
		choice = testinput#int(raw_input("<  "))
		
		if choice == 1:
			battle = Battle(self.currentLocation)
			battle.Action(BuildHero)
			print "Would you like too 1.Continue 2.Shop 3.Rest?"
			postBattleChoice = testinput#int(raw_input("<  "))
			
			if postBattleChoice == 1:
				return self.nextLocation
			elif postBattleChoice == 2:
				postBattle = Shop(self.hero, self.nextLocation)
				nextLoc = postBattle.Action()
				return nextLoc
			elif postBattleChoice == 3:
				postBattle = Rest(self.hero, self.nextLocation)
				nextLoc = postBattle.Action()
				return nextLoc
				
		elif choice == 2:
			retLoc = Outskirts(self.hero)
			retLoc.Action()
		else:
			print "uhh..."
			
class Subway(BuildHero):

	def __init__(self,hero,location):
		#set locaions
		self.prevLocation = location
		self.nextLocation = "Tunnels"
		self.currentLocation = "Subway"
		self.hero = hero

	
	def Action(self):
		"""
		Handle possible actions in subway
		"""
		print "\nThe Subway.."
		print "What would you like to do?"
		print "1.Continue 2.Return to %s" % self.prevLocation
		choice = testinput#int(raw_input("<  "))
		
		if choice == 1:
			battle = Battle(self.currentLocation)
			battle.Action(BuildHero)
			print "Would you like too 1.Continue 2.Shop 3.Rest?"
			postBattleChoice = testinput#int(raw_input("<  "))
			
			if postBattleChoice == 1:
				return self.nextLocation
			elif postBattleChoice == 2:
				postBattle = Shop(self.hero, self.nextLocation)
				nextLoc = postBattle.Action()
				return nextLoc
			elif postBattleChoice == 3:
				postBattle = Rest(self.hero, self.nextLocation)
				nextLoc = postBattle.Action()
				return nextLoc
			return self.nextLocation
		elif choice == 2:
			retLoc = Downtown(self.hero, "Subway")
			retLoc.Action()
		else:
			print "uhh..."
		
class Tunnels(BuildHero):

	def __init__(self,hero,location):
		#setting locations
		self.prevLocation = location
		self.nextLocation = ""
		self.currentLocation = "Tunnels"
		self.hero = hero

	
	def Action(self):
		"""
		Handle possible actions in tunnels object
		"""
		print "\nThe Tunnels..."
		print "What would you like to do?"
		print "1.Continue 2.Return to %s" % self.prevLocation
		choice = testinput#int(raw_input("<  "))
		
		if choice == 1:
			battle = Battle(self.currentLocation)
			battle.Action(BuildHero)
			print "Would you like too 1.Continue 2.Shop 3.Rest?"
			postBattleChoice = testinput#int(raw_input("<  "))
			
			if postBattleChoice == 1:
				return self.nextLocation
			elif postBattleChoice == 2:
				postBattle = Shop(self.hero, self.nextLocation)
				nextLoc = postBattle.Action()
				return nextLoc
			elif postBattleChoice == 3:
				postBattle = Rest(self.hero, self.nextLocation)
				nextLoc = postBattle.Action()
				return nextLoc
		elif choice == 2:
			retLoc = Subway(self.hero, "Tunnels")
			retLoc.Action()
		else:
			print "uhh..."

class BattleCall(BuildHero):
	"""
	Handle preparation of variables and handle logic of battle
	"""
	
	def __init__(self, choice, location):
		pass
		
	#def 
		

		

#build = BuildHero('Paperboy')
#build.printStats()
#print "\nYour Journey begins (1.Depart, 2.Shop, 3.Rest)"
#choice = int(raw_input("<  "))
#test = Engine(choice, 'Paperboy')
#test.Run(choice, 'Paperboy')
#print "\nStill in development, thanks for playing!\n"