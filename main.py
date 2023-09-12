#Importando biblioteca Tkinter, utilizada para criar interface
from tkinter import *
from tkinter import ttk

#Cores
cor1 = "#1e1f1e" #preto
cor2 = "#feffff" #Branco 
cor3 = "#38576b" #azul
cor4 = "#ECEFF1" #cizento
cor5 = "#FFAB40" #laranja

#Criando a janela 
janela = Tk()
janela.title("Calculadora")

#alterando a cor da janela
janela.config(bg=cor1)

#largura e comprimento da janela
janela.geometry("235x309")

#dividindo a janela em duas partes
Frame_tela = Frame(janela, width=235, height=50, bg=cor3)
Frame_tela.grid(row=0, column=0)

#Criando o corpo
Frame_corpo = Frame(janela, width=235, height=268)
Frame_corpo.grid(row=1, column=0)

#Criando a lógica da calculadora
todos_valores = ""
def digitar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    valor_texto.set(todos_valores)

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(resultado)

def limpar():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

#Criando label
valor_texto = StringVar()
app_label = Label(Frame_tela, textvariable = valor_texto, width=17, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=("ivy 17"), bg=cor3, fg=cor2)
app_label.place(x=0,y=0)


#Criando botões

#Botões = C, % e /
b1 = Button(Frame_corpo, command=limpar, text="C", width=11, height=2, bg=cor4, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b1.place(x=0, y=0)
b2 = Button(Frame_corpo, command = lambda: digitar_valores("%"), text="%", width=5, height=2, bg=cor4, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b2.place(x=120, y=0)
b3 = Button(Frame_corpo, command = lambda: digitar_valores("/"), text="/", width=5, height=2, bg=cor5, fg=cor2, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b3.place(x=180, y=0)

#Botões = 7, 8, 9 e *
b4 = Button(Frame_corpo, command = lambda: digitar_valores("7"), text="7", width=5, height=2, bg=cor4, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b4.place(x=0, y=52)
b5 = Button(Frame_corpo, command = lambda: digitar_valores("8"), text="8", width=5, height=2, bg=cor4, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b5.place(x=60, y=52)
b6 = Button(Frame_corpo, command = lambda: digitar_valores("9"), text="9", width=5, height=2, bg=cor4, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b6.place(x=120, y=52)
b7 = Button(Frame_corpo, command = lambda: digitar_valores("*"), text="*", width=5, height=2, bg=cor5, fg=cor2, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b7.place(x=180, y=52)

#Botões = 4, 5, 6 e -
b8 = Button(Frame_corpo, command = lambda: digitar_valores("4"), text="4", width=5, height=2, bg=cor4, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b8.place(x=0, y=104)
b9 = Button(Frame_corpo, command = lambda: digitar_valores("5"), text="5", width=5, height=2, bg=cor4, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b9.place(x=60, y=104)
b10 = Button(Frame_corpo, command = lambda: digitar_valores("6"), text="6", width=5, height=2, bg=cor4, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b10.place(x=120, y=104)
b11 = Button(Frame_corpo, command = lambda: digitar_valores("-"), text="-", width=5, height=2, bg=cor5, fg=cor2, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b11.place(x=180, y=104)

#Botões = 1, 2, 3 e +
b12 = Button(Frame_corpo, command = lambda: digitar_valores("1"), text="1", width=5, height=2, bg=cor4, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b12.place(x=0, y=156)
b13 = Button(Frame_corpo, command = lambda: digitar_valores("2"), text="2", width=5, height=2, bg=cor4, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b13.place(x=60, y=156)
b14 = Button(Frame_corpo, command = lambda: digitar_valores("3"), text="3", width=5, height=2, bg=cor4, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b14.place(x=120, y=156)
b15 = Button(Frame_corpo, command = lambda: digitar_valores("+"), text="+", width=5, height=2, bg=cor5, fg=cor2, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b15.place(x=180, y=156)

#Botões = 0, ., =
b16 = Button(Frame_corpo, command = lambda: digitar_valores("0"), text="0", width=11, height=2, bg=cor4, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b16.place(x=0, y=208)
b17 = Button(Frame_corpo, command = lambda: digitar_valores("."), text=".", width=5, height=2, bg=cor4, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b17.place(x=120, y=208)
b18 = Button(Frame_corpo, command = calcular, text="=", width=5, height=2, bg=cor5, fg=cor2, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b18.place(x=180, y=208)

janela.mainloop()