#! /usr/bin/env python
#  -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import askyesno

from PIL import ImageTk, Image

import UrnesDePolyaV2 as urnes

app = tk.Tk()

def clear_frame():
   app.labelErreur.configure(text="")
   for widgets in app.frameGraphe.winfo_children():
      widgets.destroy()
    
def calculerUrne():
    clear_frame()
    nbIter = int(app.saisieNbIter.get())
    nbSimul = int(app.saisieNbSimul.get())
    operation = str(app.boxActionTirage.get())
    nbBquandB = int(app.saisieBLorsDeTirageB.get())
    nbRquandB = int(app.saisieRLorsDeTirageB.get())
    nbBquandR = int(app.saisieBLorsDeTirageR.get())
    nbRquandR = int(app.saisieRLorsDeTirageR.get())
    nbBstart=int(app.saisieBleueIni.get())
    nbRstart=int(app.saisieRougeIni.get())
    try:
        urnes.tracerUrnes(nbIter, nbSimul, nbBquandB, nbRquandB, nbBquandR, nbRquandR, operation, nbBstart, nbRstart)
        img = Image.open("simul.png")
        photo = ImageTk.PhotoImage(img)
        label = tk.Label(app.frameGraphe, image=photo)
        label.image = photo
        label.pack()
    except Exception as e:
        s = str(e)
        app.labelErreur.configure(text=s)

def quitter():
    answer = askyesno(title="Confirmation", message="Voulez-vous vraiment quitter ?")
    if answer:
        app.destroy()

def reset():
    answer = askyesno(title="Confirmation", message="Voulez-vous vraiment remettre tous les paramètres aux valeurs par défaut ?")
    if answer:
        app.saisieNbIter.delete(0, "end")
        app.saisieNbIter.insert("end", "400")
        app.saisieNbSimul.delete(0, "end")
        app.saisieNbSimul.insert("end", "20")
        app.saisieBleueIni.delete(0, "end")
        app.saisieBleueIni.insert("end", "1")
        app.saisieRougeIni.delete(0, "end")
        app.saisieRougeIni.insert("end", "1")
        app.saisieBLorsDeTirageB.delete(0, "end")
        app.saisieBLorsDeTirageB.insert("end", "1")
        app.saisieRLorsDeTirageB.delete(0, "end")
        app.saisieRLorsDeTirageB.insert("end", "0")
        app.saisieBLorsDeTirageR.delete(0, "end")
        app.saisieBLorsDeTirageR.insert("end", "0")
        app.saisieRLorsDeTirageR.delete(0, "end")
        app.saisieRLorsDeTirageR.insert("end", "1")

def entryValidation(S):
    for c in S:
        if c not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-']:
            app.bell()
            return False
    return True

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana2color = 'beige' # X11 color: #f5f5dc
app.style = ttk.Style()
app.style.configure('.',background=_bgcolor)
app.style.configure('.',foreground=_fgcolor)
app.style.configure('.',font="TkDefaultFont")
app.style.map('.',background=
    [('selected', _compcolor), ('active',_ana2color)])

app.geometry("1075x430")
app.title("Urnes de Polya")
app.configure(background="#d9d9d9")
app.resizable(False, False)

app.combobox = tk.StringVar()

app.frameNbIterSimul = tk.Frame(app)
app.frameNbIterSimul.place(relx=0.011, rely=0.022, relheight=0.278 ,relwidth=0.387)
app.frameNbIterSimul.configure(relief='groove')
app.frameNbIterSimul.configure(borderwidth="2")
app.frameNbIterSimul.configure(relief="groove")
app.frameNbIterSimul.configure(background="#d9d9d9")

vcmd = (app.register(entryValidation), '%S')

# Frame saisie paramètres itération, simulation

app.saisieNbIter = tk.Entry(app.frameNbIterSimul, validate='key', vcmd=vcmd)
app.saisieNbIter.place(relx=0.577, rely=0.08, height=20, relwidth=0.307)
app.saisieNbIter.configure(background="white")
app.saisieNbIter.configure(disabledforeground="#a3a3a3")
app.saisieNbIter.configure(font="TkFixedFont")
app.saisieNbIter.configure(foreground="black")
app.saisieNbIter.configure(highlightbackground="#d9d9d9")
app.saisieNbIter.configure(highlightcolor="black")
app.saisieNbIter.configure(insertbackground="black")
app.saisieNbIter.configure(selectbackground="#c4c4c4")
app.saisieNbIter.configure(selectforeground="black")
app.saisieNbIter.insert("end", "400")

