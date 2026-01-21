import turtle
import pandas

screen = turtle.Screen()
screen.title("Jogo: Estados do Brasil")
image = "mapa-brasil.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("brazil-estates.csv")
lista_estados = data["state"].to_list()
print(lista_estados)
lista_xcor = data["x"].to_list()
lista_ycor = data["y"].to_list()

lista_x_exit = []
lista_y_exit = []


score = 0
cont = 0
while len(lista_estados) > 0:
    cont += 1
    answer_state = screen.textinput(title=f"Pontuação: {score}/27", prompt="Qual é o nome do estado?")
    answer_state = answer_state.title()

    print(lista_estados)
    if answer_state in lista_estados:
        indice = lista_estados.index(answer_state)
        score += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        x_cor = lista_xcor[indice]
        y_cor = lista_ycor[indice]

        t.goto(x_cor, y_cor)
        t.write(f"{answer_state.upper()}", align="center", font=("Arial", 8, "bold"))
        lista_estados.pop(indice)
        lista_xcor.pop(indice)
        lista_ycor.pop(indice)

    if answer_state.lower() == "exit":
        for i in range(len(lista_estados)):
            a = turtle.Turtle()
            a.hideturtle()
            a.penup()

            x = lista_xcor[i]
            y = lista_ycor[i]

            a.goto(x, y)
            a.write(lista_estados[i].upper(), align="center", font=("Arial", 8, "bold"))
        break

screen.exitonclick()
