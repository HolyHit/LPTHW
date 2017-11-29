from sys import exit
import webbrowser
import time


name = raw_input("What is your name? ")
playerlocation = "start"
mainroomvisits = 0
leftroomvisits = 0
rightroomvisits = 0
mapvisits = 0
gotKey = 0



def start():
	print """
	Welcome, %s, to the dungeon of DOOOOOOOOOM!
        You find yourself in complete darkness. However, through your mighty hero senses you sense a door
	right in front of you. Will you find your courage and venture forth?
	""" %name

	answer = raw_input("1. Yes, I will take the challenge!\n2. Oh god no, please let me out!\n>")

	if "1" in answer or "Yes" in answer or "yes" in answer or "challenge" in answer:
		Mainroom()

	if "2" in answer or "No" in answer or "no" in answer or "god" in answer:
		NoBrave()

def dead(why):
	print why, "Better luck next time brave hero!"
	exit(0)


def Mainroom():
    	playerlocation = "Mainroom"
    	global mainroomvisits
	global gotKey
	mainroomvisits = mainroomvisits +1
	print """
	You, the brave hero %s, find yourself in a big hall. It seems rather pompous for what you expected waking up in a completly dark room.
	On the walls of the hall you see enough gold to get you through your whole life, family and 3 children included.
	Looking at each of the walls, you can see one door on each. One to the left of you, one to the right and one in
	front of you. Of course there is the one behind you, but no good hero would ever walk back into the room they
	started...uh...woke up from.
	""" %name

	if mainroomvisits == 1:
		print "\tWhile looking around in the big hall you find a map in front of you! That might come in handy.\n"
	else:
		print "You have visited this room %r times" %mainroomvisits
	answer = raw_input("So what will you do now?\n1. Try the door in front of you?\n2. Try the door to your left?\n3. Try the door to your right?\n4. Open the map?\n>")

	if "2" in answer or "left" in answer:
			Leftroom()

	elif "3" in answer or "right" in answer:
			Rightroom()

	elif "1" in answer or "front" in answer:
			if gotKey == 1:
				Finalroomopen()

			if gotKey == 0:
				Finalroomclosed()

	elif "4" in answer or "map" in answer:
			Map(playerlocation)

	else:
		print "The words you are spouting do not make any sense."
		Mainroom()

def Finalroomclosed():
	print"""
	It seems like our brave hero finds himself in front of a door. But what is this?
	He is not able to open the door! There must be a key somwhere in this complex.
	"""
	raw_input("Press enter to continue")
	Mainroom()

def Finalroomopen():
	print"""
	This is it %s. The final room. The climax of this epic adventure. Are you sure you want to go in there?
    """ %name
	answer = raw_input("1. Let's goooooo.\n2. Nah, let me check some more stuff out.\n>")
	if "2" in answer or "nah" in answer or "stuff" in answer or "check" in answer:
		Mainroom()

	elif "1" in answer or "go" in answer:
		Finalroom()
	else:
		Mainroom()

def Finalroom():
	global leftroomvisits
	global rightroomvisits
	global mainroomvisits
	global mapvisits
	new = 2
	url = "https://www.youtube.com/watch?v=SBCw4_XgouA"
	webbrowser.open(url,new=new)
	print """
	You did it! You beat the game! Well, there wasn't much to be beaten, but I hope you at least checked out
	the cool Map function!
	Overall, you visited the mainroom %d times, the left room %d times, the right room %d times and looked
	at the map %d times!

	Thanks for playing <3""" %(mainroomvisits, leftroomvisits, rightroomvisits, mapvisits)





def Leftroom():
	playerlocation = "Leftroom"
	global leftroomvisits
	leftroomvisits = leftroomvisits + 1
	print """
	You enter the LEFTROOM! In it you find...
	nothing of note. Guess the developer was too busy
	creating a basic map function to put in creative writing.
	Thus you, the brave hero %s, make your way back to the MAINROOM!
	""" %name
	if leftroomvisits > 1:
		print "Also, why did you visit this room more than once?"
	answer = raw_input("1. Okay!\n2. I still want to look at the map though.\n>")
	if "1" in answer or "okay" in answer:
		Mainroom()

	elif "2" in answer or "map" in answer:
		Map(playerlocation)
	else:
		Leftroom()

def Rightroom():
	playerlocation ="Rightroom"
	global rightroomvisits
	rightroomvisits = rightroomvisits+1
	global gotKey
	gotKey = 1
	print """
	Welcome to the right room, oh brave hero. The right room looks exactly like
	you want this right room to look. Just imagine it! Isn't text a beautiful medium?
	The only thing that has to be in the room is a big golden key that fits perfectly
	into the keyhole of that one door that was closed. But you should be able
	to imagine that in your own special room, right? Now you also have to imagine
	yourself picking up those keys and putting them into your imaginary pocket.
	Great job!
	"""
	if rightroomvisits > 1:
		print "You really like your own special room, don't you? After all, you have visited it %r many times already." %rightroomvisits
	answer = raw_input("So, what is the plan of the brave hero?\n1. Leave the room to be productive\n2. Look at the cool map\n>")
	if "1" in answer or "leave" in answer or "Leave" in answer:
		Mainroom()

	elif "2" in answer or "map" in answer:
		Map(playerlocation)
	else:
		print("\tWell, I am not sure what you just said, but you probably want to go into the main room anyways.")
		Mainroom()





def Map(playerlocation):
	global mapvisits
	mapvisits = mapvisits + 1
	print "You look at the map of the dungeon you found in the mainroom:";
 	if playerlocation == "Mainroom":
		mappic = open("Ex36MapMR.txt")
		print mappic.read()

	elif playerlocation == "Leftroom" :
		mappic = open("Ex36MapLR.txt")
		print mappic.read()

	elif playerlocation == "Rightroom" :
		mappic = open("Ex36MapRR.txt")
		print mappic.read()

	else:
		print "How did you manage to clip out of bounds in a game without clipping or bounds?"
	raw_input("When you're done looking, press enter.\n>")

	if playerlocation == "Mainroom":
		Mainroom()

	elif playerlocation == "Leftroom" :
		Leftroom()

	elif playerlocation == "Rightroom" :
		Rightroom()





def NoBrave():
	print "If that is what your heart tells you to do, so be it..."
	time.sleep(5)
	print "Uh..yeah..that means you lost by the way, you can close the game now."
	time.sleep(5)
	print "No really, there is no reason to continue waiting..."
	time.sleep(5)
	print "What are you still doing here? Don't you have stuff to do?"
	time.sleep(5)
	print "Fiiiiine...I guess you really need a price..check this out:"
	time.sleep(2)
	new = 2
	url="https://www.youtube.com/watch?v=DLzxrzFCyOs"
	webbrowser.open(url,new=new)
	dead("You let yourself be rick rolled.\n")






start()
