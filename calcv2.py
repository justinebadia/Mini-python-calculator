from _ast import Lambda
from tkinter import *

# Créer la fenêtre principale
main_window = Tk()

# paramètres pour la fenêtre principale - couleur de fond, titre et taille
main_window.configure(background="#3e41de")
main_window.title("My Calculator")
main_window.geometry("195x310")

# Variable permettant de stocker le contenu de notre caclul
equation = StringVar()

# variable qui va permettre de garder en mémoire les touches cliquées
expression = ""

# fonction qui gère le clique de la souris
def click_button(touche):
	if touche == "=":
		calculer()
		return

	global expression
	expression += str(touche)
	equation.set(expression)
	return 

def calculer():
	try:
		global expression
		total = str(eval(expression))
		equation.set(total)
		expression = total
	except:
		equation.set("erreur")
		expression = ""

def effacer():
	global expression
	expression = ""
	equation.set("")
	return

# Boite de résultats : l'encadré où va s'afficher notre calcul
resultat = Label(main_window, bg="#3e41de", fg="#FFF", textvariable=equation, height="2")
resultat.grid(columnspan=3)

# Création des boutons avec les paramètres de texte, hauteur, largeur, couleur de fonds, couleur d'écriture, épaisseur de bordure et type de relief
button_1 = Label(main_window, text ="1", height=4, width=5, bg="#211180", fg="#ffffff", borderwidth="1", relief="raised")
button_2 = Label(main_window, text ="2", height=4, width=5, bg="#211180", fg="#ffffff", borderwidth="1", relief="raised")
button_3 = Label(main_window, text ="3", height=4, width=5, bg="#211180", fg="#ffffff", borderwidth="1", relief="raised")
button_4 = Label(main_window, text ="4", height=4, width=5, bg="#211180", fg="#ffffff", borderwidth="1", relief="raised")
button_5 = Label(main_window, text ="5", height=4, width=5, bg="#211180", fg="#ffffff", borderwidth="1", relief="raised")
button_6 = Label(main_window, text ="6", height=4, width=5, bg="#211180", fg="#ffffff", borderwidth="1", relief="raised")
button_7 = Label(main_window, text ="7", height=4, width=5, bg="#211180", fg="#ffffff", borderwidth="1", relief="raised")
button_8 = Label(main_window, text ="8", height=4, width=5, bg="#211180", fg="#ffffff", borderwidth="1", relief="raised")
button_9 = Label(main_window, text ="9", height=4, width=5, bg="#211180", fg="#ffffff", borderwidth="1", relief="raised")
button_0 = Label(main_window, text ="0", height=4, width=5, bg="#211180", fg="#ffffff", borderwidth="1", relief="raised")
button_clear = Label(main_window, text ="C", height=4, width=5, bg="#747287", fg="#ffffff", borderwidth="1", relief="raised")
button_equal = Label(main_window, text ="=", height=4, width=5, bg="#747287", fg="#ffffff", borderwidth="1", relief="raised")
button_add = Label(main_window, text ="+", height=4, width=5, bg="#747287", fg="#ffffff", borderwidth="1", relief="raised")
button_sub = Label(main_window, text ="-", height=4, width=5, bg="#747287", fg="#ffffff", borderwidth="1", relief="raised")
button_mul = Label(main_window, text ="x", height=4, width=5, bg="#747287", fg="#ffffff", borderwidth="1", relief="raised")
button_div = Label(main_window, text ="/", height=4, width=5, bg="#747287", fg="#ffffff", borderwidth="1", relief="raised")

# Après avoir créé les variables des boutons, il faut les positionner dans notre fenêtre
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_add.grid(row=1, column=4)
button_sub.grid(row=2, column=4)
button_mul.grid(row=3, column=4)
button_div.grid(row=4, column=4)

# Rendre les boutons cliquables et les associer à leur fonctions
# <Button-1> correspond à un évenement : le clique gauche de la souris
button_1.bind("<Button-1>", lambda e, button_1=button_1: click_button("1"))
button_2.bind("<Button-1>", lambda e, button_2=button_2: click_button("2"))
button_3.bind("<Button-1>", lambda e, button_3=button_3: click_button("3"))
button_4.bind("<Button-1>", lambda e, button_4=button_4: click_button("4"))
button_5.bind("<Button-1>", lambda e, button_5=button_5: click_button("5"))
button_6.bind("<Button-1>", lambda e, button_6=button_6: click_button("6"))
button_7.bind("<Button-1>", lambda e, button_7=button_7: click_button("7"))
button_8.bind("<Button-1>", lambda e, button_8=button_8: click_button("8"))
button_9.bind("<Button-1>", lambda e, button_9=button_9: click_button("9"))
button_0.bind("<Button-1>", lambda e, button_0=button_0: click_button("0"))
button_clear.bind("<Button-1>", lambda e, button_clear=button_clear: effacer())
button_equal.bind("<Button-1>", lambda e, button_equal=button_equal: click_button("="))
button_add.bind("<Button-1>", lambda e, button_add=button_add: click_button("+"))
button_sub.bind("<Button-1>", lambda e, button_sub=button_sub: click_button("-"))
button_mul.bind("<Button-1>", lambda e, button_mul=button_mul: click_button("*"))
button_div.bind("<Button-1>", lambda e, button_div=button_div: click_button("/"))

# event loop
main_window.mainloop()