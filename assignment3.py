#http://www.codeskulptor.org/#user40_o0p4nk6iiptqsJE.py
#http://www.codeskulptor.org/#user40_o0p4nk6iiptqsJE.py


# template for "Stopwatch: The Game"
# This is a simple game that acts like a stop watch and 
# The game is the if a player stops the stopwatch a exact
# stroke of a second then he earns a point else only his 
# number of chances increases but not his score


# So play the game and enjoy!!!!!!!!!!!!!!




import simplegui
# define global variables
num=0
txt="00:00.00"
text="0/0"
ch=0
pt=0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global txt
    a=t/600
    if((a<10) and(a>0)):
        a="0"+str(a)
    elif(a>10):
        a=a
    else:
        a="00"
    x=t%600
    b=x/10
    if((b<10) and(b>0)):
        b="0"+str(b)
    elif(b>10):
        b=b
    else:
        b="00"
    c=x%10
    if((c<10) and(c>0)):
        c="0"+str(c)
    else:
        c="00"
    txt= str(a)+":"+str(b)+"."+str(c)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
# The various event handlers are defined here 
# THis is the funtion that helps to 
def tick():
    global num
    num=num+1
    format(num)
    timer.start()
# The function that helps to begin the game
def start():
    tick()
# The function that helps to stop the game
def stop():
    global text, num, ch, pt
    timer.stop()
    ch=ch+1
    if(((num%10)==0)and(num!=0)):
        pt=pt+1
    else:
        pt=pt+0
    text=str(pt)+"/"+str(ch)
# The function that restarts the game
def restart():
    global num, txt, ch, pt, text
    num=0
    text="0/0"
    ch=0
    pt=0
    txt="00:00.00"
# Handler to draw on canvas
def draw(canvas):
    global txt, text
    canvas.draw_text(txt,(60, 120), 30, "red")
    canvas.draw_text(text,(20,50), 20, "white")
    canvas.draw_text("player score", (20,30), 20, "white")
# The creation of canvas
f=simplegui.create_frame("stopwatch!!!", 200, 200, 200)
# All the bottons and inputs are registered here
f.add_button("start", start, 200)
f.add_button("stop", stop, 200)
f.add_button("Restart", restart, 200)
f.set_draw_handler(draw)
timer=simplegui.create_timer(100, tick)

# Start the frame animation
f.start()




















import simplegui
width = 600
height = 400
bal_rad = 20
bal_pos = [width/2, height/2]
vel = [0, 0]

def draw(canvas):
    bal_pos[0] += vel[0]
    bal_pos[1] += vel[1]
    if bal_pos[0] <= bal_rad:
        vel[0] = -vel[0]
    elif bal_pos[0] >= width-bal_rad:
        vel[0] = -vel[0]
    elif bal_pos[1] <= bal_rad:
        vel[1] = -vel[1]
    elif bal_pos[1] >= height - bal_rad:
        vel[1] = -vel[1]
    
    canvas.draw_circle(bal_pos, bal_rad, 2, "red", "white")
def keydown(key):
    acc = 1
    if key==simplegui.KEY_MAP["left"]:
        vel[0] -= acc
    elif key==simplegui.KEY_MAP["right"]:
        vel[0] += acc
    elif key==simplegui.KEY_MAP["down"]:
        vel[1] += acc
    elif key==simplegui.KEY_MAP["up"]:
        vel[0] -= acc
    
f = simplegui.create_frame("motion", width, height)
f.set_draw_handler(draw)
f.set_keydown_handler(keydown)
f.start()

                 

