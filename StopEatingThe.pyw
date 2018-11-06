# Benjamin Mitchell
# 7/1/2018
# Exercises and stuff.
import ctypes
import threading
import time
from random import randint

#Don't mess with these functions (windowKiller / newMsgBox).  They're generic and will take what they're assigned
#from the controlling functions below.
def windowKiller(title,close_until_seconds):
    time.sleep(close_until_seconds)
    wd=ctypes.windll.user32.FindWindowW(0,title)
    ctypes.windll.user32.SendMessageW(wd,0x0010,0,0)
    return

def newMsgBox(text, title, close_until_seconds):
    t = threading.Thread(target=windowKiller,args=(title,close_until_seconds))
    t.start()
    ctypes.windll.user32.MessageBoxW(0, text, title, 0)

#Generates the assignment string which currently supports:
#	Pushups
#	Situps
#	Squats
#	Calf Raises
#	Stress Ball / Hand exercises
# To add another type, increase the randint of the 'kind' variable by one,
# and make a new elif case.
def getNewAssignment():
	#Type of exercise
	kind = randint(0,5)

	#Number of repetitions
	num = randint(15, 30)
	assignment = str(num)

	if(kind == 0):
		assignment += ' Pushups'
	elif(kind == 1):
		assignment += ' Situps'
	elif(kind == 2):
		#Squats are hard, do 5 less
		assignment = str(int(assignment) - 5)
		assignment += ' Squats'
	elif(kind == 3):
		#Needs more lactic acid - do 2X
		assignment = str(int(assignment) * 2)
		assignment += ' Calf Raises'
	elif(kind == 4):
		#We aren't babies here, really Squeeze that ball! - do 4X
		assignment = str(int(assignment) * 4)
		assignment += ' Stress Ball Squeezes'
		assignment += '\nWith your: '
		hand = randint(0,1)
		if(hand == 0):
			assignment += ' Right Hand'
		elif(hand == 1):
			assignment += ' Left Hand'
	elif(kind == 5):
		#PHEW
		assignment = 'Take a deep breath... relax.  Keep going.  Get some work done.'

	return assignment

def main():

	#Indefinitely runs until killed via task manager
	while(1):
		#Sleep for 20-40 minutes randomly
		time.sleep(randint(1200,2400))

		#Creates the assignment randomly
		thisAssignment = 'This Assignment: ' + getNewAssignment()

		#Calls func to display the message.  Message disappears after 30 seconds
		#DO NOT MAKE THIS TITLE THE SAME AS ANY OTHER WINDOW TITLE
		#Please just trust me, don't do it.
		newMsgBox(thisAssignment,'Hey JABRONI, get up and MOVE!',30)

if __name__ == "__main__":
    main()