app.labelNbIter = tk.Label(app.frameNbIterSimul)
app.labelNbIter.place(relx=0.077, rely=0.08, height=21, width=127)
app.labelNbIter.configure(anchor='w')
app.labelNbIter.configure(background="#d9d9d9")
app.labelNbIter.configure(compound='left')
app.labelNbIter.configure(disabledforeground="#a3a3a3")
app.labelNbIter.configure(foreground="#000000")
app.labelNbIter.configure(justify='right')
app.labelNbIter.configure(text='''Nombre d'itérations''')

app.saisieNbSimul = tk.Entry(app.frameNbIterSimul, validate='key', vcmd=vcmd)
app.saisieNbSimul.place(relx=0.577, rely=0.48, height=20, relwidth=0.307)
app.saisieNbSimul.configure(background="white")
app.saisieNbSimul.configure(disabledforeground="#a3a3a3")
app.saisieNbSimul.configure(font="TkFixedFont")
app.saisieNbSimul.configure(foreground="black")
app.saisieNbSimul.configure(highlightbackground="#d9d9d9")
app.saisieNbSimul.configure(highlightcolor="black")
app.saisieNbSimul.configure(insertbackground="black")
app.saisieNbSimul.configure(selectbackground="#c4c4c4")
app.saisieNbSimul.configure(selectforeground="black")
app.saisieNbSimul.insert("end", "20")

app.labelNbSimul = tk.Label(app.frameNbIterSimul)
app.labelNbSimul.place(relx=0.077, rely=0.48, height=21, width=137)
app.labelNbSimul.configure(activebackground="#f9f9f9")
app.labelNbSimul.configure(anchor='w')
app.labelNbSimul.configure(background="#d9d9d9")
app.labelNbSimul.configure(compound='left')
app.labelNbSimul.configure(disabledforeground="#a3a3a3")
app.labelNbSimul.configure(foreground="#000000")
app.labelNbSimul.configure(highlightbackground="#d9d9d9")
app.labelNbSimul.configure(highlightcolor="black")
app.labelNbSimul.configure(justify='right')
app.labelNbSimul.configure(text="Nombre de simulations")

# Frame du graphe

app.frameGraphe = tk.Frame(app)
app.frameGraphe.place(relx=0.424, rely=0.022, relheight=0.889
        , relwidth=0.565)
app.frameGraphe.configure(relief='groove')
app.frameGraphe.configure(borderwidth="2")
app.frameGraphe.configure(relief="groove")
app.frameGraphe.configure(background="white")

# Frame des paramètres sur les boules

app.frameTirageBoule = tk.Frame(app)
app.frameTirageBoule.place(relx=0.011, rely=0.311, relheight=0.489
        , relwidth=0.387)
app.frameTirageBoule.configure(relief='groove')
app.frameTirageBoule.configure(borderwidth="2")
app.frameTirageBoule.configure(relief="groove")
app.frameTirageBoule.configure(background="#d9d9d9")

# - Paramètres de boules initiaux

app.labelnbInitialBoules = ttk.Label(app.frameTirageBoule)
app.labelnbInitialBoules.place(relx=0.036, rely=0.05, height=20, width=150)
app.labelnbInitialBoules.configure(background="#d9d9d9")
app.labelnbInitialBoules.configure(foreground="#000000")
app.labelnbInitialBoules.configure(font="TkDefaultFont")
app.labelnbInitialBoules.configure(relief="flat")
app.labelnbInitialBoules.configure(anchor='w')
app.labelnbInitialBoules.configure(justify='left')
app.labelnbInitialBoules.configure(text="Nombre initial de boules")
app.labelnbInitialBoules.configure(compound='left')

app.saisieBleueIni = tk.Entry(app.frameTirageBoule, validate='key', vcmd=vcmd)
app.saisieBleueIni.place(relx=0.036, rely=0.15, height=20, relwidth=0.161)
app.saisieBleueIni.configure(background="white")
app.saisieBleueIni.configure(disabledforeground="#a3a3a3")
app.saisieBleueIni.configure(font="TkFixedFont")
app.saisieBleueIni.configure(foreground="#000000")
app.saisieBleueIni.configure(insertbackground="black")
app.saisieBleueIni.configure(selectbackground="#c4c4c4")
app.saisieBleueIni.configure(selectforeground="black")
app.saisieBleueIni.insert("end", "1")

