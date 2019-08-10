import sys
import random
def roll_die(x,y):
	die1 = random.randint(0,x)
	die2 = random.randint(0,y)
	if die1 > die2:
		winner = x
	elif die2 > die1:
		winner = y
	else:
		winner = x
	return winner
#
#
#
#SETUP SEQUENCE :D
#
#
#
print("Game is starting up...")
print("---ADVENTURES AND STUFF---")
print("a pointless game by Madeline Kamprath")
print("Most people here have actual coding experience, had a project in mind beforehand, and are serious about their work,")
print("and then there's me")
idk = raw_input("Press enter to set up. ")
name = raw_input("What would you like your name to be? ")
print("Your name is saved as " + name)
age = input("How old would you like to be? Enter as an integer, please keep it between the ages of 8 and 80. ")
if age < 8:
	print("Your age is too young. Please restart the game and enter an age between 8-80.")
	sys.exit(0)
elif age >= 8 and age < 14:
	print("Your age has been saved as " + str(age) + ". You are classified as a Child.")
elif age >= 14 and age < 20:
	print("Your age has been saved as " + str(age) + ". You are classified as a Teenager.")
elif age >= 20 and age < 33:
	print("Your age has been saved as " + str(age) + ". You are classified as a Young Adult.")
elif age >= 33 and age < 65:
	print("Your age has been saved as " + str(age) + ". You are classified as an Adult.")
elif age >= 65 and age <= 80:
	print("Your age has been saved as " + str(age) +". You are classified as a Senior. Why you'd choose that is known only to you.")
elif age > 80:
	print("Your age is too old. Please restart the game and enter an age between 8-80.")
	sys.exit(0)
idk = raw_input("You are " + name + ", a " + str(age) + " year old. Press enter to continue.")
print(">>>")
print("There are 5 different areas of skill in Adventures and Stuff: Dexterity, Strength, Intelligence, Constitution, and Charisma.")
print("If it sounds similar to a tabletop game you know, then you're correct. There's no Wisdom because nobody cares about Wisdom.")
print("We'll generate a random number that will define your level in each skill. 1 is the lowest you can be, but there is no cap as to how good you can be.")
print("For example, you could be a 35 Charisma walking around making people fall in love with you left and right. The average, though, is about 3 for normal people. Anything above 6 is impressive.")
print("You'll always be able to improve, so don't freak out if you generate a low skill number. If it's really that low, you can just cheat and restart the game so it's regenerated.")
idk = raw_input("TL;DR: Press enter to generate your skill levels. ")
dex = random.randint(2,4)
stren = random.randint(1,5)
intel = random.randint(1,5)
con = random.randint(2,5)
char = random.randint(1,6)
health = random.randint(20,35)
healthcap = health
print("Dexterity: " + str(dex))
print("Strength: " + str(stren))
print("Intelligence: " + str(intel))
print("Constituion: " + str(con))
print("Charisma: " + str(char))
print("You also have " + str(health) + " hitpoints.")
idk = raw_input("When you're ready to start the game, press enter. ")
guard_intel = random.randint(1,2)
guard_dex = random.randint(1,2)
guard_stren = random.randint(1,4)
guard_con = random.randint(2,3)
guard_char = random.randint(1,3)
guard_health = random.randint(15,25)
def generateGuard():
	guard_intel = random.randint(1,100)
	guard_dex = random.randint(1,4)
	guard_stren = random.randint(3,4)
	guard_con = random.randint(2,4)
	guard_char = random.randint(1,3)
	guard_health = random.randint(15,25)
def melee_combat():
	global health
	global guard_health
	global stren
	global guard_stren
	global dex
	global guard_dex
	while health >= 0 and guard_health >= 0:
		hello = random.randint(1,2)
		if hello == 1:
			winner = roll_die(stren,guard_dex)
			if winner == stren:
				yeehaw = random.randint(1,stren)
				guard_health -= yeehaw
				idk = raw_input("You attack the guard. His health drops by " + str(yeehaw) + " points. You're feeling somewhat confident.")
			else:
				idk = raw_input("You attack the guard with a knife, but he dodges your attack. Oopsie daisy.")
		else:
			winner = roll_die(guard_stren,dex)
			if winner == guard_stren:
				yeehaw = random.randint(1,guard_stren)
				health -= yeehaw
				idk = raw_input("The guard attacks you. You lose " + str(yeehaw) + " hitpoints. You are now at " + str(health) + " hitpoints. UGHHH")	
			else:
				idk = raw_input("The guard attacks you, but you dodge the attack. You attempt to do a fancy backflip, but realize you'll never be able to.")
	if health <= 0:
		idk = raw_input("You've died in battle. \nToo bad, so sad. Sucks to be you. \nGAME OVER. RESTART TO PLAY AGAIN.")
		sys.exit(0)
	else:
		idk = raw_input("You've knocked out the guard in battle. You feel kind of bad about killing another human being, but you're a video game character with no conscience.")
