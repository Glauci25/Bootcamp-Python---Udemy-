from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#printar o report
my_money_machine = MoneyMachine()
cafeteira = CoffeeMaker()
menu = Menu()
ligado = True

#2 - recursos são suficientes?
while ligado:
    opcoes = menu.get_items()
    escolha = input(f'O que você quer pedir? {opcoes}: ')
    if escolha == 'off':
        ligado = False
    elif escolha == 'report':
        cafeteira.report()
        my_money_machine.report()
    else:
        bebida = menu.find_drink(escolha)
        if cafeteira.is_resource_sufficient(bebida):
            if my_money_machine.make_payment(bebida.cost):
                cafeteira.make_coffee(bebida)