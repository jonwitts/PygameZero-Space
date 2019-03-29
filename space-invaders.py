import random

# define our sprites
alien = Actor('alien')
rocket = Actor('rocket')
laser = Actor('laser')

# set our stage
WIDTH = 800
HEIGHT = 500

# position our sprites 
rocket.midbottom = WIDTH / 2, HEIGHT - 5
alien.midbottom = (random.randint(40, WIDTH - 40), 80)

# set score and statuses 
score = 0
game_status = 0 # 0 = stop, 1 = playing
laser_status = 0  # 0 for not fired, 1 for fired

def draw():
    if game_status == 0:
        screen.draw.text("Press F1", (100, 300), color="white", fontsize=32)
    if game_status == 1:
        screen.clear()
        screen.draw.text("score: " + str(score), (20, 20))
        rocket.draw()
        move_alien()  # move our alien down each draw loop
        alien.draw()
        if laser_status > 0:
            move_laser()
            laser.draw()
        detect_hits()

def update():
    checkKeys()

def checkKeys():
    global rocket, laser, game_status, laser_status
    if game_status == 0:
        if keyboard.f1:
            game_status = 1
    elif game_status == 1:
        if keyboard.left:
            if rocket.x > 40:
                rocket.x -= 5
        if keyboard.right:
            if rocket.right < 760:
                rocket.x += 5
        if laser_status == 0:
            if keyboard.space:
                laser.pos = (rocket.x, HEIGHT - 98)
                laser_status = 1

def move_alien():
    alien.pos = (alien.x, alien.y+1)
    
def move_laser():
    global laser_status
    if laser_status > 0:
        laser.pos = (laser.x, laser.y - 2)
        if laser.y < 10:
            laser_status = 0

def detect_hits():
    global game_status, score, laser_status
    if alien.y >= HEIGHT - 40:
        screen.draw.text("Game Over", (100, 300), color="red", fontsize=32)
        game_status = 1
    if laser_status == 1 and alien.collidepoint(laser.pos):
        hit_alien()
        laser_status = 0
        score += 1

def hit_alien():
    alien.midbottom = (random.randint(40, WIDTH - 40), 80)