def melee_combat2():
	global health
	global p_health
	global stren
	global p_stren
	global dex
	global p_dex
	while health >= 0 and p_health >= 0:
		hello = random.randint(1,2)
		if hello == 1:
			winner = roll_die(stren,p_dex)
			if winner == stren:
				yeehaw = random.randint(1,stren)
				p_health -= yeehaw
				idk = raw_input("You attack the pastor. His health drops by " + str(yeehaw) + " points. You're having mixed feelings about attacking a pastor.")
			else:
				idk = raw_input("You attack the pastor with a knife, but he dodges your attack. Oopsie daisy.")
		else:
			winner = roll_die(p_stren,dex)
			if winner == p_stren:
				yeehaw = random.randint(1,p_stren)
				health -= yeehaw
				idk = raw_input("The pastor attacks you with his God and anime powers. You lose " + str(yeehaw) + " hitpoints. You are now at " + str(health) + " hitpoints. UGHHH")	
			else:
				idk = raw_input("The guard attacks you, but you dodge the attack. You attempt to do a fancy backflip, but instead fall over and cry.")
	if health <= 0:
		idk = raw_input("You've died in battle. \nToo bad, so sad. Sucks to be you, I guess. \nGAME OVER. RESTART TO PLAY AGAIN.")
		sys.exit(0)
	else:
		idk = raw_input("You've knocked out the pastor in battle. You feel kind of bad about killing another human being, but you're a video game character with no conscience.")
def melee_combat1():
	global health
	global guard_health
	global stren
	global guard_stren
	global dex
	global guard_dex
	while health >= 0 and guard_health >= 0:
		hello = random.randint(1,2)
		if hello == 1:
			winner = roll_die(stren,guard_dex)
			if winner == stren:
				yeehaw = random.randint(1,stren)
				guard_health -= yeehaw
				idk = raw_input("You attack the bandit. His health drops by " + str(yeehaw) + " points. You're feeling somewhat confident.")
			else:
				idk = raw_input("You attack the bandit with a knife, but he dodges your attack. Oopsie daisy.")
		else:
			winner = roll_die(guard_stren,dex)
			if winner == guard_stren:
				yeehaw = random.randint(1,guard_stren)
				health -= yeehaw
				idk = raw_input("The bandit attacks you. You lose " + str(yeehaw) + " hitpoints. You are now at " + str(health) + " hitpoints. UGHHH")	
			else:
				idk = raw_input("The bandit attacks you, but you dodge the attack. You attempt to do a fancy backflip, but realize you'll never be able to.")
	if health <= 0:
		idk = raw_input("You've died in battle. \nToo bad, so sad. Sucks to be you. \nGAME OVER. RESTART TO PLAY AGAIN.")
		sys.exit(0)
	else:
		idk = raw_input("You've knocked out the bandit in battle. You feel kind of bad about killing another human being, but you're a video game character with no conscience.")
ailaDead = 0
friendDead = 0
def aila_combat():
	global a_health
	global guard_health
	global a_stren
	global guard_stren
	global a_dex
	global guard_dex
	while a_health >= 0 and guard_health >= 0:
		winner = roll_die(a_stren,guard_stren)
		if winner == a_stren:
			winner = roll_die(a_stren,guard_dex)
			if winner == a_stren:
				yeehaw = random.randint(0,a_stren)
				guard_health -= yeehaw
			else:
				unicorn = 1
		else:
			winner = roll_die(guard_stren,a_dex)
			if winner == guard_stren:
				yeehaw = random.randint(0,guard_stren)
				a_health -= yeehaw
			else:
				unicorn = 1
	if a_health <= 0:
		ailaDead = 1
		friendDead = 1
	else:
		unicorn = 1
connorDead = 0
def connor_combat():
	global c_health
	global guard_health
	global c_stren
	global guard_stren
	global c_dex
	global guard_dex
	while c_health >= 0 and guard_health >= 0:
		winner = roll_die(c_stren,guard_stren)
		if winner == c_stren:
			winner = roll_die(c_stren,guard_dex)
			if winner == c_stren:
				yeehaw = random.randint(0,c_stren)
				guard_health -= yeehaw
			else:
				unicorn = 1
		else:
			winner = roll_die(guard_stren,c_dex)
			if winner == guard_stren:
				yeehaw = random.randint(0,guard_stren)
				c_health -= yeehaw
			else:
				unicorn = 1
	if c_health <= 0:
		connorDead = 1
		friendDead = 1
	else:
		unicorn = 1
def replenishHealth():
	global time
	global food
	global water
	global health
	global healthcap
	global a_health
	global a_healthcap
	global c_health
	global c_healthcap
	idk = raw_input("You and your friend have taken some damage, so you decide to rest for a day to replenish your health.")
	print(".")
	print(".")
	print(".")
	print(".")
	print(".")
	time += 1
	food -= 1
	water -=1
	print("Day " + str(time))
	health = healthcap
	a_health = a_healthcap
	c_health = c_healthcap
	idk = raw_input("Your health has been replenished. ()")
		
#
#
#
#GAME INTRO
#
#
#
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print("When reading, press enter to continue on, and pay attention for any choices you'll have to make. () means it's the end of that string and you can press enter.")
print("IKEAVILLE, April 1, XX20")
idk = raw_input("You are sitting in a Bible Study class with your pastor, Pastor Bob. Normally you would be surrounded with other people, but apparently nobody likes Bible Study anymore. You still begrudgingly go because it makes you feel bad when you see Pastor Bob sits alone in the church, crying. (Press enter to read on.)")
idk = raw_input("Suddenly, Pastor Bob gasps. You assume he's realized something, from the lightbulb that suddenly appeared over his head. You rush to his side to make sure he's not dead, because that would make you a suspect and you have two priors already. ()")
idk = raw_input("Pastor Bob says slowly, 'I believe I just had a vision!'\nYou sigh. 'What is it?' You try not to sound TOO annoyed, and it apparently did the trick. ()")
print("Pastor Bob turns to you, and tries to sound as serious as he can with his awkwardly high voice. 'You are...THE CHOSEN ONE.' ")
if intel < 3:
	idk = raw_input("Your low intelligence causes you to be very gullible. You listen closely as he speaks, trying to hide your excitement at the thought of finally being important. ()")
