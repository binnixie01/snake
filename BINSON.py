# imports
from tkinter import *
import turtle
from datetime import datetime
import winsound
import mysql.connector as sqltor
import time
import random
from tkinter import ttk

   
    
    
#MYSQL CONNECTIVITY
mycon= sqltor.connect(host='localhost',user='root',passwd='tiger',database='score_record',charset='utf8')
q=mycon.cursor()
q.execute("CREATE TABLE IF NOT EXISTS low(USERNAME varchar(20) ,AGE INTEGER(10),DATE_TIME DATETIME,SCORE integer(5) default 0)")
q.execute("select max(score) from low")
data1=q.fetchall()

for score in data1:
    global high_point
    high_point=score
#SCORE RECORD
def io():
    
    winsound.PlaySound("bin.wav", winsound.SND_ASYNC)
    global iot
    iot = Tk()
    iot.geometry("1366x500")
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

# curent score
def bins():
    global itt
   
    itt = Tk()
    itt.geometry("850x200")
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
    board=turtle.Turtle()
    board.pencolor("black")
    board.pensize(5)
    board.setheading(0)

    board.up()
    board.goto(313,380)
    board.down()
    board.begin_fill()
    # draw top
    board.forward(370)
    # draw right
    board.right(90)
    board.forward(740)
    # draw bottom
    board.right(90)
    board.forward(370)
    # draw left
    board.right(90)
    board.forward(740)
   
    board.end_fill()

    beard=turtle.Turtle()
    beard.pencolor("black")
    beard.pensize(5)
    beard.setheading(0)

    beard.up()
    beard.goto(-683,380)
    beard.down()
    beard.begin_fill()
    # draw top
    beard.forward(370)
    # draw right
    beard.right(90)
    beard.forward(740)
    # draw bottom
    beard.right(90)
    beard.forward(370)
    # draw left
    beard.right(90)
    beard.forward(740)
   
    beard.end_fill()

    board1=turtle.Turtle()
    board1.pencolor("black")
    board1.pensize(5)
    board1.setheading(0)

    board1.up()
    board1.goto(-310,410)
    board1.down()
    board1.begin_fill()
    # draw top
    board1.forward(620)
    # draw right
    board1.right(90)
    board1.forward(100)
    # draw bottom
    board1.right(90)
    board1.forward(620)
    # draw left
    board1.right(90)
    board1.forward(100)
   
    board1.end_fill()

    board2=turtle.Turtle()
    board2.pencolor("black")
    board2.pensize(5)
    board2.setheading(0)

    board2.up()
    board2.goto(-310,-313)
    board2.down()
    board2.begin_fill()
    # draw top
    board2.forward(620)
    # draw right
    board2.right(90)
    board2.forward(100)
    # draw bottom
    board2.right(90)
    board2.forward(620)
    # draw left
    board2.right(90)
    board2.forward(100)
   
    board2.end_fill()
    
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
            q.execute("CREATE TABLE IF NOT EXISTS low(USERNAME varchar(20) ,AGE INTEGER(10),DATE_TIME DATETIME,SCORE integer(5) default 0)")
            q.execute("INSERT INTO low(USERNAME,AGE,DATE_TIME,SCORE) VALUES('{}','{}','{}',{})".format(name,age,dtr,point))
            mycon.commit()
            
            
            
            # Reset the delay
            delay = 0.1
            
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(point, high_point), align="center", font=("Courier", 24, "bold")) 
            turtle.bye()   
            bins()
            
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
                q.execute("CREATE TABLE IF NOT EXISTS low(USERNAME varchar(20) ,AGE INTEGER(10),DATE_TIME DATETIME,SCORE integer(5))")
                q.execute("INSERT INTO low(USERNAME,AGE,DATE_TIME,SCORE) VALUES('{}','{}','{}',{})".format(name,age,dtr,point))
                mycon.commit()
                
                
                # Reset the delay
                delay = 0.1
                
                # Update the score display
                pen.clear()
                pen.write("Score: {}  High Score: {}".format(point, high_point), align="center", font=("Courier", 24, "bold"))
                turtle.bye()
                bins()
                
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
    
   
    b5=Button(menu2,text='SCORE RECORDS',width=15, bg ='lightblue3',font= ("Tempus Sans ITC",40),command=io)
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


