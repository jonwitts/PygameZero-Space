import random

# define our sprites
alien = Actor('alien')
alien2 = Actor('alien2')
rocket = Actor('rocket')
laser = Actor('laser')

# set our stage
WIDTH = 800
HEIGHT = 800

# position our sprites 
rocket.midbottom = WIDTH / 2, HEIGHT - 5
alien.midbottom = (random.randint(40, WIDTH - 40), 80)
alien2.midbottom = (random.randint(40, WIDTH - 40), 80)

# set score and statuses 
score = 0
game_status = 0  # 0 = stop, 1 = playing
laser_status = 0  # 0 for not fired, 1 for fired
alien_speed = 1.0
laser_speed = 1.0

def draw():
    if game_status == 0:
        screen.draw.text("Press F1", (100, 300), color="white", fontsize=32)
    if game_status == 1:
        screen.clear()
        screen.draw.text("Score: " + str(score), (20, 20))
        rocket.draw()
        move_alien(alien)  # move our alien down each draw loop
        alien.draw()
        if score > 10:
            move_alien(alien2)
            alien2.draw()
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

def move_alien(alien_name):
    global alien_speed
    alien_name.pos = (alien_name.x, alien_name.y+(1*alien_speed))
    
def move_laser():
    global laser_status, laser_speed
    if laser_status > 0:
        laser.pos = (laser.x, laser.y - (2*laser_speed))
        if laser.y < 10:
            laser_status = 0

def game_over(alien_name):
    global game_status
    if alien_name.y >= HEIGHT - 40:
        screen.draw.text("Game Over", (100, 300), color="red", fontsize=32)
        game_status = 1

def laser_hit(alien_name, aggression, powerup):
    ''' Each alien can speed up with aggression and give you a '''
    ''' quicker laser with power up '''
    global laser_status, score, alien_speed, laser_speed
    if laser_status == 1 and alien_name.collidepoint(laser.pos):
        hit_alien(alien_name)
        laser_status = 0
        score += 1
        alien_speed += aggression
        laser_speed += powerup

def detect_hits():
    global score, laser_status, alien_speed, laser_speed
    game_over(alien)
    game_over(alien2)
    laser_hit(alien, 0.125, 0.1)
    laser_hit(alien2, 0.1, 0.125)

def hit_alien(alien_name):
    alien_name.midbottom = (random.randint(40, WIDTH - 40), 80)