else:
	idk = raw_input("You're smart and immediately deduce that something seems OFF about that. I mean, you? " + name + "? \nIMPORTANT? \nImpossible. Nevertheless, you listen to what he has to say because you're SOMEWHAT respectful. ()")
idk = raw_input("Pastor Bob explains that there is a magical artificat hidden somewhere. You, The Chosen One, has been given the task of searching for and finding this artifact, because of ancient prophecies and religion and you tuned out after a while. ()")
if intel < 3:
	idk = raw_input("You gasp with delight. Your parents always told you stories like this, you can't believe it's coming true! Maybe you'll get some fancy prince to marry you, too... \nNah. ()")
else:
	idk = raw_input("'Okay, okay, something seems off about this.' You stand up and back away. 'I mean, prophecies? Artifacts? VISIONS? I seriously think you took this from something like a Zelda game. Besides, how would I find out where it is?' Annoyed, you turn to walk out. ()")
	idk = raw_input("Pastor Bob looks up. 'Oh, I forgot to tell you about the reward money.' \nYou immediately get back into your chair to stay and listen, because you're broke as heck. ()")
idk = raw_input("'I'm also offering $100,000 to you if you successfuly bring back the artifact.' Your eyes widen. You've never had that much money, because you're the classic main character that's always been poor. \n'However, for every day you take to collect the artifacts, I'll take away $1000 from the end reward. So be as quick as possible.'()")
idk = raw_input("'You may bring a friend along to help you, as well.' ()")
idk = raw_input("Ultimately, you decide to take the job, because the game is not giving you a choice. The pastor has given you many items to help you, including: ()")
idk = raw_input("-2 week's worth of food \n-2 week's worth of water \n-A map marking the locations of both the artifact and sister churches where you can replenish your food & water supply. (The fact that he already knows this seems suspicious, but also, 100k reward money.) \n-Travel gear \n-A knife \n-A bow and 10 arrows \n-A stuffed animal to keep you company during those cold, lonely nights. ()")
idk = raw_input("'The artifact is a carving made from a pink diamond, framed in rose gold. You'll know it when you see it.' You nod, thanking Pastor Bob, and then run out the church and back home to prepare.")
arrows = 10
food = 14
water = 14
time = 0
if intel < 3:
	idk = raw_input("You absolutely cannot wait to go on this EPIC ADVENTURE, because you're an idiot and are completely oblivious to the fact that, surprise, YOU MIGHT DIE. And if you die you'll have to restart the whole game over again and nobody wants to do that. ()")
else:
	idk = raw_input("You know that there will be dangers, and frankly, this whole thing seems pretty idiotic and suspicious. But the reward money alone could let you live comfortably for many years, and maybe for a few years in Silicon Valley. ()")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
idk = raw_input("Now, you have to decide which friend you'll take with you. You only have two friends(and it's surprising you have any at all), so it's a pretty simple choice. ()")
idk = raw_input("Your first friend is named Aila. She's the strong and sturdy type, could probably put up a good fight with The Rock. However, she's not very flexible, and honestly insanely stupid. She's nice, though, and people like being around her. ()")
idk = raw_input("Your second friend is named Connor. He's very agile, and has always been smarter than average. He's also somewhat charismatic, and enjoys meeting new people. However, he has low constituion, and his 'strength' is a joke. ()")

friend = 0;
while (friend == 0):
	friend = input("Which friend would you like to take with you on your journey? 1 for Aila, 2 for Connor. ")
	if friend == 1:
		idk = raw_input("You ultimately decide to take Aila with you on your journey. She was surprisingly easy to convince to join you. ()")
		friend_name = "Aila"
	elif friend == 2:
		idk = raw_input("You ultimately decide to take Connor with you on your journey. He could clearly see that this was an idiotic thing to do, but he too instantly agreed once you mentioned the reward money...Are you and your friends bad people?")
		friend_name = "Connor"
	else:
		friend = 0;
		
