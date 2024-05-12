#Anoushka Saha
#Introducing Turtle
#May 12th, 2024
#Day 16 Practice

#Importing the Turtle object and screen from the turtle class
from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)

#Creating screen object
my_screen = Screen()

#Changing shape using shape() method
timmy.shape("turtle")

#Changing colour using color() method
timmy.color("coral")

#Moving turtle forward 100 paces using forward() method
timmy.forward(100)

#Printing screen height, which is an attribute associated with the screen object
print(my_screen.canvheight)

#A function tied to an object is called a method
#Using exitonclick() method 
my_screen.exitonclick()