#Featercoin Arcade Machine Payment proof of concept
#prints to be commented out when in use, they are for test purposes only
import ftcapi
import datetime
import calendar
import time
import RPi.GPIO as GPIO ## Import GPIO library

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(7, GPIO.OUT) ## Setup GPIO Pin 7 to OUT for LED


#set up variables to start
balanceCheck = ftcapi.toFTC()
previousBalance = balanceCheck
creditCost = 1 #cost per credit in ftc
countingCredits = 0 #how many credits was bought with deposit
balance_difference = 0



#main loop
while True:	
	#gets current account balance
	balanceCheck = ftcapi.toFTC()
	
	print "Current Balance", balanceCheck
	print "Previous balance before checking credits", previousBalance
	
	#while is used to count if more than one credit is depositted at a time
	while (balanceCheck -creditCost) >= previousBalance: #checks that deposit is higher than cost of  credit or ignores
		print "New Balance", balanceCheck
		countingCredits += 1
		previousBalance = previousBalance + creditCost
		print "Credits", countingCredits, "previous balance", previousBalance	 
	
	#this part 'spends the credits' which at the moment just lights up an LED for 10 seconds
	while countingCredits > 0:
		GPIO.output(7,True) ## Turn on GPIO pin 7
		time.sleep(10)
		GPIO.output(7,False)
		countingCredits -=1 #decrement credits by 1
		print "Credits Left", countingCredits
		time.sleep(2) #wait enough time for us to see LED go off for multiple credit payments 
	
	time.sleep(15) #waits 15 seconds before repeating