a_dex = 1
a_stren = 4
a_con = 5
a_char = 3
a_intel = 2
a_health = 33
a_healthcap = 33
c_dex = 5
c_stren = 1
c_con = 2
c_char = 3
c_intel = 4
c_health = 23
c_healthcap = 23
#
#
#
#PART ONE
#
#
#
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print("LATER THAT DAY...")
idk = raw_input("You and " + friend_name + "are hastily preparing your things, getting ready for your EPIC ADVENTURE. Connor then questions if you're really ready. ()")
idk = raw_input("You would be angry at him for suggesting that you aren't prepared for this trip, but he's right. Your skills could use some improvement. He then suggests an idea. ()")
idk = raw_input("You and your companion could each improve one of your skills by 1 with some training. It would only take 7 days if you worked hard enough, and you wouldn't need to use any of the food for the travel since you'd train from home. ()")
idk = raw_input("It sounds like a great idea, but then you remember that Pastor Bob is taking off $1000 for every day you take to complete this mission. That would mean an automatic $7000 less than the $100,000 reward. On the other hand, it would mean you would be more prepared for the mission, and possibly go quicker.()")
training = 0;
while (training == 0):
	training = input("Would you like to spend a week training one skill, or leave immediately on your journey? 1 for training, 2 for leaving immediately. ")
	if training == 1:
		idk = raw_input("You take Connor's advice and decide to spend a week training one of your skills to improve. ()")
		time += 7
		print("Dexterity: " + str(dex))
		print("Strength: " + str(stren))
		print("Intelligence: " + str(intel))
		print("Constituion: " + str(con))
		print("Charisma: " + str(char))
		idk = raw_input("Here is a reminder of your skill levels. Remember, 1 is the lowest you can be, and 3 is considered average. ()")
		train = 0
		while (train == 0):
			train = input("What would you like to improve by 1 point? 1 for Dexterity, 2 for Strength, 3 for Intelligence, 4 for Constitution, and 5 for Charisma. ")
			if train == 1:
				dex += 1
				idk = raw_input("You decided to up your Dexterity by 1, making your new Dexterity level " + str(dex) + "! You're super duper flexible now, like a rubber band. WOAH ()")
			elif train == 2:
				stren += 1
				idk = raw_input("You decided to up your Strength by 1, making your new Strength level " + str(stren) + "! You punch a tree to make it break, because that's what strong people do! ()")
			elif train == 3:
				intel += 1
				idk = raw_input("You decided to up your Intelligence by 1, making your new Intelligence level " + str(intel) + "! You're so smart, Einstein would ask you for help with his math homework. ()")
			elif train == 4:
				con += 1
				idk = raw_input("You decided to up your Constitution by 1, making your new Constitution level " + str(con) + "! You're so sturdy, you could be used to build a house! ()")
			elif train == 5:
				char += 1
				idk = raw_input("You decided to up your Charisma by 1, making your new Charisma level " + str(char) + "! More people like you now, or at least they pretend to. ()")
			else:
				train = 0
	elif training == 2:
		idk = raw_input("In the end, you decide that $7000 is too much money to waste and leave immediately with " + friend_name + "for the first artifact.")
		time += 0

	else:
		training = 0;

print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
date = 1+time
print("Day " + str(time))
idk = raw_input("You and " + friend_name + " decide to go find the artifact, which is somewhere inside of a desert village called Talethray. If you go straight there, it will take 7 days of travel. ()")
idk = raw_input("There's also a sister church where you can replenish your food and water supplies, but it's some ways off the path. You would be able to get up to 10 day's worth of food and 10 day's worth of water there, but it would take 5 additional days of travel. That's an extra $5000 lost. ()")
replenish = 0;
while (replenish == 0):
	replenish = input("Would you like to go replenish your food and water supplies or go straight to Talethray? 1 for supplies, 2 for Talethray. ")
	if replenish == 1:
		idk = raw_input("You and " + friend_name + " decide to go visit the sister church on the way to Talethray. You begin the journey to the nearest one, a small desert church called Safeway Worship Center. ()")
		time += 5
		food -= 5
		water -= 5
		print(".")
		print(".")
		print(".")
		print(".")
		print(".")
		print(".")
		print("Day " + str(time))
		idk = raw_input("You finally arrive at Safeway Worship Center. It's quite small, matching the tiny oasis village it is located in. You enter, and are greeted by a middle-aged man, presumably the pastor. ()")
		idk = raw_input("You explain your purpose, seeking food and water for the long journey ahead. He calls one of the workers in the church, who quickly provides you with 10 day's worth of food and water for your journey. ()")
		food += 10
		water += 10
		print("Food: " + str(food) + " day's worth")
		print("Water: " + str(water) + " day's worth")
		idk = raw_input("Here's a reminder of how much food and water you have now. ()")
		idk = raw_input("With your supplies replenished, your morale up, and your stuffed animal to comfort you, you and " + friend_name + " set off for Talethray.")
	elif replenish == 2:
		idk = raw_input("Wasting $5000 like that? That's going to be a no. You and " + friend_name + " go straight to Talethray.")
	else:
		replenish = 0;
#
#
#
#PART TWO
#
#
#
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
time += 7
food -= 7
water -= 7
print("Day " + str(time))
print("Food left: " + str(food) + " day's worth")
print("Water left: " + str(water) + " day's worth")
idk = raw_input("Finally after a week's travels, you and " + friend_name + " arrive at Talethray. It's a bustling city of around 100,000, with colorfully painted homes dotting the sandy landscape. In the distance you can see what appears to be a small castle, probably home to the ruler of the village. ()")
idk = raw_input(friend_name + " looks closely at the spot marked on the map, but can't seem to navigate and figure out where to go. You try as well, but neither of you are familiar with the city and can't figure out how to get around. ()")
idk = raw_input("After a few hours of attempting to find the artifact's location, you and " + friend_name + " give up. " + friend_name + "suggests asking a local, which you agree to. You see a middle-aged woman in a bright orange tunic walking with an infant in her arms. You and " + friend_name + " walk over to her. ()")
idk = raw_input("You approach the woman. \n'Hello, we're a bit lost.' " + friend_name + " explains. 'Could you give us directions to this spot on this map of the city?' ()")
annoyance = random.randint(1,4)
if annoyance < 3:
	idk = raw_input("The woman seems annoyed by you two, as she's already quite busy. Regardless, she gives the both of you directions to the spot. \n'It shouldn't be more than an hour's walk.' she quickly remarks. 'Lord knows why you'd want to go there, though. It's just some old museum.' \n Museum? You glance at the woman, confused. You both thank her for her help and go on your way. ()")
