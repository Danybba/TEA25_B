"""Kleines Turtle-Beispiel: buntes Spiral-Muster."""

import turtle

screen = turtle.Screen()
screen.title("Turtle Muster")
screen.bgcolor("black")

stift = turtle.Turtle()
stift.speed(0)
stift.width(2)

farben = ["cyan", "yellow", "lime", "orange", "magenta"]

for i in range(120):
    stift.pencolor(farben[i % len(farben)])
    stift.forward(i * 2)
    stift.left(59)

# Fenster offen halten
screen.mainloop()
