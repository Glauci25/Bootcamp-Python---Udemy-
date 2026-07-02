import tkinter

def calculate():
    mile = entry.get() #essa variável recebe uma string
    km = int(mile)*1.60934 #aqui transforma a string em inteiro e multiplica
    label2.config(text=f"{km}") #muda o textodo label2 para a quilometragem

window = tkinter.Tk() #cria a janela
window.title("Conversor milhas --> quilômetros") #título da janela
window.minsize(width=250, height=150)
window.config(padx=10,pady=10)

espace = tkinter.Label(text=" ") #criei um espaço só para a grid ter uma base
espace.grid(column=0,row=0) #0,0

label1 = tkinter.Label(text="é igual a") #criação do label
label1.grid(column=0, row=1)

entry = tkinter.Entry(width=10)
entry.grid(column=1, row=0)

label2 = tkinter.Label(text="0")
label2.grid(column=1, row=1)

label3 = tkinter.Label(text="Milhas")
label3.grid(column=2, row=0)

label4 = tkinter.Label(text="Km")
label4.grid(column=2, row=1)

button = tkinter.Button(text="calcular", command=calculate) #chama a função
button.grid(column=1,row=2)

window.mainloop()