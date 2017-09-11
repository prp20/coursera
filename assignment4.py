# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left

def spawn_ball(direction):
    
    global ball_pos, ball_vel # these are vectors stored as lists
    int_vel = [0,0]
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    int_vel[0] = random.randrange(2, 4)
    int_vel[1] = random.randrange(1, 3)
    
    if direction == "RIGHT":
        ball_vel = [int_vel[0],-int_vel[1]]
    elif direction == "LEFT":
        ball_vel = [-int_vel[0],-int_vel[1]]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global score1, score2
    paddle1_pos = [WIDTH - HALF_PAD_WIDTH, HEIGHT/2 - HALF_PAD_HEIGHT]
    paddle2_pos = [HALF_PAD_WIDTH,HEIGHT/2 - HALF_PAD_HEIGHT]
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    spawn_ball("RIGHT")
     
        
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global ball_pos, ball_vel, RIGHT, LEFT
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]     
    
    if ball_pos[1]  <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
        
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
        
    if (paddle1_pos[1] + paddle1_vel < HEIGHT - PAD_HEIGHT) and (paddle1_pos[1] + paddle1_vel > 0):
        paddle1_pos[1] += paddle1_vel
    
    if (paddle2_pos[1] + paddle2_vel < HEIGHT- PAD_HEIGHT) and (paddle2_pos[1] + paddle2_vel > 0):
        paddle2_pos[1] += paddle2_vel
        
    # draw paddles
    canvas.draw_line(paddle1_pos,[paddle1_pos[0],paddle1_pos[1]+PAD_HEIGHT],PAD_WIDTH,"White")
    canvas.draw_line(paddle2_pos,[paddle2_pos[0],paddle2_pos[1]+PAD_HEIGHT],PAD_WIDTH,"White")   
    
    # determine whether paddle and ball collide   

#Left
    if ball_pos[0] <= BALL_RADIUS+PAD_WIDTH:
        if (ball_pos[1] >= paddle2_pos[1] and ball_pos[1] <= paddle2_pos[1]+PAD_HEIGHT):
            #print "paddle collision"
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] = 1.1 * ball_vel[0]
            ball_vel[1] = 1.1 * ball_vel[1]
        else:
            #print "gutter collision"
            score1 += 1
            spawn_ball("RIGHT")
#Right                
    elif ball_pos[0] >= WIDTH - (BALL_RADIUS+PAD_WIDTH):
        if (ball_pos[1] >= paddle1_pos[1] and ball_pos[1] <= paddle1_pos[1]+PAD_HEIGHT):
            #print "paddle collision"
            ball_vel[0] = -ball_vel[0] 
            ball_vel[0] = 1.1 * ball_vel[0]
            ball_vel[1] = 1.1 * ball_vel[1]
        else:
            #print "gutter collision"
            score2 += 1
            spawn_ball("LEFT")
            
    # draw scores
    #Left
    canvas.draw_text("Left Player",[100,20],20, "Yellow")
    canvas.draw_text(str(score2),[142,42],25, "Yellow")
    #Right
    canvas.draw_text("Right Player",[400,20],20, "Yellow")
    canvas.draw_text(str(score1),[450,42],25, "Yellow")
    
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 2
    
    if key == simplegui.KEY_MAP["up"]:
        paddle1_vel -= acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle1_vel += acc
       
    #print "Right pad vel = ", paddle1_vel
    #print ball_vel
#    print "Right paddle pos = ",paddle1_pos
#    print "Left paddle pos = ",paddle2_pos
    
    if key == simplegui.KEY_MAP["w"]:
        paddle2_vel -= acc
    elif key == simplegui.KEY_MAP["s"]:
        paddle2_vel += acc
    
def keyup(key):
    acc = 2
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle1_vel += acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle1_vel -= acc
       
    #print "Right pad vel = ", paddle1_vel
    
    #print "Right paddle pos = ",paddle1_pos
    #print "Left paddle pos = ",paddle2_pos
    
    if key == simplegui.KEY_MAP["w"]:
        paddle2_vel += acc
    elif key == simplegui.KEY_MAP["s"]:
        paddle2_vel -= acc
    

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.add_button("Reset", new_game, 100)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()














