import random

print('''$$\   $$\ $$\           $$\                           
$$ |  $$ |\__|          $$ |                          
$$ |  $$ |$$\  $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  
$$$$$$$$ |$$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$  __$$ |$$ |$$ /  $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |      
$$ |  $$ |$$ |\$$$$$$$ |$$ |  $$ |\$$$$$$$\ $$ |      
\__|  \__|\__| \____$$ |\__|  \__| \_______|\__|      
              $$\   $$ |                              
              \$$$$$$  |                              
               \______/                               
$$\                                                   
$$ |                                                  
$$ |      $$$$$$\  $$\  $$\  $$\  $$$$$$\   $$$$$$\   
$$ |     $$  __$$\ $$ | $$ | $$ |$$  __$$\ $$  __$$\  
$$ |     $$ /  $$ |$$ | $$ | $$ |$$$$$$$$ |$$ |  \__| 
$$ |     $$ |  $$ |$$ | $$ | $$ |$$   ____|$$ |       
$$$$$$$$\\$$$$$$  |\$$$$$\$$$$  |\$$$$$$$\ $$ |       
\________|\______/  \_____\____/  \_______|\__|''')

pessoas = [{
    'nome': 'Neymar',
    'descrição': 'jogador de futebol brasileiro.',
    'seguidores': 231000000
    },

    {
        'nome': 'Zendaya',
        'descrição': 'atriz e cantora, conhecida por seu papel como Michelle Jones em Homem-Aranha.',
        'seguidores': 177000000
    },

    {
        'nome': 'Ronaldinho Gaúcho',
        'descrição': 'jogador de futebol brasileiro',
        'seguidores': 77700000
    },

    {
        'nome': 'Nike',
        'descrição': 'marca de roupas e sapatos',
        'seguidores': 299000000
    },

    {
        'nome': 'Katseye',
        'descrição': 'grupo feminino de pop',
        'seguidores': 6800000
    },

    {
        'nome': 'São Paulo FC',
        'descrição': 'maior time de futebol do Brasil',
        'seguidores': 7000000
    },

    {
        'nome': 'Will Smith',
        'descrição': 'ator estadunidense',
        'seguidores': 69500000
    },

    {
        'nome': 'Rayssa Leal',
        'descrição': 'skatista olímpica brasileira',
        'seguidores': 8400000
    },

    {
        'nome': 'Virginia',
        'descrição': 'blogueira empreendedora brasileira',
        'seguidores': 52500000
    },

    {
        'nome': 'Rodaldinho Gaúcho',
        'descrição': 'jogador de futebol brasileiro',
        'seguidores': 77700000
    },

    {
        'nome': 'Michael B Jordan',
        'descrição': 'ator estadunidense',
        'seguidores': 77700000
    },

    {
    'nome': 'Anitta',
    'descrição': 'cantora e empresária brasileira',
    'seguidores': 66500000
    },

    {
    'nome': 'Cristiano Ronaldo',
    'descrição': 'jogador de futebol português',
    'seguidores': 620000000
    },

    {
    'nome': 'Beyoncé',
    'descrição': 'cantora e atriz norte-americana',
    'seguidores': 320000000
    },

    {
    'nome': 'Whindersson Nunes',
    'descrição': 'comediante e influenciador brasileiro',
    'seguidores': 59000000
    },

    {
    'nome': 'Lionel Messi',
    'descrição': 'jogador de futebol argentino',
    'seguidores': 500000000
    },

    {
    'nome': 'Selena Gomez',
    'descrição': 'cantora e atriz norte-americana',
    'seguidores': 430000000
    },

    {
    'nome': 'Taylor Swift',
    'descrição': 'cantora e compositora norte-americana',
    'seguidores': 300000000
    },

    {
    'nome': 'Kylian Mbappé',
    'descrição': 'jogador de futebol francês',
    'seguidores': 120000000
    },

    {
    'nome': 'Ivete Sangalo',
    'descrição': 'cantora brasileira',
    'seguidores': 37000000
    },

    {
    'nome': 'Aidan Gallagher',
    'descrição': 'ator norte-americano',
    'seguidores': 10000000
    },

    {
    'nome': 'Virat Kohli',
    'descrição': 'jogador de críquete indiano',
    'seguidores': 270000000
    }
]
pontuacao = 0
right = True
a_b = random.sample(range(22), 2)
a = a_b[0]
b = a_b[1]
while right == True:
    print(f'Pontuação atual: {pontuacao}.')
    print(f"Compare A: {pessoas[a]['nome']}, {pessoas[a]['descrição']}.")
    print('''$$\    $$\           
    $$ |   $$ |          
    $$ |   $$ | $$$$$$$\ 
    \$$\  $$  |$$  _____|
     \$$\$$  / \$$$$$$\  
      \$$$  /   \____$$\ 
       \$  /   $$$$$$$  |
        \_/    \_______/ 
                         ''')
    print(f"Contra B: {pessoas[b]['nome']}, {pessoas[b]['descrição']}.")
    resp = input('Quem você acha que tem mais seguidores? (A/B): ').lower()
    if resp == 'a' and pessoas[a]['seguidores'] > pessoas[b]['seguidores']:
        right = True
        a = a
        b = random.randint(1,22)
        pontuacao += 1
    elif resp == 'b' and pessoas[b]['seguidores'] > pessoas[a]['seguidores']:
        right = True
        a = b
        b = random.randint(0,21)
        pontuacao += 1
        while b == a:
                b = random.randrange(len(pessoas))
    else:
        print('Você perdeu!')
        print(f'Pontuação final: {pontuacao}.')
        right = False
