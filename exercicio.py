from tkinter import *
from tkinter import messagebox

def imc():
    peso = float(txtPeso.get())
    altura = float(txtAltura.get())
    imc=peso/altura**2
    messagebox.showinfo("Seu IMC",f"Seu IMC é: {imc:1f}")





janela = Tk()

janela.geometry("400x300+800+300")
janela.title("Dados para o IMC")

labelTopo= Label(janela, text="Vamos Calcular seu IMC", font="Calibri 16")
labelTopo.grid(row=0, column=1)


labelPeso= Label(janela, text="Digite seu peso", font="Calibri 16")
labelPeso.grid(row=1, column=0, stick=W)
txtPeso = Entry(janela, font="Calibri 16")
txtPeso.grid(row=1, column=1)

labelAltura= Label(janela, text="Digite sua altura", font="Calibri 16")
labelAltura.grid(row=2,column=0, stick=W)
txtAltura = Entry(janela, font="Calibri 16")
txtAltura.grid(row=2 , column=1)

botaoCalcular= Button(janela, text="Calcular IMC", width=12, bg= "black", fg="orange",command=imc)
botaoCalcular.grid(row=3, column=1)



janela.mainloop()