app.labelBleueIni = ttk.Label(app.frameTirageBoule)
app.labelBleueIni.place(relx=0.2, rely=0.15, height=20)
app.labelBleueIni.configure(background="#d9d9d9")
app.labelBleueIni.configure(foreground="#000000")
app.labelBleueIni.configure(font="TkDefaultFont")
app.labelBleueIni.configure(relief="flat")
app.labelBleueIni.configure(anchor='w')
app.labelBleueIni.configure(justify='left')
app.labelBleueIni.configure(text='''Bleue(s)''')
app.labelBleueIni.configure(compound='left')

app.saisieRougeIni = tk.Entry(app.frameTirageBoule, validate='key', vcmd=vcmd)
app.saisieRougeIni.place(relx=0.5, rely=0.15, height=20, relwidth=0.161)
app.saisieRougeIni.configure(background="white")
app.saisieRougeIni.configure(disabledforeground="#a3a3a3")
app.saisieRougeIni.configure(font="TkFixedFont")
app.saisieRougeIni.configure(foreground="#000000")
app.saisieRougeIni.configure(insertbackground="black")
app.saisieRougeIni.configure(selectbackground="#c4c4c4")
app.saisieRougeIni.configure(selectforeground="black")
app.saisieRougeIni.insert("end", "1")

app.labelRougeIni = ttk.Label(app.frameTirageBoule)
app.labelRougeIni.place(relx=0.664, rely=0.15, height=20)
app.labelRougeIni.configure(background="#d9d9d9")
app.labelRougeIni.configure(foreground="#000000")
app.labelRougeIni.configure(font="TkDefaultFont")
app.labelRougeIni.configure(relief="flat")
app.labelRougeIni.configure(anchor='w')
app.labelRougeIni.configure(justify='left')
app.labelRougeIni.configure(text='''Rouge(s)''')
app.labelRougeIni.configure(compound='left')


app.separator = ttk.Separator(app.frameTirageBoule)
app.separator.place(relx=0.05, rely=0.3,  relwidth=0.9)
app.separator.configure(orient="horizontal")

# - Paramètres de boules lors du tirage

app.labelActionTirage = ttk.Label(app.frameTirageBoule)
app.labelActionTirage.place(relx=0.036, rely=0.374, height=20, width=90)
app.labelActionTirage.configure(background="#d9d9d9")
app.labelActionTirage.configure(foreground="#000000")
app.labelActionTirage.configure(font="TkDefaultFont")
app.labelActionTirage.configure(relief="flat")
app.labelActionTirage.configure(anchor='w')
app.labelActionTirage.configure(justify='left')
app.labelActionTirage.configure(text='''Lors du tirage,''')
app.labelActionTirage.configure(compound='left')

app.boxActionTirage = ttk.Combobox(app.frameTirageBoule, state="readonly", values=["Additionner", "Multiplier","Aleatoire"])
app.boxActionTirage.place(relx=0.255, rely=0.374, relheight=0.081, width=100)
app.boxActionTirage.configure(textvariable=app.combobox)
app.boxActionTirage.configure(takefocus="#c4c4c4")
app.boxActionTirage.current(0)

app.labelTirageR = ttk.Label(app.frameTirageBoule)
app.labelTirageR.place(relx=0.5, rely=0.563, height=20, width=121)
app.labelTirageR.configure(background="#d9d9d9")
app.labelTirageR.configure(foreground="#000000")
app.labelTirageR.configure(font="TkDefaultFont")
app.labelTirageR.configure(relief="flat")
app.labelTirageR.configure(anchor='w')
app.labelTirageR.configure(justify='left')
app.labelTirageR.configure(text='''Tirage d'une Rouge''')
app.labelTirageR.configure(compound='left')

app.labelTirageB = ttk.Label(app.frameTirageBoule)
app.labelTirageB.place(relx=0.036, rely=0.563, height=20, width=111)
app.labelTirageB.configure(background="#d9d9d9")
app.labelTirageB.configure(foreground="#000000")
app.labelTirageB.configure(font="TkDefaultFont")
app.labelTirageB.configure(relief="flat")
app.labelTirageB.configure(anchor='w')
app.labelTirageB.configure(justify='left')
app.labelTirageB.configure(text='''Tirage d'une Bleue''')
app.labelTirageB.configure(compound='left')

app.separator = ttk.Separator(app.frameTirageBoule)
app.separator.place(relx=0.464, rely=0.504,  relheight=0.678)
app.separator.configure(orient="vertical")