elif annoyance == 3:
	idk = raw_input("The woman is obviously somewhat busy, though she stops and politely helps you and " + friend_name + " out. \n'It shouldn't be more than an hour's walk.' she says articulately, pointing in the general direction of the location. 'Lord knows why you'd want to go there, though. It's just some old museum.' \n Museum? You glance at the woman, confused. You both thank her for her help and go on your way. ()")
else:
	idk = raw_input("'Well, of course, sweethearts!' The woman smiles. She looks at your map, readjusting it to get a better look. \n'It shouldn't be more than an hour's walk.' she smiles, pointing in the general direction of the location. 'Lord knows why you'd want to go there, though. It's just some old museum.' \n Museum? You glance at the woman, confused. You both thank her for her help and go on your way. ()")
print("AN HOUR LATER...")
idk = raw_input("You and " + friend_name + " arrive at the location. Just as the woman said, it's a large museum, built of fine stones. The two of you reluctantly climb up the stairs and step inside. ()")
idk = raw_input("As you step inside, cool air hits your face, as you are faced with a layout remniscent of...well, a museum. There's many fine objects in there, but nothing resembling the pink diamond you were told about by Pastor Bob. ()")
idk = raw_input("If this place has the artifact, it's not just going to be out in the open. It has to be inside of some safe room, right?' " + friend_name + " points out. 'We just need to find it.' You nod, grabbing a paper map of the museum. ()")
idk = raw_input("You look the map over. 'There's a big empty space on the east side, it might be inside of there.' The both of you stalk carefully to the east wing so the area is in sight. ()")
idk = raw_input("There's a long wall covering the east wing, decorated with various pieces of art. The only door that you can currently see has a large 'NO UNAUTHORIZED ACCESS' painted on, with a tall man guarding it. \n'Gosh diddly darn,' you mumble. \n 'We'll probably have to lie to be able to get in,' " + friend_name + " mutters. ()")
if friend == 1:
	if char <= a_char:
		liar = str(friend_name)
		liars = a_char
	else:
		liar = "you"
		liars = char
else:
	if char <= c_char:
		liar = str(friend_name)
		liars = c_char
	else:
		liar = "you"
		liars = char
idk = raw_input("The two of you decide that " + liar + " will do the primary talking to the guard, simply because " + liar + "has the most charisma between you two. ()")
idk = raw_input("You and " + friend_name + " walk up to the door. \n'Excuse me, you two.' The guard stops you and your friend. 'I'm sorry, but unless you're an employee here, you can't come back here.' \nYou act oblivious as " + liar + " step forwards to speak with the guard. ()")
idk = raw_input("'Oh, I'm so sorry, sir!' " + liar + " gasp, appearing shocked. 'It's just that my husband works here and told me that he left his hat in this room. He's terribly protective of his hat, you know, since it was handmade by his own late mother.' " + liar + " fake a small tear or two. You're not exactly loving the direction in which this is going, but it's better than nothing. ()")
winner = roll_die(char,guard_intel)
if winner == char:
	key = 0
	idk = raw_input("The guard laughs. 'Ah, yes, the guy with the weird hat! Tom, right?' \nDID THAT ACTUALLY HECKING WORK? WHAT THE HECK. HOW. \nYou smile and nod. 'Yes, my precious Tommy.'")
	idk = raw_input("'I can understand how ol' Tom would nag his spouse just for that STUPID hat, haha!...' It seems as if the guard has some strong feelings regarding Tom and his hat. \nHe opens the door. 'Right this way. The museum is open 24 hours, so you'll be able to exit anytime.' You and " + friend_name + " thank the man and walk inside. " + friend_name + " turns to you and smiles. 'See? Easy as that.'")
else:
	idk = raw_input("The guard appears skeptical. 'Are you sure you're his partner? I don't know...' \n" + liar + " appear hurt, maybe even shocked. \n'I'm sorry, it's just that something seems off. Why wouldn't he give you the access key to the building instead?' \nOops. \n'I'm sorry, but until you have that I can't let you in.' Defeated, you and " + friend_name + " walk away. ()")
	idk = raw_input("You and " + friend_name + " quickly get away from the guard at the door, instead searching for any other entrances to the room. ()")
	idk = raw_input(" 'This is really cool! Oooooh, we're like secret spies.' You try to ignore " + friend_name + " 's idiotic whispers as the two of you sneak around, like secret spie- OH DANG " + friend_name + " WAS RIGHT ()")
	idk = raw_input("You turn around a corner, passing over an EMPLOYEES ONLY line, and scan the wall ahead. \n'No doors,' you mutter to " + friend_name + ", and the two of you walk along the wall. Before turning, " + friend_name + " peeks around the corner. After staying still for a while, they turn back to you with a slightly...upset? Afraid? pAnIcKy??? expression on their face. ()")
	idk = raw_input(" '" + name + "! There's a guard walking around the back wall! What do you think we should do?' \nYou pause in thought(as if you're smart enough to be able to think, you're just waiting for the game to load a solution for you.) ()")
	idk = raw_input("You remember the bow and arrows Pastor Bob gave you. You quietly retrieve them from your bag. \n'I'll shoot a bow and arrow at him, and try??? to hit him. It should work, I'm smart kind of maybe sort of.' \n'Don't kid yourself.' \n'Fair.' ()")
	key = 0
	winner = roll_die(dex,guard_dex)
	if winner == dex:
		guard_health -= dex
		idk = raw_input("The arrow hit the guard in the arm. He sees you, and you run forward to engage in COMBATtm. " + friend_name + " runs away, searching along the long, long wall for any doors or entrances.")
		melee_combat()
	else:
		idk = raw_input("The arrow misses, because you didn't bother to train yourself how to shoot an arrow. Stupid " + name + ". The guard sees you, and you run forward to engage in COMBATtm. " + friend_name + " runs away, searching along the long, long wall for any doors or entrances.")
		melee_combat()
	idk = raw_input("You look for any useful items that the guard's body might have. You find a key in his pocket, presumably for something in the safe room. ()")
	key += 1
	idk = raw_input("ACQUIRED ONE KEY")
	idk = raw_input("As you stuff the key into your pocket, you hear " + friend_name + " running back. \n'I found a door into the safe room!' \nYou both run up to the door. It's small, similar to the one the man was guarding in front. You both enter the room.")
