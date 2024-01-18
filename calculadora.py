from tkinter import *

def limparDisplay()->None:
    display.delete(0,END)

def inserir(valor:str) ->None:
    display.insert(END,valor)

def calcularResultado() -> None:
    textoDisplay = display.get()
    resultado = eval(textoDisplay)
    limparDisplay()
    inserir(resultado)

janela = Tk()
janela.title("Calculadora")

display = Entry(janela, bg="black",font="Calibri 24", width=19, fg="white")
display.pack()

frame = Frame(janela)
frame.pack()

gray = "#333333"
orange = "#ff9500"

btn0 = Button(frame, text="0", bg=gray, fg="white", font="Calibri 16 bold",
              height=2, width=6,command=lambda :inserir('0'))
btn1 = Button(frame, text="1", bg=gray, fg="white", font="Calibri 16 bold",
              height=2, width=6,command=lambda :inserir('1'))
btn2 = Button(frame, text="2", bg=gray, fg="white", font="Calibri 16 bold",
              height=2, width=6,command=lambda :inserir('2'))
btn3 = Button(frame, text="3", bg=gray, fg="white", font="Calibri 16 bold",
              height=2, width=6,command=lambda :inserir('3'))
btn4 = Button(frame, text="4", bg=gray, fg="white", font="Calibri 16 bold",
              height=2, width=6,command=lambda :inserir('4'))
btn5 = Button(frame, text="5", bg=gray, fg="white", font="Calibri 16 bold",
              height=2, width=6,command=lambda :inserir('5'))
btn6 = Button(frame, text="6", bg=gray, fg="white", font="Calibri 16 bold",
              height=2, width=6,command=lambda :inserir('6'))
btn7 = Button(frame, text="7", bg=gray, fg="white", font="Calibri 16 bold",
              height=2, width=6,command=lambda :inserir('7'))
btn8 = Button(frame, text="8", bg=gray, fg="white", font="Calibri 16 bold",
              height=2, width=6,command=lambda :inserir('8'))
btn9 = Button(frame, text="9", bg=gray, fg="white", font="Calibri 16 bold",
              height=2, width=6,command=lambda :inserir('9'))

btnMais = Button(frame, text="+", bg=orange, fg="white", font="Calibri 16 bold",
                 height=2, width=6,command=lambda :inserir('+'))
btnMenos = Button(frame, text="-", bg=orange, fg="white", font="Calibri 16 bold",
                  height=2, width=6,command=lambda :inserir('-'))
btnMulti = Button(frame, text="x", bg=orange, fg="white", font="Calibri 16 bold",
                  height=2, width=6,command=lambda :inserir('*'))
btnDiv = Button(frame, text="/", bg=orange, fg="white", font="Calibri 16 bold",
                height=2, width=6,command=lambda :inserir('/'))

btnIgual = Button(frame, text="=", bg=orange, fg="white", font="Calibri 16 bold",
                  height=2, width=6, command=calcularResultado)
btnZerar = Button(frame, text="CE", bg=orange, fg="white", font="Calibri 16 bold",
                  height=2, width=6, command=limparDisplay)

btn7.grid(row=0, column=0)
btn8.grid(row=0, column=1)
btn9.grid(row=0, column=2)
btnMulti.grid(row=0, column=3)

btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)
btnMenos.grid(row=1, column=3)

btn1.grid(row=2, column=0)
btn2.grid(row=2, column=1)
btn3.grid(row=2, column=2)
btnMais.grid(row=2, column=3)

btnZerar.grid(row=3, column=0)
btn0.grid(row=3, column=1)
btnIgual.grid(row=3, column=2)
btnDiv.grid(row=3, column=3)















janela.mainloop()