app.saisieBLorsDeTirageB = tk.Entry(app.frameTirageBoule, validate='key', vcmd=vcmd)
app.saisieBLorsDeTirageB.place(relx=0.036, rely=0.678, height=20, relwidth=0.161)
app.saisieBLorsDeTirageB.configure(background="white")
app.saisieBLorsDeTirageB.configure(disabledforeground="#a3a3a3")
app.saisieBLorsDeTirageB.configure(font="TkFixedFont")
app.saisieBLorsDeTirageB.configure(foreground="#000000")
app.saisieBLorsDeTirageB.configure(insertbackground="black")
app.saisieBLorsDeTirageB.configure(selectbackground="#c4c4c4")
app.saisieBLorsDeTirageB.configure(selectforeground="black")
app.saisieBLorsDeTirageB.insert("end", "1")

app.labelBlorsDeTirageB = ttk.Label(app.frameTirageBoule)
app.labelBlorsDeTirageB.place(relx=0.2, rely=0.678, height=20)
app.labelBlorsDeTirageB.configure(background="#d9d9d9")
app.labelBlorsDeTirageB.configure(foreground="#000000")
app.labelBlorsDeTirageB.configure(font="TkDefaultFont")
app.labelBlorsDeTirageB.configure(relief="flat")
app.labelBlorsDeTirageB.configure(anchor='w')
app.labelBlorsDeTirageB.configure(justify='left')
app.labelBlorsDeTirageB.configure(text='''Bleue(s)''')
app.labelBlorsDeTirageB.configure(compound='left')

app.saisieRLorsDeTirageB = tk.Entry(app.frameTirageBoule, validate='key', vcmd=vcmd)
app.saisieRLorsDeTirageB.place(relx=0.036, rely=0.83, height=20, relwidth=0.161)
app.saisieRLorsDeTirageB.configure(background="white")
app.saisieRLorsDeTirageB.configure(disabledforeground="#a3a3a3")
app.saisieRLorsDeTirageB.configure(font="TkFixedFont")
app.saisieRLorsDeTirageB.configure(foreground="#000000")
app.saisieRLorsDeTirageB.configure(highlightbackground="#d9d9d9")
app.saisieRLorsDeTirageB.configure(highlightcolor="black")
app.saisieRLorsDeTirageB.configure(insertbackground="black")
app.saisieRLorsDeTirageB.configure(selectbackground="#c4c4c4")
app.saisieRLorsDeTirageB.configure(selectforeground="black")
app.saisieRLorsDeTirageB.insert("end", "0")

app.labelRlorsDeTirageB = ttk.Label(app.frameTirageBoule)
app.labelRlorsDeTirageB.place(relx=0.2, rely=0.83, height=20)
app.labelRlorsDeTirageB.configure(background="#d9d9d9")
app.labelRlorsDeTirageB.configure(foreground="#000000")
app.labelRlorsDeTirageB.configure(font="TkDefaultFont")
app.labelRlorsDeTirageB.configure(relief="flat")
app.labelRlorsDeTirageB.configure(anchor='w')
app.labelRlorsDeTirageB.configure(justify='left')
app.labelRlorsDeTirageB.configure(text='''Rouge(s)''')
app.labelRlorsDeTirageB.configure(compound='left')

app.saisieBLorsDeTirageR = tk.Entry(app.frameTirageBoule, validate='key', vcmd=vcmd)
app.saisieBLorsDeTirageR.place(relx=0.5, rely=0.678, height=20, relwidth=0.161)
app.saisieBLorsDeTirageR.configure(background="white")
app.saisieBLorsDeTirageR.configure(disabledforeground="#a3a3a3")
app.saisieBLorsDeTirageR.configure(font="TkFixedFont")
app.saisieBLorsDeTirageR.configure(foreground="#000000")
app.saisieBLorsDeTirageR.configure(highlightbackground="#d9d9d9")
app.saisieBLorsDeTirageR.configure(highlightcolor="black")
app.saisieBLorsDeTirageR.configure(insertbackground="black")
app.saisieBLorsDeTirageR.configure(selectbackground="#c4c4c4")
app.saisieBLorsDeTirageR.configure(selectforeground="black")
app.saisieBLorsDeTirageR.insert("end", "0")

