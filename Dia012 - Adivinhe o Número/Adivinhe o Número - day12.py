print("""                                                                                                                                        
  _  _            _                ___                _              ___                
 | \| |_  _ _ __ | |__  ___ _ _   / __|_  _ ___ _____(_)_ _  __ _   / __|__ _ _ __  ___ 
 | .` | || | '  \| '_ \/ -_) '_| | (_ | || / -_|_-<_-< | ' \/ _` | | (_ / _` | '  \/ -_)
 |_|\_|\_,_|_|_|_|_.__/\___|_|    \___|\_,_\___/__/__/_|_||_\__, |  \___\__,_|_|_|_\___|
                                                            |___/                       
""")
import random
numero = random.randint(1,101)
print("I'm thinking of a number between 1 and 100.")
difficulty = input('Type a difficulty (easy) or (hard): ').lower()
tentativas = 10 if difficulty == 'easy' else 5 if difficulty == 'hard' else 0

if tentativas == 0:
    print('Você digitou algo errado.')
else:
    while tentativas > 0:
        print(f'Você tem {tentativas} tentaivas sobrando.')
        user_guess = int(input('Dê um palpite: '))
        if user_guess > numero:
            print('Menos.')
        elif user_guess < numero:
            print('Mais.')
        else:
            print('Você ganhou!')
            break
        tentativas -= 1
    else:
        print(f'Você perdeu! O número era {numero}.')