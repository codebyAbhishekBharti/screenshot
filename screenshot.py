import pyautogui
import datetime
import time
command =input("Do you want to take screenshot of this page \n If yes type 'y' otherwise 'n' :-  ")
try :
	if command.lower().startswith("y"):
		time.sleep(1)
		now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
		myScreenshot = pyautogui.screenshot()
		myScreenshot.save(r"E:\\picture-"+now+".png")
		print("Screenshot has been taken see the directry")
	else:
		st=int(input("After what interval of time do you want to take screenshot (in second) :-"))
		while True:
			now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
			myScreenshot = pyautogui.screenshot()
			myScreenshot.save(r"E:\\picture-"+now+".png")
			print("Screenshot has been taken see the directry")
			time.sleep(st)
except KeyboardInterrupt:
	pass