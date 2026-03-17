from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Gerenciador de Senhas")
window.config(padx=20, pady=20)

img = PhotoImage(file="/Users/estagiario.inovacao/Desktop/mundo da glau/python/password-manager-start/logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

#label website
label1 = Label(text="Site:")
label1.grid(column=0, row=1)
entry1 = Entry(width=35)
entry1.grid(column=1, row=1, columnspan=2)

#label email/username
label2 = Label(text= "Email ou Usuário:")
label2.grid(column=0, row=2)
entry2 = Entry(width=35)
entry2.grid(column=1, row=2)

#label password
label3 = Label(text="Senha:")
label3.grid(column=0, row=3)
entry3 = Entry(width=21)
entry3.grid(column=1, row=3)

#buttons
button1 = Button(text="Gerar Senha")
button1.grid(column=2, row=3)

button2 = Button(text="Adicionar")
button2.grid(column=1, row= 4)

window.mainloop()