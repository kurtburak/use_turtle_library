import turtle
import random

#Sahneyi Oluşturduk
screen=turtle.Screen()
screen.screensize(400,400)
screen.bgcolor("lightblue")
screen.title("Catch The Turtle")

###Kamlumbağa nesnesini oluşturduk
turtle_instance=turtle.Turtle()
turtle_instance.shape("turtle")
turtle_instance.color("green")
turtle_instance.penup()
turtle_instance.speed("fastest")
turtle_instance.hideturtle()
turtle_instance.goto(0,300)
turtle_instance.write("Catch The Turtle","","center",font=("Arial",20,"bold"))
turtle_instance.home()
turtle_instance.showturtle()

#şimdi score nesnesini oluşturucağız

score=0
score_display=turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0,250)
score_display.hideturtle()
score_display.write(f"Your Score: {score}", "", "center",font=("Arial",20,"bold"))



#zamanlayacı ekliyoruz

time_left=30
time_display=turtle.Turtle()
time_display.penup()
time_display.hideturtle()
time_display.goto(0,200)
time_display.write(f"Yourt Left Time: {time_left}","","center",font=("Arial",15,"bold"))


#şimdi kamplumbağanın rastgele konuma gitmesi için bir fonksiyon kullanacağız

def move_tos():
    x=random.randint(-200,200)
    y=random.randint(-200,200)
    turtle_instance.goto(x,y)
    screen.ontimer(move_tos,1000)
def on_click(x,y):
    global score
    score=score+1
    score_display.clear()
    score_display.write(f"Your Score: {score}", "", "center",font=("Arial",20,"bold"))
def timeleft():
    global time_left
    time_display.clear()
    if time_left > 0 :
        time_display.write(f"Left Time: {time_left}", "", "center", font=("Arial",15,"bold"))
        time_left =time_left-1
        screen.ontimer(timeleft,1000)
    else:
        time_display.write("Game OVER","","center",font=("Arial",15,"bold"))
        turtle_instance.hideturtle()
        turtle_instance.onclick(None)

timeleft()
turtle_instance.onclick(on_click)
move_tos()


turtle.done()




