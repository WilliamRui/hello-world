from PIL import ImageFont,ImageFilter,Image,ImageDraw
import random
def rndColor():
    return(random.randint(64,255),random.randint(64,255),random.randint(64,255))
def rndChar():
    return chr(random.randint(65,95))
def rndColor2():
    return(random.randint(32，217),random.randint(32，217),random.randint(32，217))
    
    
W = 60*4
h = 60

im = Image.new('RGB',(W,H),(0,0,0))
draw = ImageDraw.Draw(im)
font = ImageFont.truetype('Arial.ttf',36)
for i in range(60*4):
    for j in range(60):
        draw.point((i,j),fill=rndColor())
for i in range(4):
    draw.text((10+60*i,10),rndChar(),rndColor2())
image.save('1.jpg')
