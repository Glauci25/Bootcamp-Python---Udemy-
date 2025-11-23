print('''
                      _ ,====, _    |I|`` ||  `|I `|
                     |`I|    || `==,|``   ^^   ``  |
                     | ``    ^^    ||_,===TT`==,,_ |
                     |,==Y``Y==,,__| \L=_-`'   +J/`
                      \|=_  ' -=#J/..-|=_-     =|
                       |=_   -;-='`. .|=_-     =|----T--,
                       |=/\  -|=_-. . |=_-/^\  =||-|-|::|____
                       |=||  -|=_-. . |=_-| |  =|-|-||::\____
                       |=LJ  -|=_-. . |=_-|_| =||-|-|:::::::
                       |=_   -|=_-_.  |=_-     =|-|-||:::::::
                       |=_   -|=//^\. |=_-     =||-|-|:::::::
                   ,   |/&_,_-|=||  | |=_-     =|-|-||:::::::
                ,--``8%,/    ',%||  | |=_-     =||-|-|%::::::
***************************************************************''')
print('Bem-vindo a Hogwarts! \n Sua missão é encontrar a varinha perdida do Harry Potter. A única dica é: ele perdeu na floresta.')
print('Você deu de cara com duas opções de caminho: direita ou esquerda.')
a = input('Digite (esquerda) para ir à esquerda e (direita) para ir à direita.')
if a == 'esquerda':
    print('Você chegou a um lago. Quer nadar ou esperar?')
    a = input('Escolha (nadar) ou (esperar): ')
    if a == 'esperar':
        print('Você notou que há três portas atrás de você: uma azul, uma amarela e uma vermelha.')
        a = input('Quer entrar na (amarela), (azul) ou (vermelha)?')
        if a == 'amarela':
            print('PARABÉNS, GANHASTE!!')
        elif a == 'vermelha':
            print('Você encontrou com os centauros. Game Over.')
        elif a == 'azul':
            print('Você encontrou Aragogue e seus filhos. Já era!.')
        else:
            print('Game Over.')
    else:
        print('Você foi atacado pelas Sereias! Game Over.')
else:
    print('Que buraco enorme! Deve ser um feitiço dos capangas de Voldemort! Perdeste.')