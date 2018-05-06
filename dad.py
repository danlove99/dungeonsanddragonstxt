from random import randrange
import sys
from time import sleep


class Player:
	def __init__(self, name, damage, health, Class, weapon, xplvl, gender):
		self.name = name 
		self.damage = damage
		self.health = health
		self.Class = Class
		self.xplvl = xplvl
		self.gender = gender

	def __str__(self):
		return ('{} is a {} {} that weilds a {} that does {} damage and has {} health'.format(self.name, self.gender, self.Class, self.weapon ,self.damage, self.health))
	
	def heal(self):
		self.health = self.health + (100 - self.health)
		return self.health
		print('post battle healing has taken effect full health regained')

	
	def attack(self, other):
		print ('{} attacks {} !!'.format(self.name, other.name)) ; sleep(0.1)
		other.health -= self.damage
		print('{} has {} health left'.format(other.name, other.health))

	def loosehealth(self, other):
		print ('{} attacks {} !!'.format(other.name, self.name))
		self.health -= other.damag
		print('{} has {} lives left'.format(self.name, self.health))

	def win(self, other):
		print('{} defeated {} and {} gained {} experiance points'.format(self.name, other.name, self.name, other.XP))
		self.xplvl += other.XP
		print ('{} now has {} XP'.format(self.name, self.xplvl))

	def lose(self):
		print('{} died!'.format(self.name))

	def battle(self, other):
		boo = True
		while boo == True:
			chance = randrange(10)
			if chance >= 0 and chance <= 5:
				
				self.attack(other)
				
				if other.health <= 0:
					boo = False
					self.win(other)
					self.heal
				elif self.health <= 0:
					boo = False
					self.lose
					other.health = 100
				else:
					pass
			elif chance >= 6 and chance < 11:
				other.attack(self)

			if self.xplvl == 10:
				self.damage = self.damage + 10
				self.health = self.health +100
			elif self.xplvl == 30:
				self.damage = self.damage + 30
				self.health = self.health + 100
			elif self.xplvl == 70:
				self.damage = self.damage + 50
				self.health = self.health + 100

	def lvlupcheck(self):
		if self.xplvl == 10:
			self.damage = self.damage + 10
			self.health = self.health +100
		elif self.xplvl == 30:
			self.damage = self.damage + 30
			self.health = self.health + 100
		elif self.xplvl == 70:
			self.damage = self.damage + 50
			self.health = self.health + 100


class Foe:
	def __init__(self, name, damage, health, XP):
		self.name = name
		self.damage = damage
		self.health = health
		self.XP = XP

	def __str__(self):
		print('a {} appears!'.format(self.name))

	def attack(self, other):
		print ('{} attacks {} !!'.format(self.name, other.name))
		other.health -= self.damage
		print("{} has {} lives left".format(other.name, other.health))



def skip(x):
	if x in Skip:
		print('SATAN RISES')
		guy.battle(satan)
		print(guy)
		weaponlvl_check(guy)



Skip = ['skip']

# Enemies
# stage 1

goblin = Foe('goblin', 10, 50, 10)
hellhound = Foe('hellhound', 20, 60, 20)
dragon = Foe('dragon', 30, 70, 40)

# stage 2

orc = Foe('orc', 70, 80, 50)
snowtroll = Foe('snow troll', 95, 90, 60)
demon = Foe('demon', 100, 95, 95)


# boss
satan = Foe('satan', 110, 100, 100)

Goblin = ['Goblin', 'goblin', 'g', 'G', '1']
Hellhound = ['hellhound', 'Hellhound', 'H', 'h', '2']
Dragon = ['Dragon', 'dragon', 'd', 'D', '3']
Orc = ['orc']
Snowtroll = ['snow troll']
Demon = ['demon']

now = ['now', 'n', '1', 'N', 'Now']
startag = ['continue', 'go', '2', 's', 'S']

boy = ['boy', 'man', 'male', 'm', 'M']
girl = ['girl', 'woman', 'w', 'W']

def typeffect(x):

	for y in x:
		sleep(0.1)
		sys.stdout.write(char)
		sys.stdout.flush()

def weaponlvl_check(guy):
	if guy.xplvl < 10 or guy.xplvl == 10:
		print('your weapon does 10 percent more damage \n')
	elif guy.xplvl < 30 and guy.xplvl > 10 or guy.xplvl == 30:
		print('your weapon does 30 percent more damage \n')
	elif guy.xplvl > 30 and guy.xplvl < 100:
		print('your weapon does 75 percent more damge')
	else:
		print('your weapon is in peak condition and does maximum damage')

def main():

	ans = input('what is your name? \n')
	gen = input('what is your gender? \n ')
	cla = input('what is your class? \n warrior \n thief \n assassin \n mage\n')
	weapon = ''
	guy = Player(ans, 10, 100, cla, weapon, 0, gen)
	if cla in 'warrior':
		guy.Class = 'warrior'
		guy.weapon = 'Mighty sword'
	elif cla in 'thief':
		guy.Class = 'thief'
		guy.weapon = 'swift blade'
		print('extra damage points to my favourite class')
		guy.damage += 100
	elif cla in 'assassin':
		guy.Class = 'assassin'
		guy.weapon = 'trusty bow'
	elif cla in 'mage':
		guy.Class = 'mage'
		guy.weapon = 'elemental staff'
	else:
		print ('invalid class choice so youre a warrior k')
		guy.Class = 'warrior'
		guy.weapon = 'mighty sword'

	if gen in boy:
		guy.gen = 'male'
	elif gen in girl:
		guy.gen = 'female'
	


	
	turn = 0
	print (guy)
	path = input('which path do you choose....\n A: the dark forest \n B: the slimey caves \n')
	while turn < 3:
		if path in 'a':
			who = input('who do you want to fight? \n goblin \n hellhound \n dragon \n')
			if who in Goblin:
				guy.battle(goblin)
				guy.heal
				weaponlvl_check(guy)
				turn += 1
			elif who in Hellhound:
				guy.battle(hellhound)
				guy.heal
				weaponlvl_check(guy)
				turn += 1
			elif who in Dragon:
				guy.battle(dragon)
				guy.heal
				weaponlvl_check(guy)
				turn += 1
			print ('you continue your venture out of the dark forest and fall into a giant fire pit...\n')
		elif path in 'b':
			who2 = input('who do you want to fight? \n orc \n snow troll \n demon \n')
			if who2 in Orc:
				guy.battle(orc)
				guy.heal
				weaponlvl_check(guy)
				turn += 1
			elif who2 in Snowtroll:
				guy.battle(snowtroll)
				guy.heal
				weaponlvl_check(guy)
				turn += 1
			elif who2 in Demon:
				guy.battle(demon)
				guy.heal
				weaponlvl_check(guy)
				turn += 1
			print('you venture through to the end of the slimey caves and fall into a giant pit...\n')


	print('SATAN RISES')
	guy.battle(satan)
	print(guy)
	weaponlvl_check(guy)
	




main()