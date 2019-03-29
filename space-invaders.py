alien = Actor('alien')
rocket = Actor('rocket')
laser = Actor('laser')

WIDTH = 500
HEIGHT = 350

alien.midbottom = WIDTH / 2, HEIGHT - 5
score = 0

def draw():
    screen.clear()
    screen.draw.text("score: " + str(score), (20, 20))
    alien.draw()

def on_key_down(key):
    if key == keys.LEFT:
        alien.left -= 5
    elif key == keys.RIGHT:
        alien.right += 5
    elif key == keys.SPACE:
        print("Space pressed")