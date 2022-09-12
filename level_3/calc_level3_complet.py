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
	if len(expression) < 15:
		expression += str(touche)
		equation.set(expression)
	else:
		equation.set("Erreur")
		expression = ""
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

Boutons = [7, 8, 9, "+", 4, 5, 6, "-", 1, 2, 3, "*", 0, "C", "=", "/"];
ligne = 1;
colonne = 0;

for bouton in Boutons:
	button = Label(main_window, text = str(bouton), height=4, width=5, bg="#211180", fg="#ffffff", borderwidth="1", relief="raised")
		
	button.grid(row=ligne, column=colonne)
	if bouton == "C":
		button.bind("<Button-1>", lambda e: effacer())
	else:
		button.bind("<Button-1>", lambda e, bouton = bouton: click_button(bouton))
 
	colonne += 1
	if colonne == 4:
		colonne = 0
		ligne += 1

# event loop
main_window.mainloop()