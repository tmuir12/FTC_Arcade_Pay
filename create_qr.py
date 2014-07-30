import qrcode
import PIL
from PIL import ImageTk, Image, ImageFont, ImageDraw

###This module creates the QR code based on the information set in main.oy

def FTCQR(FTCAccountNo, creditCost, Narration):
	qrdata = ("feathercoin:%s?amount=%s&label=%s") % (FTCAccountNo, creditCost, Narration)
	qr = qrcode.QRCode(version=10) 
	qr.add_data(qrdata) 
	qr.make() 
	im = qr.make_image() 
	basewidth = 220
	wpercent = (basewidth/float(im.size[0]))
	hsize = int((float(im.size[1])*float(wpercent)))
	im = im.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
	#code above creates QR code
	
	img = Image.new("RGB", (320, 240), "white")#creates white 320 x 240 image
	img.paste(im, (100, 10)) #pastes QR code into image
	logo = Image.open('FTC-logo.png') #open FTC logo
	img.paste(logo, (10, 25)) #adds FTC logo to image
	#next section adds text to image
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype("/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Bold.ttf", 20)
	draw.text((20, 130), str(creditCost)+" FTC", (0,0,0), font=font)
	draw.text((45, 155), "=", (0,0,0), font=font)
	draw.text((10, 180), "1 Credit", (0,0,0), font=font)
	img.save("qr.png")
	return
