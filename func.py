import random, threading, time

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BALL_SIZE = 25

balls = list()

class Ball:
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed_x = 0
        self.speed_y = 0
        self.color = 0
 
def make_ball():
    ball = Ball()
    ball.x = random.randrange(BALL_SIZE, WINDOW_WIDTH - BALL_SIZE)
    ball.y = random.randrange(BALL_SIZE, WINDOW_HEIGHT - BALL_SIZE)
    ball.speed_x = random.choice([-5, -1, 1, 5])
    ball.speed_y = random.choice([-5, -1, 1, 5])
    ball.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    balls.append(ball)

def make_ten_balls():
    for _ in range(10):
        make_ball()
        time.sleep(0.05)

class threads_balls(threading.Thread):
    
    def run(self):
        self.kill = False

        ball = balls[(len(balls) - 1)]
        while not self.kill:
            time.sleep(0.01)
            ball.x += ball.speed_x
            ball.y += ball.speed_y
            ### Collisions ###
            if (ball.y > WINDOW_HEIGHT - BALL_SIZE) or (ball.y < BALL_SIZE):
                ball.speed_y *= -1
            if (ball.x > WINDOW_WIDTH - BALL_SIZE) or (ball.x < BALL_SIZE):
                ball.speed_x *= -1