Student 22222222222222222
# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]
paddle1_pos = [HALF_PAD_WIDTH, HEIGHT / 2]
paddle2_pos = [WIDTH - HALF_PAD_WIDTH, HEIGHT / 2]
paddle1_vel = [0, 0]
paddle2_vel = [0, 0]
score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == LEFT:
        ball_vel[0] = -random.randrange(2, 4)
        ball_vel[1] = -random.randrange(1, 3)
    if direction == RIGHT:
        ball_vel[0] = random.randrange(2, 4)
        ball_vel[1] = -random.randrange(1, 3)


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos = [HALF_PAD_WIDTH, HEIGHT / 2]
    paddle2_pos = [WIDTH - HALF_PAD_WIDTH, HEIGHT / 2]
    paddle1_vel = [0, 0]
    paddle2_vel = [0, 0]
    score1 = 0
    score2 = 0
    spawn_ball(RIGHT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[1] += paddle1_vel[1]
    if paddle1_pos[1] <= HALF_PAD_HEIGHT:
        paddle1_pos[1] = HALF_PAD_HEIGHT
    elif paddle1_pos[1] >= HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos[1] = HEIGHT - HALF_PAD_HEIGHT
    paddle2_pos[1] += paddle2_vel[1]
    if paddle2_pos[1] <= HALF_PAD_HEIGHT: 
        paddle2_pos[1] = HALF_PAD_HEIGHT
    elif paddle2_pos[1] >= HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos[1] = HEIGHT - HALF_PAD_HEIGHT
        
    # draw paddles
    canvas.draw_polygon([[paddle1_pos[0] - HALF_PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT], [paddle1_pos[0] + HALF_PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT], [paddle1_pos[0] + HALF_PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT], [paddle1_pos[0] - HALF_PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT]], 2, "White", "White")
    canvas.draw_polygon([[paddle2_pos[0] - HALF_PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT], [paddle2_pos[0] + HALF_PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT], [paddle2_pos[0] + HALF_PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT], [paddle2_pos[0] - HALF_PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT]], 2, "White", "White")
    
    # determine whether paddle and ball collide    
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH : 
        if ball_pos[1] >= paddle1_pos[1] - HALF_PAD_HEIGHT and ball_pos[1] <= paddle1_pos[1] + HALF_PAD_HEIGHT:
            ball_vel[0] = - ball_vel[0]
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
        else :
            spawn_ball(RIGHT)
            score2 +=1
    elif ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH:
        if ball_pos[1] >= paddle2_pos[1] - HALF_PAD_HEIGHT and ball_pos[1] <= paddle2_pos[1] + HALF_PAD_HEIGHT:
            ball_vel[0] = - ball_vel[0]
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
        else :
            spawn_ball(LEFT)
            score1 +=1
            
    # draw scores
    canvas.draw_text(str(score1), (120, 100), 44, "White")
    canvas.draw_text(str(score2), (440, 100), 44, "White")
    
        
def keydown(key):
    global paddle1_vel, paddle2_vel    
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = 4
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel[1] = -4
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel[1] = 4
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel[1] = -4
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["down"] or key == simplegui.KEY_MAP["up"]:
        paddle2_vel = [0, 0]
    elif key == simplegui.KEY_MAP["s"] or key == simplegui.KEY_MAP["w"]:
        paddle1_vel = [0, 0] 

def restart_handler():
    new_game()
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
restart = frame.add_button("Restart", restart_handler, 100)


# start frame
new_game()
frame.start()

student 333333333333333333
# Implementation of classic arcade game Pong

import simplegui
import random
import math

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [0.0, 0.0]
ball_vel = [0.0, 0.0]
direction = RIGHT

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel[0] = random.randrange(120, 240) / 60
    ball_vel[1] = random.randrange(60, 180) / 60
    if direction == LEFT: ball_vel[0] = -ball_vel[0]


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    ball_pos[0] = WIDTH / 2
    ball_pos[1] = HEIGHT / 2
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    paddle1_vel = 0.0
    paddle2_vel = 0.0
    spawn_ball(RIGHT)
    score1 = 0
    score2 = 0

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global paddle1_vel, paddle2_vel
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

    
    # update paddle's vertical position, keep paddle on the screen
    # update paddle1 if within screen
    #if (paddle1_pos > HALF_PAD_HEIGHT + BALL_RADIUS / 2) and  (paddle1_pos < (HEIGHT - HALF_PAD_HEIGHT - BALL_RADIUS / 2)):
    if (paddle1_pos > HALF_PAD_HEIGHT) and  (paddle1_pos < (HEIGHT - HALF_PAD_HEIGHT)):
        paddle1_pos += paddle1_vel
    else:
        # reflect paddle1 from the border
        if paddle1_pos <= HALF_PAD_HEIGHT:
            paddle1_vel = 1
            paddle1_pos += paddle1_vel
        if paddle1_pos >= HEIGHT - HALF_PAD_HEIGHT:
            paddle1_vel = -1
            paddle1_pos += paddle1_vel
    # update paddle2 if within screen
    if (paddle2_pos > HALF_PAD_HEIGHT) and  (paddle2_pos < (HEIGHT - HALF_PAD_HEIGHT)):
        paddle2_pos += paddle2_vel
    else:
        # reflect paddle2 from the border
        if paddle2_pos <= HALF_PAD_HEIGHT:
            paddle2_vel = 1
            paddle2_pos += paddle2_vel
        if paddle2_pos >= HEIGHT - HALF_PAD_HEIGHT:
            paddle2_vel = -1
            paddle2_pos += paddle2_vel

    # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], [HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], [WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    
    # determine whether paddle and ball collide
    
    # collide and reflect off of bottom of canvas
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
    # collide and reflect off of top of canvas
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]

    # collide and reflect off of left hand side of canvas
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        # paddle1_offset
        paddle1_offset = math.fabs(ball_pos[1] - paddle1_pos)
        if paddle1_offset < HALF_PAD_HEIGHT:
            # paddle collision
            ball_vel[0] = - ball_vel[0]
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
        else:
            # gutter collision
            spawn_ball(RIGHT)
            score2 += 1

    # collide and reflect off of right hand side of canvas
    if ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
        # paddle2_offset
        paddle2_offset = math.fabs(ball_pos[1] - paddle2_pos)
        if paddle2_offset < HALF_PAD_HEIGHT:
            # paddle collision
            ball_vel[0] = - ball_vel[0]
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
        else:
            # gutter collision
            spawn_ball(LEFT)
            score1 += 1
    
    # draw scores
    canvas.draw_text(str(score1), (WIDTH / 4, HEIGHT / 2), 36, 'Green')
    canvas.draw_text(str(score2), (3 * WIDTH / 4, HEIGHT / 2), 36, 'Green')
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel -= 3
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel += 3
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= 3
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel += 3


def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
