from turtle import Turtle, Screen
import time

my_turt_obj = Turtle()

my_turt_obj.color("red", "green")
my_turt_obj.shape("turtle")

# for i in range(20):
#     my_turt_obj.forward(2)
#     time.sleep(0.3)

for i in range(4):
    my_turt_obj.forward(40)
    my_turt_obj.left(90)


screen = Screen()

screen.exitonclick()