#
#
#
#THE SAFE ROOM
#
#
#
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print("THE SAFE ROOM")
idk = raw_input("You and " + friend_name + " close the door behind you. In front of you lies a cavernous maze of files, artifacts, and art. The room looks to be the size of a Costco, but without the free samples and Vitamixes. ()")
idk = raw_input("'Should we split up to cover more ground?' " + friend_name + " suggests. It's a decent plan; no one person could cover any area the size of a Costco alone. But on the other hand, if either of you run into any challenges, you'll have to fight alone. ()")
split_up = 0;
while (split_up == 0):
	split_up = input("Would you like to stick together or split up? 1 for together, 2 to split up. ")
	if split_up == 1:
		idk = raw_input("You and " + friend_name + " believe that it's a smarter idea to stay together, just in case you have to fight any more guards. ()")
		idk = raw_input("As you turn a corner, you and " + friend_name + " are suddenly face-to-face with two guards! They look like they spend 20 hours a day working out. Oh no. You're scared. ()")
		idk = raw_input("'I'll fight the one on the right, you take the other,' " + friend_name + " sputters before punching the guy on the right. He wasn't affected. This isn't going to turn out well. But for now, you focus on the guy on the left.")
		generateGuard()
		melee_combat()
		if friend == 1:
			generateGuard()
			aila_combat()				
		else:
			generateGuard()
			connor_combat()	
		if friendDead == 1:
			idk = raw_input("You fought the guard! You somehow beat him. Maybe it's because of all the veggies you've been eating lately. You check his body for anything of value, and find a key. ()")
			key += 1
			idk = raw_input("1 KEY ACQUIRED ()")
			idk = raw_input("You glance over to your friend to see how they're doing, if they need any help. Luckily, they knocked out the guard...but they're dead. \nCurse this goshdang game, killing off your acquaintance. ()")
			idk = raw_input("Fighting back tears(no no don't cry water breaks the computer), you check the bodies of the other guard and your friend. \nYou retrieve the food and water from your friend's bag, and find another key in the other guard's pocket.")
			key += 1
			idk = raw_input("1 KEY ACQUIRED ()")
		else:
			idk = raw_input("You fought the guard! You somehow beat him. Maybe it's because of all the veggies you've been eating lately. You check his body for anything of value, and find a key. ()")
			key += 1
			idk = raw_input("1 KEY ACQUIRED ()")
			idk = raw_input("You glance over to " + friend_name + " to see if they need any help. They knocked out the guard, and they seem to be in decent shape. They give you a key they found on the guard's body.")
			key += 1
			idk = raw_input("1 KEY ACQUIRED ()")
			idk = raw_input("You and your friend have taken some damage, so you decide to rest for a day to replenish your health.")
			replenishHealth()
	elif split_up == 2:
		idk = raw_input("You and " + friend_name + " decide to split up to cover more ground. You agree to meet near the entrance, the same place you walked in, within 6 hours. With that, you and " + friend_name + " part ways. ()")
		print(".")
		print(".")
		print(".")
		print("6 HOURS LATER")
		idk = raw_input("Time goes by. You've searched and searched, but haven't found anything even close to the beautiful pink diamond carving you were told about. Defeated, you go back to the meeting spot and wait.")
		if friend == 1:
			generateGuard()
			aila_combat()				
		else:
			generateGuard()
			connor_combat()	
		if friendDead == 1:
			idk = raw_input("Hours pass, and " + friend_name + " is nowhere to be found. You begin to worry that something may have happened to them. You leave the meeting spot and begin searching for them.")
			idk = raw_input("After some searching, you hear muffled noises to your left. You follow it, and are shocked to see " + friend_name + " laying lifelessly on the floor. \nGASP \nThere is also the body of another guard next to them; it looks like " + friend_name + " knocked them out. However, there's still one other guard standing there, frantically trying to resuscitate their colleague. \nBecause that would make them a suspect. ()")
			idk = raw_input("You think the guard notices you. There's no running away now. You don't really want to fight, but at the same time you want to avenge one of the only friends you have, because you're a decent person. ()")
			idk = raw_input("You see two ways to go about this; \n1-Fight the guard, then take the loot from the bodies and keep searching for the artifact. \n2-As quickly as you can, raid the body of " + friend_name + " for remaining food and water and RUN. Seems kind of coldhearted, but that would be a waste of water. And if third grade science taught you anything, it's that wasting water is bad.")
			loot = 0;
			while (loot == 0):
				loot = input("Do you think it's a better idea to fight the guard, or loot " + friend_name + "'s body for food and water? 1 for fighting, 2 for raiding the body. ")
				if loot == 1:
					idk = raw_input("You decide to engage in COMBATtm with the guard. LET'S FIGHT Y'ALL ()")
					generateGuard()
					melee_combat()
					idk = raw_input("You win the fight, because you're super strong and eat hardboiled eggs for breakfast. You're safe for now. ()")
					idk = raw_input("You check the bodies for anything of importance. You find food and water in " + friend_name + "'s bag, as well as a key on each of the guards. You stash them away. ()")
					key += 2
					idk = raw_input("2 KEYS ACQUIRED ()")
					idk = raw_input("You've taken some damage, so you decide to rest for a day.")
					replenishHealth()
					idk = raw_input("You continue searching the Costco-like room for the artifact.")
				elif loot == 2:
					idk = raw_input("You, as quickly as humanly possible, loot the bodies. You find food and water in " + friend_name + "'s bag, as well as a key on the dead guard. The living guard notices you and tries to attack you. ()")
					idk = raw_input("You dodge the attack and run away as fast as you can. ")
					idk = raw_input("You've taken some damage, so you decide to rest for a day.")
					replenishHealth()
					idk = raw_input("Once you're sure you're safe, you continue searching the Costco-like room for the artifact.")
					key += 1
				else:
					loot = 0;
		else:
			idk = raw_input(friend_name + " arrives at the meeting spot, a bit out of breath. \n'I fought two of the guards!' \n'Ooh, cool cool cool cool cool. Did they have anything on them?' \n'Just these two keys.' You thank " + friend_name + " and tuck the keys into your pocket.")
			key += 2
			idk = raw_input("2 KEYS ACQUIRED ()")
			idk = raw_input("You and your friend have taken some damage, so you decide to rest for a day to replenish your health.")
			replenishHealth()
			idk = raw_input("You continue searching the Costco-like room for the artifact. ()")
			
	else:
		split_up = 0;
