menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0
}

def report():
    #mostra os recursos e suas quantidades na máquina
    print(f"Água: {resources['water']}ml")
    print(f"Leite: {resources['milk']}ml")
    print(f"Café: {resources['coffee']}g")
    print(f"Dinheiro: ${resources['money']:.2f}")

def check_resources(beb):
    if resources['water'] < beb['ingredients']['water']:
        print('Sentimos muito. Não há água suficiente.')
        return False
    elif resources['milk'] < beb['ingredients']['milk']:
        print('Sentimos muito. Não há leite suficiente.')
        return False
    elif resources['coffee'] < beb['ingredients']['coffee']:
        print('Sentimos muito. Não há café suficiente.')
        return False
    else:
        print(f"A bebida que escolheste vale ${beb['cost']}")
        return True

print('''           (
                          )     (
                   ___...(-------)-....___
               .-""       )    (          ""-.
         .-'``'|-._             )         _.-|
        /  .--.|   `""---...........---""`   |
       /  /    |                             |
       |  |    |                             |
        \  \   |                             |
         `\ `\ |                             |
           `\ `|                             |
           _/ /\                             /
          (__/  \                           /
       _..---""` \                         /`""---.._
    .-'           \                       /          '-.
   :               `-.__             __.-'              :
   :                  ) ""---...---"" (                 :
    '._               `"--...___...--"`              _.'
  jgs \""--..__                              __..--""/
       '._     """----.....______.....----"""     _.'
          `""--..,,_____            _____,,..--""`
                        `"""----"""`''')

fazer = ''
while fazer != 'off': #enquanto ninguém desligar a máquina
    fazer = input('O que você gostaria de fazer? (espresso/latte/cappuccino): ').lower() #pedido do cliente
    if fazer == 'report': # alguém sresponsável pela manutenção pode verificar o conteúdo na máquina
        report()
    elif fazer == 'off':
        print('Desligando...')
        break
    else:
        bebida = menu[fazer]
        if check_resources(bebida) == True:
            print('Hora de inserir as moedas.')
            quarters = int(input('Quantas quarters?: ')) #quarters= $0.25
            dimes = int(input('Quantas dimes?: ')) #dimes= $0.10
            nickles = int(input('Quantas nickles?: ')) #nickles= $0.05
            pennies = int(input('Quantas pennies?: ')) #pennies= $0.01
            total = 0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies
            if total < bebida['cost']:
                print('Sinto muito, você não inseriu dinheiro suficiente. Dinheiro devolvido')
            else:
                troco = total - bebida['cost']
                print(f'Troco devolvido: ${troco:.2f}')
                water = resources['water'] - bebida['ingredients']['water']
                milk = resources['milk'] - bebida['ingredients']['milk']
                coffee = resources['coffee'] - bebida['ingredients']['coffee']
                money = resources['money'] + bebida['cost']

                resources = {
                    'water': water,
                    'milk': milk,
                    'coffee': coffee,
                    'money': money
                }
                print('Aqui está seu café. Aproveite e volte sempre.')