app.labelBLorsDeTirageR = ttk.Label(app.frameTirageBoule)
app.labelBLorsDeTirageR.place(relx=0.664, rely=0.678, height=20)
app.labelBLorsDeTirageR.configure(background="#d9d9d9")
app.labelBLorsDeTirageR.configure(foreground="#000000")
app.labelBLorsDeTirageR.configure(font="TkDefaultFont")
app.labelBLorsDeTirageR.configure(relief="flat")
app.labelBLorsDeTirageR.configure(anchor='w')
app.labelBLorsDeTirageR.configure(justify='left')
app.labelBLorsDeTirageR.configure(text='''Bleue(s)''')
app.labelBLorsDeTirageR.configure(compound='left')

app.saisieRLorsDeTirageR = tk.Entry(app.frameTirageBoule, validate='key', vcmd=vcmd)
app.saisieRLorsDeTirageR.place(relx=0.5, rely=0.83, height=20, relwidth=0.161)
app.saisieRLorsDeTirageR.configure(background="white")
app.saisieRLorsDeTirageR.configure(disabledforeground="#a3a3a3")
app.saisieRLorsDeTirageR.configure(font="TkFixedFont")
app.saisieRLorsDeTirageR.configure(foreground="#000000")
app.saisieRLorsDeTirageR.configure(highlightbackground="#d9d9d9")
app.saisieRLorsDeTirageR.configure(highlightcolor="black")
app.saisieRLorsDeTirageR.configure(insertbackground="black")
app.saisieRLorsDeTirageR.configure(selectbackground="#c4c4c4")
app.saisieRLorsDeTirageR.configure(selectforeground="black")
app.saisieRLorsDeTirageR.insert("end", "1")

app.labelRLorsDeTirageR = ttk.Label(app.frameTirageBoule)
app.labelRLorsDeTirageR.place(relx=0.664, rely=0.83, height=20)
app.labelRLorsDeTirageR.configure(background="#d9d9d9")
app.labelRLorsDeTirageR.configure(foreground="#000000")
app.labelRLorsDeTirageR.configure(font="TkDefaultFont")
app.labelRLorsDeTirageR.configure(relief="flat")
app.labelRLorsDeTirageR.configure(anchor='w')
app.labelRLorsDeTirageR.configure(justify='left')
app.labelRLorsDeTirageR.configure(text='''Rouge(s)''')
app.labelRLorsDeTirageR.configure(compound='left')

# Boutons et label pour les messages d'erreur

app.boutonQuit = tk.Button(app, command=quitter)
app.boutonQuit.place(relx=0.32, rely=0.844, height=24, width=80)
app.boutonQuit.configure(activebackground="beige")
app.boutonQuit.configure(activeforeground="#000000")
app.boutonQuit.configure(background="#d9d9d9")
app.boutonQuit.configure(compound='left')
app.boutonQuit.configure(highlightbackground="#d9d9d9")
app.boutonQuit.configure(highlightcolor="black")
app.boutonQuit.configure(pady="0")
app.boutonQuit.configure(text="Quitter")

app.boutonReset = tk.Button(app, command=reset)
app.boutonReset.place(relx=0.165, rely=0.844, height=24, width=80)
app.boutonReset.configure(activebackground="beige")
app.boutonReset.configure(activeforeground="#000000")
app.boutonReset.configure(background="#d9d9d9")
app.boutonReset.configure(compound='left')
app.boutonReset.configure(highlightbackground="#d9d9d9")
app.boutonReset.configure(highlightcolor="black")
app.boutonReset.configure(pady="0")
app.boutonReset.configure(text="Réinitialiser")

app.boutonValider = tk.Button(app,command=calculerUrne)
app.boutonValider.place(relx=0.01, rely=0.844, height=24, width=80)
app.boutonValider.configure(activebackground="beige")
app.boutonValider.configure(activeforeground="#000000")
app.boutonValider.configure(background="#d9d9d9")
app.boutonValider.configure(compound='left')
app.boutonValider.configure(highlightbackground="green")
app.boutonValider.configure(highlightcolor="black")
app.boutonValider.configure(pady="0")
app.boutonValider.configure(text="Valider")

app.labelErreur = ttk.Label(app)
app.labelErreur.place(relx=0.01, rely=0.93, width=3000)
app.labelErreur.configure(background="#d9d9d9")
app.labelErreur.configure(foreground="red")
app.labelErreur.configure(font="TkDefaultFont")
app.labelErreur.configure(relief="flat")
app.labelErreur.configure(anchor='w')
app.labelErreur.configure(justify='left')
app.labelErreur.configure(text="")
app.labelErreur.configure(compound='left')

app.menubar = tk.Menu(app,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
app.configure(menu = app.menubar)

app.mainloop()