if friendDead == 1:
	idk = raw_input("You search for the next few hours. You finally see something strange. There is a small, locked room on the far south end of the Costco warehouse. It has a huge RESTRICTED ACCESS sign painted onto it. The artifact has got to be in there! You fumble around in your pocket to see if you have the key. ()")
	idk = raw_input("You pull out a key you took from one of the guards. Carefully, you unlock the door and walk inside. ()")
	key -= 1
else:
	idk = raw_input("You and " + friend_name + " continue searching for the artifact. You finally see something strange. There is a small, locked room on the far south end of the Costco warehouse. It has a huge RESTRICTED ACCESS sign painted onto it.\n'The artifact has got to be in there!' " + friend_name + " exclaims. \nYou nod and fumble around in your pocket to see if you have the key. ()")
	idk = raw_input("You pull out a key you took from one of the guards. \n'I'll stand watch,' " + friend_name + " says. You thank them, and then unlock the door and walk inside.")
	key -= 1
idk = raw_input("The room is dimly lit and dusty. It appears as if nobody's been in here for ages. There are only a few boxes in here, so checking them for the artifact should be fairly quick. ()")
print("A few minutes later...")
idk = raw_input("You open a box and pull out another clear box. It is locked, and inside is the artifact you've been searching for. ()")
if key <= 0:
	idk = raw_input("Sadly, you don't have a key to open the box. You attempt to hide it under your jacket. It is quite obvious, but it's better than nothing. ()")
	obvious = 1
else:
	idk = raw_input("You pull out another key and unlock the box. You cautiously pull out the pink diamond carving. It's so beautiful, you don't even have to use imagery to describe it to the players. ()")
	key -= 1
	obvious = 0
	idk = raw_input("You tuck the artifact into your pocket. It fits perfectly. You walk out the door confidently. ()")	
if friendDead == 0:
	idk = raw_input("As you exit the small room, you show " + friend_name + " the artifact. 'Woah!' they gasp, because diamonds are pretty. \nThe two of you walk out of the Costco together.")
if obvious == 0:
	idk = raw_input("You exit the Costco, pass over the EMPLOYEES ONLY line once more, and walk out. You politely smile at the guards and employees, and exit the museum to be greeted by the hot and arid air of Talethray. ()")
else:
	idk = raw_input("You exit the Costco and pass over the EMPLOYEES ONLY line, but a guard notices you acting suspicious. He asks for you to empty your pockets, and you refuse. You begin running away. ()")
	generateGuard()
	winner = roll_die(dex,guard_dex)
	if winner == dex:
		idk = raw_input("You are faster than the guard, and ultimately are able to escape the museum without getting caught by the guards.")
	else:
		idk = raw_input("You try to escape, but the guards catch you. They confiscate the artifact and take you away. Too bad, y'all are going to jail. \nGAME OVER \nRestart to play again.")
		sys.exit(0)
if friendDead == 0:
	idk = raw_input("You were going to go back home with " + friend_name + ", but it turns out that they found love with a villager in Talethray. You bid your farewells and begin the journey home. ()")
