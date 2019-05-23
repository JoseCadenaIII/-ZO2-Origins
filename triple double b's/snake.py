from gamelib import *

game = Game(800, 600, "snake.io", 30)
bk = Image("slither.jpg", game)
bk.resizeTo(game.width,game.height)
snake = Image("j1.png", game)
snake.moveTo(900,randint(50,300))
             
snake.setSpeed(3,90)
hero = Image("hero.png",game)
hero.moveTo(400,600)
pellet = Image("soul.png",game)
pellet.setSpeed(50,0)#set so that the pellets can move
pellet.resizeBy(-20)
pellet.visible = False
evil = Image("evil.png",game)
evil.resizeBy(-30)
evil.moveTo(-500,randint(50,300))
a = 270
evil.setSpeed(5,a)


while not game.over:
    game.processInput()
    bk.draw()
    pellet.move()#needed to move the pellets when the space bar is pressed
    snake.move()
    hero.draw()
    evil.move()
    
 
 
    
    if snake.isOffScreen("left"):
         snake.moveTo(900,randint(50,300))

        
    if evil.isOffScreen("right"):
        evil.moveTo(-500,randint(50,300))

    if evil.isOffScreen("bottom"):
        evil.moveTo(randint(50,400),randint(50,300))
        evil.resizeTo(800,800)

    if keys.Pressed[K_SPACE]:
        pellet.visible = True
        pellet.moveTo(hero.x,hero.y-130)
     

    if pellet.collidedWith(evil,"rectangle"):
        a+=20
        evil.resizeBy(-5)
        evil.setSpeed(3,a)       
        evil.moveTowards(hero,2)
     
     
           
        
    game.update(30)
        
game.quit()
