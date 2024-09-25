#Installe d'abord tkinter: pip3 install tkinter

#Format
"""
----
789*
456-
123+
0,/=
----
"""


from tkinter import * #importer tout

expression = ""

def appuyer(touche):
    if touche == "=":
        calculer()
        return
    
    global expression
    expression += str(touche)
    equation.set(expression)

def calculer():
    try:
        global expression
        total = str(eval(expression))

        equation.set(total)
        expression = total
    except:
        equation.set("erreur")
        expression=""

def effacer():
    global expression
    expression = ""
    equation.set("")
    
    
#Designe
if __name__ =="__main__":
    gui = Tk() #gui: graphical user interface
    gui.configure(background="#74EC8D")
    gui.title("calculatrice")
    gui.geometry("235x385")
    
    
    equation = StringVar()
    resultat = Label(gui, bg="#74EC8D", fg="#FFF", textvariable=equation, height=2)
    resultat.grid(columnspan=4)
    
    # Boutons
    boutons = [7, 8, 9, "*", 4, 5, 6, "-", 1, 2, 3, "+", 0, ".", "/", "="]
    ligne = 1
    colonne = 0
    
    for bouton in boutons :
        b = Label(gui, text=str(bouton), bg="#7E7E7E", fg="#FFF", height=5, width=8)
        #Rendre le texte cliquable
        b.bind("<Button-1>", lambda e, bouton=bouton: appuyer(bouton))
        
        b.grid(row=ligne, column=colonne)
        
        colonne += 1
        if colonne == 4:
            colonne = 0
            ligne += 1
            
    #Pour effacer
    b = Label(gui, text="Effacer", bg="#F9968B", fg="#FFF", height=1, width=30)
    b.bind("<Button-1>", lambda e: effacer())
    b.grid(columnspan=4)
    
    gui.mainloop()