idk = raw_input("You have the choice once more to stop at Safeway Worship Center to refill food and water supplies(7 days travel, then 5 extra), or to go straight home(7 days travel). ()")
print("Food: " + str(food) + " days worth")
print("Water: " + str(water) + " days worth")
idk = raw_input("Here is a reminder of your food and water levels. Remember, for every day you don't have food and water, you will take damage. However, for every day you take to complete this mission, Pastor Bob is taking $1000 off of the reward.()")
replenish = 0;
while (replenish == 0):
	replenish = input("Would you like to go replenish your food and water supplies or go straight to Talethray? 1 for supplies, 2 for Talethray. ")
	if replenish == 1:
		idk = raw_input("You decide to go visit the sister church on the way to Talethray. You begin the journey to Safeway Worship Center. ()")
		time += 7
		food -= 7
		water -= 7
		print(".")
		print(".")
		print(".")
		print(".")
		print(".")
		print(".")
		print("Day " + str(time))
		idk = raw_input("You finally arrive at Safeway Worship Center. It's quite small, matching the tiny oasis village it is located in. You enter, and are greeted by a middle-aged man, presumably the pastor. ()")
		idk = raw_input("You explain your purpose, seeking food and water for the long journey ahead. He calls one of the workers in the church, who quickly provides you with 10 day's worth of food and water for your journey. ()")
		food += 10
		water += 10
		print("Food: " + str(food) + " day's worth")
		print("Water: " + str(water) + " day's worth")
		idk = raw_input("Here's a reminder of how much food and water you have now. ()")
		idk = raw_input("With your supplies replenished, your morale up, and your stuffed animal to comfort you, you set off for home.")
		time += 5
		food -= 5
		water -= 5
		artifact = 1
	elif replenish == 2:
		idk = raw_input("Wasting $5000 like that? That's going to be a no. You go straight to Talethray.")
		print(".")
		print(".")
		print(".")
		print(".")
		print(".")
		print(".")		
		time += 3
		food -= 3
		water -= 3
		print("Day " + str(time))
		idk = raw_input("You'd been traveling for days, when suddenly a bandit on your path pops up like an annoying ad. He threatens to kill you if you don't give him your money. ()")
		idk = raw_input("'I don't have any money, I only have a priceless diamond-and-gold artifact.' \nWHAT THE HECK WHY DID I DO THAT ()")
		fight = 0
		artifact = 1
		while fight == 0:
			fight = input("Do you hand over the artifact or fight the bandit? 1 for giving the artifact, 2 for fighting. ")
			if fight == 2:
				raw_input("You decide that you will fight the bandit. you FIGHT WOOH ()")
				generateGuard()
				melee_combat1()
			elif fight == 1:
				raw_input("Fearing for your life, you reluctantly hand over the artifact. The bandit takes it and runs away on his magnifent pink lion. Guess you don't have an artifact anymore. ()")
				artifact = 0
			else:
				fight = 0
		time += 4
		food -= 4
		water -= 4
	else:
		replenish = 0;
		water -= 7
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
p_stren = random.randint(2,10)
p_dex = random.randint(1,3)
p_health = 25
print("Day " + str(time))
idk = raw_input("You are standing in front of Pastor Bob, telling him all about the adventure you went on, the fate of " + friend_name + ", and so much more. \n'This is very interesting, " + name + ", but do you have the artifact or not? ()")
if artifact == 1:
	idk = raw_input("You smile, and hand over the artifact. PAstor Bob takes it in his hands, in awe of its glory. \n'A carving so intricate that the author doesn't have to use imagery...my, my, it's truly wonderful.' ()")
	money = 100000 - (time * 1000)
	idk = raw_input("You beam, proud of your hard work. 'So, sir, what would my reward money amount be now?' \n'Hm, you were gone for " + str(time) + " days, so that... $100,000...math... your reward would be " + str(money) + ". Good job, " + name + ".' ()")
	idk = raw_input("You stand awkwardly. 'Um...sir, when would I receive this money?' \n'Oh, yes, I'll get it to you after I sell this.' \nWait. Sell? ()")
	idk = raw_input("Pastor Bob nods. 'That whole 'Chosen One' stuff was stupid. I just wanted you to steal this artifact so that I could sell it on eBay.' \nYou gasp. You've never felt so betrayed! Except when your girlfriend decided to play on the opposite team in laser tag last year. But that's beside the point. You begin yelling at him, telling him how horrible of a person he is, manipulating and using people for his own illegal activities. ()")
	idk = raw_input("'Oh, settle down, settle down. I'll still give you the money as a reward. And reporting my actions wouldn't work, since you're an accessory to the crime. You'd go to video game prison as well.' Dangit, he's actually right. ()")
finalcount = 0
while finalcount == 0:
	finalcount = input("You see three options. You can take the money, report him to the police, or kill the pastor(you're a horrible person). 1 for money, 2 for police, 3 for killing. ")
	if finalcount == 1:
		print("'Smart choice,' says Pastor Bob. You go home and forget about it. Two weeks later you receive $" + str(money) + " in the mail. You live a comfortable life and never speak of the crimes you've committed again.")
		print("GAME OVER")
		sys.exit(0)
	elif finalcount == 2:
		death = age + 5
		print("You report Pastor Bob to the police. While they eventually arrest him, you are also arrested and placed into a nearby jail. You die at the age of " + str(death) + " in a dispute with your cellmate about who won the fifth Halloween Heist.")
		print("GAME OVER")
		sys.exit(0)
	elif finalcount == 3:
		idk = raw_input("You begin fighting with the pastor. \n'You've made a bad choice, buddy!' says Pastor Bob. 'I have the power of God and anime on my side!' ()")
		melee_combat2()
		print("You somehow actually won. You hide the body in the church. You are never caught.")
		print("GAME OVER")
		sys.exit(0)
	else:
		finalcount = 0