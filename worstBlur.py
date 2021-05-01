import pygame
import time
from PIL import Image
pygame.init()
screen_size = 500
screen = pygame.display.set_mode([screen_size, screen_size])
running = True
imageName = "yes.jpg"
processSpeed = 0
blueRadius = 1
imgToBlur = Image.open(imageName)
image = pygame.image.load(imageName)
imgPixels = [[0 for i in range(imgToBlur.width)] for j in range(imgToBlur.height)]
outputImg = Image.new('RGB', (imgToBlur.width, imgToBlur.height))
for x in range(0,imgToBlur.width):
	for y in range(0,imgToBlur.height):
		imgPixels[x][y] = imgToBlur.getpixel((x,y))
x = 0
y = 0
class Pointer:
	pointer_x = 0
	pointer_y = 0
	def __init__(self,radius):
		self.radius = radius
	def draw(self,xPos,yPos):
		for xR in range(-self.radius,self.radius+1):
			for yR in range(-self.radius,self.radius+1):
				pygame.draw.rect(screen, (255,255,255), pygame.Rect(xR+xPos,yR+yPos,1,1))
		pygame.draw.rect(screen, (0,255,0), pygame.Rect(xPos,yPos,1,1))
def avgPixel(x,y,radius):
	resultColor = (0,0,0)
	totalR = 0
	totalG = 0
	totalB = 0
	nbPixel = pow(radius+1,2)
	for x2 in range(-radius,radius+1):
		for y2 in range(-radius,radius+1):
			try:
				totalR+=imgPixels[x+x2][y+y2][0]
				totalG+=imgPixels[x+x2][y+y2][1]
				totalB+=imgPixels[x+x2][y+y2][2]
			except:
				pass

	return (x,y,(round(totalR/nbPixel/2),round(totalG/nbPixel/2),round(totalB/nbPixel/2)))
p = Pointer(blueRadius)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    screen.blit(image, (0, 0))
    p.draw(x,y)
    result = avgPixel(x,y,blueRadius)
    pX = result[0]
    pY = result[1]
    color = result[2]
    try:
    	outputImg.putpixel((pX,pY),color)
    except:
    	pass
    if (x == imgToBlur.width):
    	x = 0
    	y+=1
    if(y== imgToBlur.height):
    	y = 0
    	outputImg.show()
    	outputImg.save("result.png")
    x+=1
    time.sleep(processSpeed)
    pygame.display.flip()
