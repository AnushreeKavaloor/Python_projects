import random
class Character:
	def __init__(self, name, health):
		self.name = name
		self.health = health
	
	def take_damage(self, hits):
		self.health-=hits
	
	def check_if_alive(self):
		return self.health>0
class Player(Character):
	def __init__(self, name, health, potions):
		super().__init__(name, health)
		self.potions=potions
		
Enemy = Character
		
p = Player("Raj", 100, 3)
e = Enemy("Shatru", 100)
while p.check_if_alive()==True and e.check_if_alive()==True:
	print(f"{p.name}: {p.health} and {e.name}: {e.health}")

	while True:
		choice = input("1. Attack \n2.Heal \nEnter your choice(1 or 2): ")
		if choice=="1":
			damage = random.randint(10,20)
			e.take_damage(damage)
			print(f"{p.name} hit {e.name} for {damage}")
			break
		elif choice=="2":
			if p.health==100:
				print("Already full health.")
				continue
			elif p.potions>0:
				p.potions-=1
				p.health = min(100, p.health + 20)
				print(f"{p.name} healed for 20! Health is now {p.health}")
			else:
				print("No potions left!")
				continue
			break
		else:
			print("Invalid! Try again")
	if not e.check_if_alive():
		print(f"{p.name} wins!")
		break
	damage = random.randint(10,20)
	p.take_damage(damage)
	print(f"{e.name} hit {p.name} for {damage}")
	if not p.check_if_alive():
		print(f"{e.name} wins!")
		break
