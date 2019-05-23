from gamelib import*
#objects
game = Game(800,600,"LonzoBall Origins")
bk = Image("bk.jpg",game)
bk.resizeTo(game.width,game.height)
title = Image("zo1.jpg",game)
player1 = Image("player 1.png",game)
player1.moveTo(player1.x,450)
player1.resizeBy(-65)
player2 = Image("kobe.png",game,3)
player2.resizeBy(-80)
player2.moveTo(200,player2.y)
ball = Image("ball.png",game)
ball.resizeBy(-90)
ball.setSpeed(10,90)
ball.visible = False
hoop = Image("hoop.png",game)
hoop.resizeBy(-80)
hoop.moveTo(650,230)
secondhoop = Image("hoop 2.png",game)
secondhoop.resizeBy(-80)
secondhoop.moveTo(150,240)
player2.setSpeed(10,180)
player3 = Image("Lebron.png",game,3)
player3.setSpeed(10,180)
player3.resizeBy(-90)
player3.moveTo(600,player3.y)
game.displayScore()

while not game.over:
    game.processInput()
    bk.draw()
    player1.draw()
    player2.draw()
    player3.draw()
    hoop.draw()
    secondhoop.draw()
    ball.move(True)
    player3.move(True)
    player2.move(True)
    
    if keys.Pressed[K_LEFT]:
        player1.x -=10

    if keys.Pressed[K_RIGHT]:
        player1.x +=10
    
    if keys.Pressed[K_SPACE]:
        ball.visible = True
        ball.moveTo(player1.x,player1.y)
        
    if keys.Pressed[K_UP]:
        player1.y-=8
        
    if keys.Pressed[K_DOWN]:
        player1.y+=8

    if ball.collidedWith(hoop):
        game.score+=10
    game.update(30)
game.over = False

