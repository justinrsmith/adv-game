import random
#from adv.game import BuildHero

testinput = 1

class Battle():

	def __init__(self,  location):
		self.location = location
		self.enemyAttr = []
		self.Health = 200
		self.Damage = 100
		self.Name = 'Paperboy Johnny'
#		self.test = bhero
	#	self.Health = bhero.Health

	def attack(*args):
		"""
		Function for handling attacking
		"""
		heroHP, enemyHP, heroDMG, enemyDMG = args
		flag = 0
	
		while(flag == 0):
			print '%r deals %r damage' % (self.Name, heroDMG)
			enemyHP = enemyHP - heroDMG
			print "enemy %r" % enemyHP
			if enemyHP <= 0:
				flag = 1
				print "You defeated.."
				break
			# monster attacks
			print 'Enemy %r deals %r damage\n' % (randEnemy, enemyDMG)
			heroHP = heroHP - enemyDMG
			print "hero %r" % heroHP
			if heroHP <= 0:
				flag = 1
				print "You died..."
				quit(0)
			print "1. Attack 2. Defend 3. Item"
			atkChoice = testinput#int(raw_input("<  "))	
				
	def Action(hero):
		"""
		Handle battle actions
			-much work to be done
		"""
		
		#generate dicts of stats available to assign
		attrA = {'Type':'A', 'Health':random.randrange(175,250), 'Damage':random.randrange(50,100)}
		attrB = {'Type':'B', 'Health':random.randrange(200,275), 'Damage':random.randrange(75,125)}
		attrC = {'Type':'C', 'Health':random.randrange(225,300), 'Damage':random.randrange(100,150)}
		
		# a dict with character type and name
		enemy = {'A':'Goon', 'A':'Thug', 'B':'Henchman', 
		          'B':'Crony', 'C':'Crime Lord', 'C':'Crime Boss'}
		randEnemy = enemy[random.choice(enemy.keys())]
		print "\n%s attacks!" % randEnemy
		
		# based on monster type distribute stats
		# THIS NEEDS TO BE REVISITED
		if randEnemy == 'Goon' or randEnemy == 'Thug':
			self.enemyAttr.append(attrA['Health'])
			self.enemyAttr.append(attrA['Damage'])
		elif randEnemy == 'Henchman' or randEnemy == 'Crony':
			self.enemyAttr.append(attrB['Health'])
			self.enemyAttr.append(attrB['Damage'])
		else:
			self.enemyAttr.append(attrC['Health'])
			self.enemyAttr.append(attrC['Damage'])
		
		print "%s has %s health" % (randEnemy, self.enemyAttr[0])
		print "\nWhat will you do?!"
		print "1. Attack 2. Defend 3. Item"
		atkChoice = testinput#int(raw_input("<  "))

		if atkChoice == 1:
			#pass
			self.Attack(self.Health, self.enemyAttr[0], self.Damage, self.enemyAttr[1], randEnemy)
		elif atkChoice == 2:
			pass
		#	self.Defend(self.hero.Health, self.enemyAttr[0], self.hero.Damage, self.enemyAttr[1], randEnemy)
		else:
			print "item"
		
	def Attack(self, heroHP, enemyHP, heroDMG, enemyDMG, randEnemy):
		"""
		Function for handling attacking
		"""
		flag = 0
		
		while(flag == 0):
			print heroHP
			print '%r deals %r damage' % (self.Name, heroDMG)
			enemyHP = enemyHP - heroDMG
			print "enemy %r" % enemyHP
			if enemyHP <= 0:
				flag = 1
				print "You defeated.."
				break
			print 'Enemy %r deals %r damage\n' % (randEnemy, enemyDMG)
			heroHP = heroHP - enemyDMG
			print "hero %r" % heroHP
			if heroHP <= 0:
				flag = 1
				print "You died..."
				quit(0)
			print "1. Attack 2. Defend 3. Item"
			atkChoice = testinput#int(raw_input("<  "))
			if atkChoice == 2:
				self.defend(heroHP, enemyHP, heroDMG, enemyDMG, randEnemy)
				flag = 1
				break
			
	def Defend(self, heroHP, enemyHP, heroDMG, enemyDMG, randEnemy):
		"""
		Function to handle defend option
		"""
		
		flag = 0
		newenemyDMG = enemyDMG / 2
		
		while(flag==0):
			print '%r Defends' % (self.hero.Name)
			print 'Enemy %r deals %r damage\n' % (randEnemy, newenemyDMG)
			heroHP = heroHP - newenemyDMG
			if heroHP <= 0:
				flag = 1
				print "You died..."
				quit(0)
			print "1. Attack 2. Defend 3. Item"
			atkChoice = testinput#int(raw_input("<  "))
			if atkChoice == 1:
				self.Attack(heroHP, enemyHP, heroDMG, enemyDMG, randEnemy)
				flag = 1
				break