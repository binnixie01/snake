# imports

import time
import random
import turtle
import winsound
import mysql.connector as sqltor
from tkinter import *
from tkinter import ttk
from datetime import datetime
   
    
    
#MYSQL CONNECTIVITY
mycon= sqltor.connect(host='localhost',
                      user='root',
                      passwd='tiger',
                      database='score_record',
                      charset='utf8')
q=mycon.cursor()
q.execute("CREATE TABLE IF NOT EXISTS low(USERNAME varchar(20) not null,AGE INTEGER(10) not null,DATE_TIME DATETIME,SCORE integer(5) default 0)")
q.execute("select max(score) from low")
data1=q.fetchall()

for score in data1:
    global high_point
    high_point=score
    
#SCORE RECORD
def score_record():
    
    winsound.PlaySound("bin.wav", winsound.SND_ASYNC)
    global iot
    iot = Tk()
    iot.geometry("850x400")
    iot.title("score record")
    frame = Frame(iot)
    frame.pack()
    tree = ttk.Treeview(frame, columns = (1,2,3,4), height = 5, show = "headings")
    tree.pack(side = 'left')   

    tree.heading(1, text="USERNAME")
    tree.heading(2, text="AGE")
    tree.heading(3, text="DATE_TIME")
    tree.heading(4, text="SCORE")   

    tree.column(1, width = 200)
    tree.column(2, width = 200)
    tree.column(3, width = 200)
    tree.column(4, width = 200)

    iot.configure( background="skyblue3", relief="flat")  
    scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    scroll.pack(side = 'right', fill = 'y')
    tree.configure(yscrollcommand=scroll.set)

    
    q.execute("select * from low")
    data9=q.fetchall()
    for row in data9:
        gh=row
        datal = [ [gh] ]
        for val in datal:
            tree.insert('', 'end', values = (val[0]) )

    iot.mainloop()

# current score display
def score_display():
    global itt
   
    itt = Tk()
    itt.geometry("850x200")
    itt.title("score")
    frame1 = Frame(itt)
    frame1.pack()
    
    tree1 = ttk.Treeview(frame1, columns = (1,2,3,4), height = 5, show = "headings")
    tree1.pack(side = 'left')
    
    tree1.heading(1, text="USERNAME")
    tree1.heading(2, text="AGE")
    tree1.heading(3, text="DATE_TIME")
    tree1.heading(4, text="SCORE")
    
    tree1.column(1, width = 200)
    tree1.column(2, width = 200)
    tree1.column(3, width = 200)
    tree1.column(4, width = 200)
    itt.configure( background="skyblue3", relief="flat")

    q.execute("select * from low")
    datak=q.fetchall()
    for row in datak:
        gg=row
    datah = [ [gg] ]

    

    for val in datah:
        tree1.insert('', 'end', values = (val[0]) )

    itt.mainloop()
    
