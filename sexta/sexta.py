import tkinter
canvas = tkinter.Canvas()
canvas.pack()
import random
poc = 0
for i in range(0,500,30):
    canvas.create_line(0,i,500,i)
    canvas.create_line(i,0,i,500)
    print(i)

canvas.create_rectangle(0,0,30,30, fill = "red", tag = "s")
canvas.create_rectangle(0,0,30,30, fill = "blue", tag = "t")



x1 = 0
y1 = 0

x2 = 0
y2 = 0 

def cas():
    global x1
    global y1
    global x2
    global y2

    x1 = random.randrange(0,360,30)
    y1 = random.randrange(0,270,30)
    z = random.randrange(0,100,1)
    
    x2 = random.randrange(0,360,30)
    y2 = random.randrange(0,360,30)
    
    canvas.coords("s",x1,y1,x1+30,y1+30)
    canvas.coords("t", x2,y2,x2+30,y2+30)

    canvas.update()
    canvas.after(1000 - poc*50 - z*10,cas)
  

cas()

  
def klik(a):
    global x1
    global y1
    global poc
    global x2
    global y2
    
    x = a.x//30*30
    y = a.y//30*30
    if x == x2 and y == y2:
        exit()
    if x == x1 and y1 == y:
        poc += 1
    else:
        poc -= 1
    print("skore:", poc)
    canvas.create_oval(x,y,x+30,y+30)

 
canvas.bind("<Button-1>",klik)
