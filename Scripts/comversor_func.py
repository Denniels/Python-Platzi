def conversor(tipo_peso, valor_dolar):
        pesos = float(input(f'¿Cuantos pesos {tipo_peso} tienes?: '))
        dolares = round(pesos / valor_dolar, 2)
        print(f'Tienes $ {dolares} dolares')

menu = '''
Bienvenido al conversor de monedas 💵

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Escoje una opcion
'''
opcion = int(input(menu))

# Peso Colombiano a dolar
if opcion == 1:
        conversor('colombianos', 3875)

# Peso Argentino a dolar
elif opcion == 2:
        conversor('argentinos', 65)

# Peso Mexicano a dolar
elif opcion == 3:
        conversor('Mexicanos', 24)

else:
        print('Opcion incorrecta, por favor escoje una opcion valida')