# game
def play():
       
    delay = 0.1

    # Score
    point = 0
    
    global wn
    # Set up the screen
    wn = turtle.Screen()
    wn.title("Snake Game by @binnixie01")
    wn.setup(width=1366, height=750)
    wn.bgcolor("green")
    wn.tracer(0) # Turns off the screen updates
    
    # Snake head
    head = turtle.Turtle()
    head.speed(0)
    head.shape("square")
    head.color("black")
    head.penup()
    head.goto(0,0)
    head.direction = "stop"

    # Snake food
    food = turtle.Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("red")
    food.penup()
    food.goto(0,100)

    segments = []

    # Pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("black")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "bold"))

    bls1=turtle.Turtle()
    bls1.pencolor("black")
    bls1.pensize(5)
    bls1.setheading(0)

    bls1.up()
    bls1.goto(313,380)
    bls1.down()
    bls1.begin_fill()
    # draw top
    bls1.forward(370)
    # draw right
    bls1.right(90)
    bls1.forward(740)
    # draw bottom
    bls1.right(90)
    bls1.forward(370)
    # draw left
    bls1.right(90)
    bls1.forward(740)
   
    bls1.end_fill()

    bls=turtle.Turtle()
    bls.pencolor("black")
    bls.pensize(5)
    bls.setheading(0)

    bls.up()
    bls.goto(-683,380)
    bls.down()
    bls.begin_fill()
    # draw top
    bls.forward(370)
    # draw right
    bls.right(90)
    bls.forward(740)
    # draw bottom
    bls.right(90)
    bls.forward(370)
    # draw left
    bls.right(90)
    bls.forward(740)
   
    bls.end_fill()

    blu1=turtle.Turtle()
    blu1.pencolor("black")
    blu1.pensize(5)
    blu1.setheading(0)

    blu1.up()
    blu1.goto(-310,410)
    blu1.down()
    blu1.begin_fill()
    # draw top
    blu1.forward(620)
    # draw right
    blu1.right(90)
    blu1.forward(100)
    # draw bottom
    blu1.right(90)
    blu1.forward(620)
    # draw left
    blu1.right(90)
    blu1.forward(100)
   
    blu1.end_fill()

    blu2=turtle.Turtle()
    blu2.pencolor("black")
    blu2.pensize(5)
    blu2.setheading(0)

    blu2.up()
    blu2.goto(-310,-313)
    blu2.down()
    blu2.begin_fill()
    # draw top
    blu2.forward(620)
    # draw right
    blu2.right(90)
    blu2.forward(100)
    # draw bottom
    blu2.right(90)
    blu2.forward(620)
    # draw left
    blu2.right(90)
    blu2.forward(100)
   
    blu2.end_fill()
    
    # Functions
    def go_up():
        if head.direction != "down":
            head.direction = "up"

    def go_down():
        if head.direction != "up":
            head.direction = "down"

    def go_left():
        if head.direction != "right":
            head.direction = "left"

    def go_right():
        if head.direction != "left":
            head.direction = "right"

    def move():
        if head.direction == "up":
            y = head.ycor()
            head.sety(y + 20)

        if head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)

        if head.direction == "left":
            x = head.xcor()
            head.setx(x - 20)

        if head.direction == "right":
            x = head.xcor()
            head.setx(x + 20)
    
    # Keyboard bindings
    wn.listen()
    wn.onkeypress(go_up, "w")
    wn.onkeypress(go_down, "s")
    wn.onkeypress(go_left, "a")
    wn.onkeypress(go_right, "d")

    # Main game loop
    while True:
        wn.update()
        
        # Check for a collision with the border
        if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            winsound.PlaySound("F:\ip pro\scream.wav", winsound.SND_ASYNC)
            
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
            
            # Clear the segments list
            segments.clear()
            name=usernam.get()
            age=pas.get()
            
            print('USERNAME => ',name,'\nAGE => ',age,'\nDATE AND TIME => ',dtr,'\nSCORE=> ',point)   
            q.execute("INSERT INTO low(USERNAME,AGE,DATE_TIME,SCORE) VALUES('{}','{}','{}',{})".format(name,age,dtr,point))
            mycon.commit()
            
            
            
            # Reset the delay
            delay = 0.1
            
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(point, high_point), align="center", font=("Courier", 24, "bold")) 
            turtle.bye()   
            score_display()
            
            break
                  
                       
        # Check for a collision with the food
        if head.distance(food) < 20:
            # Move the food to a random spot
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x,y)
            
            # Add a segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("grey")
            new_segment.penup()
            segments.append(new_segment)
            winsound.PlaySound("F:\ip pro\plant.wav", winsound.SND_ASYNC)
            # Shorten the delay
            delay -= 0.001

            # Increase the score
            point += 10
             
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(point, high_point), align="center", font=("Courier", 24, "bold")) 

        # Move the end segments first in reverse order
        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)

        # Move segment 0 to where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x,y)

        move()    

        # Check for head collision with the body segments
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0,0)
                head.direction = "stop"
                winsound.PlaySound("F:\ip pro\scream.wav", winsound.SND_ASYNC)
                # Hide the segments
                for segment in segments:
                    segment.goto(1000, 1000)
            
                # Clear the segments list
                segments.clear()
                name=usernam.get()
                age=pas.get()

                print('USERNAME => ',name,'AGE => ',age,'\nDATE AND TIME => ',dtr,'\nSCORE=> ',point)   
                q.execute("INSERT INTO low(USERNAME,AGE,DATE_TIME,SCORE) VALUES('{}','{}','{}',{})".format(name,age,dtr,point))
                mycon.commit()
                
                
                # Reset the delay
                delay = 0.1
                
                # Update the score display
                pen.clear()
                pen.write("Score: {}  High Score: {}".format(point, high_point), align="center", font=("Courier", 24, "bold"))
                turtle.bye()
                score_display()
                
                break
   
                
    

        time.sleep(delay)
    
# game exit
def close():
    l=quit()

# menu
def menu():
    root.destroy()
    global menu2
    menu2=Tk()
    D = Canvas(menu2, height=768, width=1366) 
    no = PhotoImage(file ="im.png")
    background_label1 = Label(menu2, image=no)
    background_label1.place(x=0, y=0, relwidth=1, relheight=1) 
    D.pack()
    
    menu2.title("menu")


    title1 = Label(menu2,text="MENU",font=('Tempus Sans ITC',50),bg="PALE GREEN")
    title1.place(x=550,y=40)


    b3=Button(menu2,text='PLAY GAME',width=15, bg ='lightblue3',font=("Tempus Sans ITC",40),command=play)
    b3.place(x=470,y=250)
    
   
    b5=Button(menu2,text='SCORE RECORDS',width=15, bg ='lightblue3',font= ("Tempus Sans ITC",40),command=score_record)
    b5.place(x=470,y=350)
    b6=Button(menu2,text='QUIT GAME',width=15, bg ='lightblue3',font= ("Tempus Sans ITC",40),command=close)
    b6.place(x=470,y=450)
    
    menu2.mainloop()


def jk():
    winsound.PlaySound("bin.wav", winsound.SND_ASYNC)
     #LOGIN
            
    global root
    root=Tk()
    C = Canvas(root, height=768, width=1366) 
    filenames = PhotoImage(file ="im.png")
    background_label = Label(root,image=filenames)
    background_label.place(x=0, y=0, relwidth=1, relheight=1) 
    C.pack()

    #TIME
    now = datetime.now()
    # dd/mm/YY H:M:S
    global dtr
    dtr = now.strftime("%Y/%m/%d %H:%M:%S")

    root.title("login")
    global usernam
    usernam= StringVar()
    global pas
    pas= IntVar()

    # login page
    title = Label(text="SNAKE!!!!",font=('jokerman',72),bg="PALE GREEN")
    title.place(x=470,y=50)
    l1=Label(text="ENTER USERNAME :",font=("Tempus Sans ITC", 40),bg="lightblue3")
    l1.place(x=150,y=250)
    l2=Label(text="ENTER AGE :",font=("Tempus Sans ITC", 40),bg="lightblue3")
    l2.place(x=150,y=350)

    #entry field
    e1= Entry(root,textvar=usernam,width=20,font=("OCR A Extended", 30))
    e1.place(x=640,y=260)
    e2= Entry(root,textvar=pas,width=20,font=("OCR A Extended", 30))
    e2.place(x=640,y=360)
    
    #button
    b1=Button(text='CLICK ME',font=("Tempus Sans ITC",30), bg ='light blue',command = menu)
    b1.place(x=600,y=580)
    
    root.mainloop()

jk()





