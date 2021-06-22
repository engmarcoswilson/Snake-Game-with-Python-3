# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Importando as bibliotecas
import turtle
import random
import time

#Criando a tela
screen = turtle.Screen()
screen.title("SNAKE GAME")
screen.setup(width=700, height=700)
screen.tracer(0)
screen.bgcolor("#1d1d1d")

#Criando a borda
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color("red")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

#score 
score = 0
delay = 0.1

#snake
snake = turtle.Turtle()
snake.speed()
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'

#comida
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("square")
fruit.color("white")
fruit.penup()
fruit.goto(30,30)

old_fruit = []

#Pontuação
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("Score: ", align="center", font=("Courier", 24, "bold"))

#definir movimentos

def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"

def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"
        
def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"
        
        
def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
        
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x +20)
        
#Definição das teclas
screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

#Funcionamento
while True:
    screen.update()
    
    #colisão entre cobra e fruta
    if snake.distance(fruit) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        fruit.goto(x, y)
        scoring.clear()
        score += 1
        scoring.write("Score: {}".format(score), align="center", font=("Courier", 24, "bold"))
        delay -=0.001
        
        #criação de uma nova fruta
        new_fruit = turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape("square")
        new_fruit.color("red")
        new_fruit.penup()
        old_fruit.append(new_fruit)
        
    #adicionando tamanho à cobra
    for i in range (len(old_fruit)-1, 0, -1):
        a = old_fruit[i-1].xcor()
        b = old_fruit[i-1].ycor()
        
        old_fruit[i].goto(a,b)
        
    if len(old_fruit) > 0:
        a = snake.xcor()
        b = snake.ycor()
        old_fruit[0].goto(a,b)
    snake_move()
    
    #Colisão entre a cobra e a borda
    if snake.xcor()>280 or snake.xcor()<-300 or snake.ycor()>240 or snake.ycor()<-240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor("turquoise")
        scoring.goto(0,0)
        scoring.write("   Game Over \n Your Score is {}".format(score), align="center", font=("Courier", 30, "bold"))
        
    #Colisões entre a cobra
    for food in old_fruit:
        if food.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("turquoise")
            scoring.goto(0,0)
            scoring.write("   Game Over \n Your Score is {}".format(score), align="center", font=("Courier", 30, "bold"))
            
    time.sleep(delay)

turtle.Terminator()