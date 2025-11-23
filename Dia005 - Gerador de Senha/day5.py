import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D','E','F','G', 'H','I', 'J', 'K','L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0','1','2','3','4','5','6','7','8','9']
simbolos = ['!', '@', '#', '$', '%', '&', '*', '(', ')']

print("Bem-vindo ao gerador de senha!")
qnt_letras = int(input('Quantas letras na senha: '))
qnt_numeros = int(input("Quantos números na senha: "))
qnt_simbolos = int(input('Quantos símbolos na senha: '))

letras_senha = random.sample(letras, qnt_letras) #retorna uma lista de x letras
numeros_senha = random.sample(numeros, qnt_numeros) #retorna uma lista de x numeros
simbolos_senha = random.sample(simbolos, qnt_simbolos) #retorna uma lista x de símbolos
lista_senha = letras_senha + numeros_senha+ simbolos_senha #lista concatenada

random.shuffle(lista_senha) #embaralhando os elementos da lista
lista_senha = ''.join(lista_senha)
print(f'Sua senha é: {lista_senha}')
