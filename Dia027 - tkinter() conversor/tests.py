import tkinter
'''
window = tkinter.Tk() #cria o objeto
window.title("Meu primeiro Programa GUI") #define o título
window.minsize(width=500, height=300) #define um tamanho mínimo para a janela

#Criando o label
my_label = tkinter.Label(text="I am a Label.", font=("Arial", 24, "bold"))
my_label.pack() #coloca o label em algum lugar na GUI

my_label["text"] = "New Text"
my_label.config(text="New Text")

def button_clicked():
    print("I got clicked.")
    my_label.config(text="Button had been clicked.")

button = tkinter.Button(text = "Click me", command = button_clicked)
button.pack()

#input
put = tkinter.Entry(width=10)
put.pack()
print(put.get())

def change_title():
    my_label.config(text=put.get())

button2 = tkinter.Button(text="change title", command=change_title)
window.mainloop()
'''
window2 = tkinter.Tk()
window2.title("Meu primeiro Programa GUI") #define o título
window2.minsize(width=500, height=300) #define um tamanho mínimo para a janela
window2.config(padx=10,pady=10) #add padding

label = tkinter.Label(text="Hello World!", font=("Arial", 24, "bold"))
label.config(text="Hello")
label.grid(column=0, row=0)

button = tkinter.Button(text="botão")
button.grid(column=1, row=1)

new_button = tkinter.Button(text="novo botão")
new_button.grid(column=2, row=0)

entry = tkinter.Entry(width=10)
entry.grid(column=3, row= 2)

window2.mainloop()






