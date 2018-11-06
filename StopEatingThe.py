# Benjamin Mitchell
# Analysis of Algorithms CSCI 261-02
# 
# 
#
import ctypes
import threading
import time
from random import randint

def windowKiller(title,close_until_seconds):
    time.sleep(close_until_seconds)
    wd=ctypes.windll.user32.FindWindowW(0,title)
    ctypes.windll.user32.SendMessageW(wd,0x0010,0,0)
    return

def newMsgBox(text, title, close_until_seconds):
    t = threading.Thread(target=windowKiller,args=(title,close_until_seconds))
    t.start()
    ctypes.windll.user32.MessageBoxW(0, text, title, 0)

def waitInterval():
	time.sleep(randint(2,3))

def getNewAssignment():
	kind = randint(0,5)
	num = randint(15, 30)
	assignment = str(num)

	if(kind == 0):
		assignment += ' Pushups'
	elif(kind == 1):
		assignment += ' Situps'
	elif(kind == 2):
		assignment = str(int(assignment) - 10)
		assignment += ' Squats'
	elif(kind == 3):
		assignment = str(int(assignment) * 2)
		assignment += ' Calf Raises'
	elif(kind == 4):
		assignment = str(int(assignment) * 4)
		assignment += ' Stress Ball Squeezes'
		assignment += '\nWith your: '
		hand = randint(0,1)
		if(hand == 0):
			assignment += ' Right Hand'
		elif(hand == 1):
			assignment += ' Left Hand'
	elif(kind == 5):
		assignment = 'Take a deep breath... relax.  Keep going.  Get some work done.'

	return assignment

def main():

	while(1):
		waitInterval()
		thisAssignment = 'This Assignment: ' + getNewAssignment()
		newMsgBox(thisAssignment,'Hey JABRONI, get up and MOVE!',4)

if __name__ == "__main__":
    main()