from PIL import ImageFont,ImageFilter,Image,ImageDraw
import random
#####################################################################################
def rndColor():
#This function is to create a RGB by random,as background color
    return(random.randint(64,255),random.randint(64,255),random.randint(64,255))
    #A RGB contains three numbers, we use random.randint to get these numbers

def rndChar():
#This function is to create a letter by random
    return chr(random.randint(65,95))

def rndColor2():
#This function is to create a RGB by random，as letter color
    return(random.randint(32，217),random.randint(32，217),random.randint(32，217))
    
    
W = 60*4
h = 60
#Define the width and height of the image
im = Image.new('RGB',(W,H),(0,0,0))
#Create a new image,using the RGB methed,width and height are defined in W AND H, the backgroundcolor is (0,0,0)
draw = ImageDraw.Draw(im)
#Define a pen, the pen is used on the image we just created, which is im.
font = ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf',36)
#Define a font which will be uesd later.
#Here, the 'r' before the path means the '\' will not be used as escape character
for i in range(60*4):
    for j in range(60):
        draw.point((i,j),fill=rndColor())
        #Go through each pixel of the image im, and set the Color coordinates random
for i in range(4):
    draw.text((10+60*i,10),rndChar(),font=font,fill=rndColor2())
    #Seprate the image into four parts, go throug each parts and put a random letter in it, 
    #set the Color coordinates of the letter random
    #Set the font of the letter as defined in variable font
image.save('1.jpg')
#Save the image as '1.jpg'

