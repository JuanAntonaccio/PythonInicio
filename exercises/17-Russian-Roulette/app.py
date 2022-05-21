import random

bullet_position = 3

def spin_chamber():
	chamber_position = random.randint(1,6)
	return chamber_position

#  DON'T CHANGE THE CODE ABOVE
def fire_gun():
	# YOUR CODE HERE
	tiro=spin_chamber()
	if tiro==bullet_position:
		texto="You are dead!"
	else:
		texto="Keep playing!"	
	return texto




print(fire_gun())