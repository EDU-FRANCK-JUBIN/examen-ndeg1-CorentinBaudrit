# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 11:07:57 2019

@author: Corentin
"""

import turtle 
import random




# Initialisation du jeu
ts = turtle.getscreen()
ts.clear()
ts.bgpic("champcourse2.gif")

ts.title("Bienvenue Ã  la course des tortues !")
ts.setup (width=1400, height=800, startx=0, starty=0)





# DÃ©clarez les 5 tortues et positionnez-les sur leurs hexagones respectifs
# A IMPLEMENTER

m = turtle.Turtle()
m.speed(0)
m.color('orange')
m.shape("turtle")
m.penup()
m.setpos(-650,320)


l = turtle.Turtle()
l.speed(0)
l.color('Blue')
l.shape("turtle")
l.penup()
l.setpos(-650,170)


r = turtle.Turtle()
r.speed(0)
r.color('red')
r.shape("turtle")
r.penup()
r.setpos(-650,0)

d = turtle.Turtle()
d.speed(0)
d.color('purple')
d.shape("turtle")
d.penup()
d.setpos(-650,-140)


s = turtle.Turtle()
s.speed(0)
s.color('grey')
s.shape("turtle")
s.penup()
s.setpos(-650,-300)




        


# Demander de saisir dans la console les prÃ©dictions des joeurus 1 et 2 dans le format 1,2,3
# A IMPLEMENTER


# A l'aide d'une boucle while, faire courir les tortues en tirant un nombre entre 0 et 5 qui reprÃ©sente le nombre de pixels du dÃ©placement vers la droite
# A IMPLEMENTER
classement =  []

while (len(classement) < 5):
    if("m" not in classement):
        m.forward(random.random() *5)
    if (m.xcor() > 650 and "m" not in classement):
        classement.append("m")
    if("l" not in classement):
        l.forward(random.random() *5)
    if (l.xcor() > 650 and "l" not in classement):
        classement.append("l")
    if("r" not in classement):
        r.forward(random.random() *5)
    if (r.xcor() > 650 and "r" not in classement):
        classement.append("r")
    if("d" not in classement):
        d.forward(random.random() *5)
    if (d.xcor() > 650 and "d" not in classement):
        classement.append("d")
    if("s" not in classement):
        s.forward(random.random() *5)
    if (s.xcor() > 650 and "s" not in classement):
        classement.append("s")
print(classement)





# Comparer les rÃ©sultats de la course avec les pronostics des joueurs 
# et afficher le rÃ©sultat de la course
# et le joueur gagnant avec la tortue arbitre et l'instruction turtle.Write Ã  la position 0,0
# A IMPLEMENTER



turtle_arbitre = turtle.Turtle()
turtle_arbitre.goto(0,0)
turtle_arbitre.color("Black")
turtle_arbitre.write("La tortue : "+classement[0]+" gagne", move=True, align="left", font=("Arial", 16, "normal"))



turtle.mainloop()