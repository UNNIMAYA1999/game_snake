import pygame
import random
pygame.init()
size=(500,500)
screen=pygame.display.set_mode(size)
BLUE=(0,0,255)
GREEN=(0,255,0)
RED=(255,0,0)
WHITE=(255,255,255)
screen.fill(WHITE)
pygame.display.set_caption("Snake Xenzia")
pygame.display.flip()
over=False
score=0
clock=pygame.time.Clock()
font=pygame.font.Font(None,25)
def scorecal(score):
	text=font.render("Score:"+ score,True,BLUE)
	screen.blit(text,[0,0])
i=1
j=1
rect_y=249
rect_x=249
x=0
y=0
snakelength=1
FPS=10
score=0
def snakedraw(snake):
	for XnY in snake:
		pygame.draw.rect(screen,BLUE,[XnY[0],XnY[1],10,10])
	
gx=random.randrange(0,489)
gy=random.randrange(0,489)
snake=[]
clock=pygame.time.Clock()
while not over:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			over=True
		if(event.type==pygame.KEYDOWN):	
			if(event.key==pygame.K_RIGHT):
				if(x==0):
					x=10
					y=0
			elif(event.key==pygame.K_LEFT):
				if(x==0):
					x=-10
					y=0
			elif(event.key==pygame.K_UP):
				if(y==0):
					y=-10
					x=0
			elif(event.key==pygame.K_DOWN):
				if(y==0):
					y=+10
					x=0
	screen.fill(WHITE)
	rect_x=rect_x+x
	rect_y=rect_y+y
	pygame.draw.rect(screen,RED,[gx,gy,10,10])
	snakehead=[]
	snakehead.append(rect_x)
	snakehead.append(rect_y)
	snake.append(snakehead)
	snakedraw(snake)
	if len(snake)>snakelength:
		del snake[0]

	if snakehead in snake[:-1]:
		over=True
	elif snakehead[0]>=489 or snakehead[0]<=0:
		over = True
	elif snakehead[1]>=489 or snakehead[1]<=0:
		over = True
	q1=str(score)
	scorecal(q1)
	pygame.display.flip()
	if(rect_x>=gx-5 and rect_x<=gx+10 and rect_y>=gy-5 and  rect_y<=gy+10):
		snakelength+=1
		score+=1
		FPS+=2
		gx=random.randrange(0,489)
		gy=random.randrange(0,489)
	clock.tick(FPS)
