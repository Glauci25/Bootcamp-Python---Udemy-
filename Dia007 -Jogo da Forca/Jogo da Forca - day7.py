#'''STEP 1'''
#todo1: randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
#todo2: ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#todo3: check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print('Right' if it is, 'wrong' if it's not.)
'''
from random import choice
lista_palavras = ['manteiga', 'caldo', 'leite', 'carne', 'mingau']
palavra_escolhida = choice(lista_palavras)
print(f'{palavra_escolhida}')

letra_user = input('Escolha uma letra: ')
for letra in palavra_escolhida:
    if letra == letra_user:
        print('Certo')
    else:
        print('Errado')
'''
'''STEP 2'''
#todo1: create an empty string called placeholder. for each letter in the chosen_word add a _ to placeholder.
#todo2: create an empty string called "display". loop through each letter in the chosen_word. if the letter at that position matches guess, then reveal that letter in the display at that position.
'''
from random import choice
lista_palavras = ['manteiga', 'caldo', 'leite', 'carne', 'mingau']
palavra_escolhida = choice(lista_palavras)
print(f'{palavra_escolhida}')
letra_user = input('Escolha uma letra: ').lower()
placeholder = ''
for letra in range(len(palavra_escolhida)):
    placeholder += '_'

display = ''
for letra in palavra_escolhida:
    if letra == letra_user:
        display += letra
    else:
        display += '_'
print(display)
'''

'''STEP 3'''
'''
from random import choice
lista_palavras = ['manteiga', 'caldo', 'leite', 'carne', 'mingau']
palavra_escolhida = choice(lista_palavras)
print(f'{palavra_escolhida}')
placeholder = ''
for letra in range(len(palavra_escolhida)):
    placeholder += '_'
print(placeholder)
letra_user = input('Escolha uma letra: ').lower()

display = ''
while letra_user in palavra_escolhida or display == '':
    display_temp = '' #display temporário
    for letra in palavra_escolhida: #a cada letra na palavra escolhida, faça:
        if letra == letra_user: #se a letra da palavra for igual a letra que o usuário digitou
            display_temp += letra #o display temporário vai adicionar a letra ao seu conteúdo
        elif letra in display: #se essa mesma letra estiver no display original, faça:
            display_temp += letra #adiciona a letra ao display temporário
        else: #caso contrário:
            display_temp += '_' #adicione underline no display temporário
    display = display_temp #iguala o display temporário ao display antes que o temporário seja reiniciado
    print(display)
    letra_user = input('Escolha uma letra: ').lower()
'''

'''STEP 4'''
from random import choice
animais = ["cachorro","gato","elefante","leão","tigre","girafa","zebra","macaco","urso","lobo","raposa","cavalo","vaca","ovelha","cabra","coelho","panda","canguru","golfinho","tartaruga","jacaré","águia","pato","galinha","pinguim"]
estagios = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
palavra_escolhida = choice(animais)
display = '_'*len(palavra_escolhida)
print(estagios[0])
print(display)
hangman = 0

while hangman <= 6 and '_' in display:
    letra_usuario = input('Digite a letra: ').lower()
    display_temp = '' #display temporário

    if letra_usuario not in palavra_escolhida:
        hangman += 1
        if hangman < len(estagios):
            print(estagios[hangman])

    for letra in palavra_escolhida: #a cada letra napalavra escolhida, faça:
        if letra == letra_usuario: #se a letra da palavra for igual a letra que o usuário digitou
            display_temp += letra #o display temporário vai adicionar a letra ao seu conteúdo
        elif letra in display: #se essa mesma letra estiver no display original, faça:
            display_temp += letra #adiciona a letra aodisplay temporário
        else: #caso contrário:
            display_temp += '_' #adicione underline nodisplay temporário

    display = display_temp #iguala o display temporário ao display antes que o temporário seja reiniciado
    print(display)

if '_' not in display:
    print('Parabéns! Você venceu!')
else:
    print(f'Você perdeu! A palavra era {palavra_escolhida}.')
