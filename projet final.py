
#--------Création de space pong par Youri -------------

from tkinter import *
import tkinter.font as tkFont
import tkinter
import random
FenMen = Tk()

#----------------------------Variables-----------------------------

x,y,w,z,delta,u,v,delta2,delta3 =30,30,1350,30,5,300,300,8,8
m, n, delta4= 650, 50, 5
largeur = 1400
hauteur = 700



#------------------------programme pricipal------------------------
FenMen.geometry('900x600')

def quitter():
    FenMen.destroy()
 
def jeu():
    global x,y,w,z,delta,u,v,delta2,delta3,m, n, delta4,largeur,hauteur, pts1, pts2, pJ1,pJ2,k,q

    #-----------------------------fonctions----------------------------

    #--déplacement palette de gauche---
    def deplaceVB(event):
        global y, delta
        if y+100 >= hauteur:
            delta = 0
            y=y+delta
        else :
            y=y+20
        Moncadre.coords(rectangle, x, y, x+20, y+100)

    def deplaceVH(event):
        global y, delta
        if y <= 0:
            delta = 0
            y=y+delta
        else :
            y=y-20
        Moncadre.coords(rectangle, x, y, x+20, y+100)

    #---déplacement pallette de droite---

    def deplaceVB2(event):
        global z, delta
        if z+100 >= hauteur:
            delta = 0
            z=z+delta
        else :
            z=z+20
        Moncadre.coords(rectangle2, w, z, w+20, z+100)

    def deplaceVH2(event):
        global z, delta
        if z <= 0:
            delta = 0
            z=z+delta
        else :
            z=z-20
        Moncadre.coords(rectangle2, w, z, w+20, z+100)

    #---déplacement de la balle---

    def deplaceballe():
        global u,delta3,v,delta2,x,pJ1,pJ2,pts1,pts2
        if (v<=0)or(v+20>=hauteur):
            delta3=delta3
            delta2=-delta2
        if ((v+20)>=z) and ((u+20)>=1350) and ((v+20)<=z+100):
            delta3=-delta3
            delta2=delta2+random.randint(-2,3)
        if ((v+20)>=y) and ((v+20)<=y+100) and (u<=50):
            delta3=-delta3
            delta2=delta2+random.randint(-2,3)
        if (u<=0):
            u=700
            v=350
            q=pJ2.get()
            q=int(q)+1
            pJ2.set(str(q))
        if (u>=largeur):
            u=700
            v=350
            k=pJ1.get()
            k=int(k)+1
            pJ1.set(str(k))
        if (u<=m) and (v>=n) and (v+20<=n+150) and (u+20>=m):
            delta2=-delta2
            delta3=-delta3
        if (u<=m+50) and (v>=n) and (v+20<=n+150) and (m+50<=u+20):
            delta2=-delta2
            delta3=-delta3
        if (v+20>=n) and (u+20>=m) and (u<=m+50) and (v<=n+150):
            delta2=-delta2

        pts1=int(pJ1.get())
        pts2=int(pJ2.get())
        if pts1>=5:
            FenJeu.destroy()
        if pts2>=5:
            FenJeu.destroy()

        u=u+delta3
        v=v-delta2



    #---Suppression des blocs---

        for k in range(10):
            if(u<=20) and (70*k<=v<=70*k+70) and(bloc3[k]==1):
                bloc3[k]=0
                Moncadre.delete(bloc[k])
                delta3=-delta3
        for k in range(10):
            if(u+20>=1380) and (70*k<=v<=70*k+70)and(bloc4[k]==1):
                bloc4[k]=0
                Moncadre.delete(bloc2[k])
                delta3=-delta3

        Moncadre.coords(balle, u, v, u+20, v+20)
        FenJeu.after(20,deplaceballe)

    #---Déplacement du module---

    def deplacemodule():
        global n, delta4
        if (n+150 >= hauteur) or (n <= 0):
            delta4 = -delta4

        n=n+delta4
        Moncadre.coords(module, m, n, m+50, n+150)
        FenJeu.after(20,deplacemodule)



    FenMen.destroy()
    FenJeu=Tk()
    FenJeu.geometry('1400x800')

    Moncadre = Canvas(FenJeu, width = largeur, height = hauteur)
    photo = PhotoImage(file="fond.gif")
    Moncadre.create_image(0, 0, anchor=NW, image=photo)
    Moncadre.pack()

    #---score---

    pJ1=StringVar()
    pJ2=StringVar()
    pJ1.set(str(0))
    pJ2.set(str(0))


    score1=tkFont.Font( size=20, weight='bold')
    score= Label(FenJeu,text='SCORE',font=score1)
    score.pack()
    score.place(x=660, y=720)
    scoreJ1= Label (FenJeu,textvariable=pJ1,font=score1)
    scoreJ1.pack()
    scoreJ1.place(x=660, y=760)
    scoreJ2= Label (FenJeu,textvariable=pJ2,font=score1)
    scoreJ2.pack()
    scoreJ2.place(x=740, y=760)

    #---Définitions des blocs,palettes et de la balle---

    rectangle= Moncadre.create_rectangle(x, y, x+20, y+100, fill='blue')
    rectangle2= Moncadre.create_rectangle(w, z, w+20, z+100, fill='blue')
    module= Moncadre.create_rectangle(m, n, m+50, n+150, fill="green")

    bloc=list(range(10))
    bloc2=list(range(10))
    bloc3=[1,1,1,1,1,1,1,1,1,1]
    bloc4=[1,1,1,1,1,1,1,1,1,1]

    for k in range (10):
        bloc[k]=Moncadre.create_rectangle(0, 0+70*k, 20, 70+70*k, fill='brown')
        bloc2[k]=Moncadre.create_rectangle(1380, 0+70*k, 1400, 70+70*k, fill='brown')

    balle= Moncadre.create_oval(u, v, u+20, v+20, fill='red')

    #---déplacements---

    deplaceballe()

    deplacemodule()


    Moncadre.pack()

    FenJeu.bind('s', deplaceVB)
    FenJeu.bind('z', deplaceVH)

    FenJeu.bind('l', deplaceVB2)
    FenJeu.bind('o', deplaceVH2)

    FenJeu.mainloop()




title=tkFont.Font( size=80, weight='bold', )

titre= Label (FenMen, text='Space Pong', font=title, padx=25, pady=60)
titre.pack()

dem= Button (FenMen,  bg='grey', text='PLAY',activeforeground='red', overrelief= 'raised', borderwidth=5,font = ('Helvetia',20), padx=25, pady=5, command=jeu)
dem.pack()


quitte= Button (FenMen,  bg='grey', text='QUIT',activeforeground='red', overrelief= 'raised', borderwidth=5,font = ('Helvetia',20), padx=25, pady=5, command=quitter)
quitte.pack()

Moncadre = Canvas(FenMen, width = 900, height = 300)

Moncadre.pack()

Message=Moncadre.create_text(0,400, fill='bisque', text = 'Hello , welcome to the Space Pong \n les regles sont simples : il faut marquer chez son adversaire, pour cela il faut bouger sa palette avec les touches Z et S ou O et L', font= ('Helvetia',10))


FenMen.mainloop()




