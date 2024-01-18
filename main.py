from tkinter import *
from tkinter import messagebox

def clicou() -> None:
    messagebox.showinfo("Clicou","Você clicou no botão!" )
    nome=txtNome.get()
    salario=float(txtSalario.get())
    messagebox.showinfo("Clicou!", f"Seu nome: {nome} \n Seu salário:{salario}")

janela = Tk()

janela.geometry("400x300+800+300")
janela.title("Minha Janela")

labelNome = Label(janela, text="Nome", font= "Calibri 16", fg="navy")
#labelNome.pack()
#labelNome.place(x=150, y=120)
labelNome.grid(row=0, column=0,sticky=W)
txtNome = Entry(janela, font="Calibri 16")
txtNome.grid(row=0, column=1)

labelSalario = Label(janela, text="Salário", font= "Calibri 16", fg="navy")
labelSalario.grid(row=2, column=0)
txtSalario = Entry(janela, font="Calibri 16")
txtSalario.grid(row=2, column=1)

btnEnviar= Button(janela, text="Enviar", font= "Calibri 16", width=10, bg="orange", fg="black", command=clicou)
btnEnviar.grid(row=3, column=1 )



janela.mainloop()
