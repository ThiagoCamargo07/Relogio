import tkinter as tk
from tkinter import *
import os
from time import strftime

# criar interface do relogio
root = tk.Tk()
root.title("Relógio")
root.geometry("600x320")
root.maxsize(600,320)
root.minsize(600,320)
root.configure(background = "#1d1d1d")


#pegar nome do usuario de acordo com o seu nome no computador
def get_saudacao():
    nome_usuario = os.getlogin()
    nome_saudacao.config(text=f"Olá {nome_usuario}")

#pegar informações do dia,ano etc...
def get_data():
    data_atual = strftime("%a,%d %b %y")
    data.config(text=data_atual)


#pegar hora aual
def get_horas():
    hora_atual = strftime("%H:%M:%S")
    horas.config(text=hora_atual)
    horas.after(1000,get_horas)



tela =tk.Canvas(root,width=600,height=60,bg="#1d1d1d",bd=0,highlightthickness=0,relief="ridge")
tela.pack()

nome_saudacao = Label(root,bg="#1d1d1d",fg="#8e27ea",font=("Calibre",16))
nome_saudacao.pack()

data = Label(root,bg="#1d1d1d",fg="#8e27ea",font=("Calibre"))
data.pack(pady=1)

horas = Label(root,bg="#1d1d1d",fg="#8e27ea",font=("Calibre",64,"bold"))
horas.pack(pady=10)


get_saudacao()
get_data()
get_horas()
root.mainloop()
