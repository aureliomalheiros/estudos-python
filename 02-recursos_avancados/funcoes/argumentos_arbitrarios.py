def fazer_pizza(*sabores):
    print('\nSabores da pizza: ')
    for sabor in sabores:
        print('- ' + sabor)

fazer_pizza('peperoni')
fazer_pizza('Mussarela', 'Calabresa', 'Portuguesa', '4 Queijos')