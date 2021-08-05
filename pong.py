from ursina import *
from random import *

def update():
		global dx, dy
		global score,sin ,r,g,b
		if held_keys['a']:
			player.x-=9*time.dt
		if held_keys['d']:
			player.x+=9*time.dt
		if held_keys['r']:
			ball.x=0
			ball.y=0
			score[0]=0
		ball.x=ball.x+1*dx
		ball.y=ball.y+1*dy
		hitinfo=ball.intersects()
		if hitinfo.entity==player2 or hitinfo.entity==player:
			dx=uniform(-1,1)/10
			dx=dx*-1
			dy=dy*-1
			Audio('audio/sfx_menu_move1.wav')
			ball.color = color.rgb(randint(0,255),randint(0,255),randint(0,255))


			#print(dx)
		#print(ball.position)
		if abs(ball.x)>6.9:
			dx=dx*-1
			Audio('audio/sfx_menu_move4.wav')
		if abs(ball.y)>4:
			dy=dy*-1
			Audio('audio/sfx_menu_move4.wav')
		if ball.x>player2.x:
				player2.x+=4*time.dt
		if ball.x<player2.x:
				player2.x-=4*time.dt
		if ball.y>4:
			score[0]=score[0]+1
		if ball.y<-4:
			score[0]=score[0]-1
		if player.x>6.9:
			player.x-=9*time.dt
		if player.x<-6.9:
			player.x+=9*time.dt


		scoretext.text=("Score : " + str(score))
		window.color = color.rgb(r,g,b)
		r=r+0.05 *sin
		g=g+0.28 *sin
		b=b+0.2 *sin
		if r+g+b>764 or r+g+b<150:
			sin = sin*-1
		player.color= color.rgb(r/5,g/5,b*5)
		player2.color= color.rgb(r*3,g*3,b*3)
		#print(r,g,b)
app=Ursina()
dx=0.1
dy=0.1
sin = 1
r=50
g=50
b=50
scoretext = Text(x=0.7,y=-0.44)
score=[0]
player = Entity(model= 'quad',collider = 'box', y=-4.1, scale=(1.5,0.5,0))
player2 = Entity(model= 'quad',collider = 'box',  y=4.1, scale=(1.5,0.5,0))
ball = Entity(model='circle', collider = 'box',scale=0.4)


app.run()
