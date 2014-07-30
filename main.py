#Featercoin Arcade Machine Payment proof of concept
#prints to be commented out when in use, they are for test purposes only
#additional modules required, requests, setup,Pillow, QRcode See readme file for install instructions
import ftcapi
import PriceAPI
import create_qr
import datetime
import calendar
import time
import RPi.GPIO as GPIO ## Import GPIO library
import os
import math

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(16, GPIO.OUT) ## Setup GPIO Pin 16 to OUT for LED
GPIO.output(16,False)

#######################################################################
########################################################################
#These are the variables to change
#To change currency change 'aud' in code below to one of the option 
#below
#aud = (Australia), eur = Euro, gbp = Great Britain 
#nzd = New Zealand, usd = United Sates
WhichCurrency = "aud"
#Cost per credit in Fiat, ignored if creditCost is not set to 0
FiatCost = 0.5

#Only need to set creditCost if you you are using a fixed FTC for credit, not one set by local Fiat
#if using credit cost worked out by local Fiat leave ceditCost as 0
creditCost = 0 #cost per credit in ftc
FTCAccountNo ='6oQqqYYPvnPRukPp2qiEWVzMkHnqCx2VKn' #enter your FTC account number here
#Remeber you need a unique account for each machine
Narration = 'FTC_Arcade_Machine' #This is the label the transaction will get in customers wallets

RelayOn = 10 # Time in seconds relay is turned on per credit
########################################################################
########################################################################


#This if statement sets credit price based on fiat cost above as long as FixedFTC == 0 to nearest whole FTC
if creditCost == 0: 
	creditCost = int(round(PriceAPI.toFTC(WhichCurrency,FiatCost)))
	while creditCost == -1: #does not proceed if API offline
		os.system('sudo fbi -T 2 -d /dev/fb1 -noverbose -a CSN.png')
		time.sleep(15) #waits 15 seconds before retrying 
		creditCost = int(round(PriceAPI.toFTC(WhichCurrency,FiatCost)))
#Once credit price is set, it stays set until machine is restarted.

print "Credit cost in FTC", creditCost 

#Creating QR code PNG file based on account number, credit price and narration
create_qr.FTCQR(FTCAccountNo,creditCost,Narration)

balanceCheck = ftcapi.toFTC(FTCAccountNo) #gets balance of account

#if API is offline at start it will set balance to -1 triggering free games
#when API comes online so need a loop to not let it progress until API is online
while balanceCheck == -1:
	os.system('sudo fbi -T 2 -d /dev/fb1 -noverbose -a CSN.png')
	time.sleep(15) #waits 15 seconds before retrying
	balanceCheck = ftcapi.toFTC(FTCAccountNo)

previousBalance = balanceCheck #set previous balance to account balance
countingCredits = 0 #how many credits was bought with deposit
os.system('sudo fbi -T 2 -d /dev/fb1 -noverbose -a qr.png') #display QR
OnOffLine = 0 # when status is 1 the offline picture has been displayed
#this is to stop the pi call the OS to keep redisplaying same picture
#every 15 seconds

#main loop
while True:	
	#gets current account balance
	balanceCheck = ftcapi.toFTC(FTCAccountNo)
	
	print "Current Balance", balanceCheck
	print "Previous balance before checking credits", previousBalance
	
	#while is used to count if more than one credit is depositted at a time
	if balanceCheck == -1:
		if OnOffLine == 0:
			os.system('sudo fbi -T 2 -d /dev/fb1 -noverbose -a CSN.png')
			OnOffLine = 1
	else:
		if OnOffLine == 1:
			os.system('sudo fbi -T 2 -d /dev/fb1 -noverbose -a qr.png')
			OnOffLine = 0		
		while (balanceCheck -creditCost) >= previousBalance: #checks that deposit is higher than cost of  credit or ignores
			print "New Balance", balanceCheck
			countingCredits += 1
			previousBalance = previousBalance + creditCost
			print "Credits", countingCredits, "previous balance", previousBalance	 
	
	#this part 'spends the credits' which at the moment just lights up an LED for 10 seconds
	while countingCredits > 0:
		GPIO.output(16,True) ## Turn on GPIO pin 16
		time.sleep(RelayOn)
		GPIO.output(16,False) ## Turn off GPIO pin 16
		countingCredits -=1 #decrement credits by 1
		print "Credits Left", countingCredits
		time.sleep(2) #wait enough time for us to see LED go off for multiple credit payments 
	

	time.sleep(15) #waits 15 seconds before repeating
