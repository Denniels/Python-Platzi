menu = '''
Bienvenido al conversor de monedas 💵

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Chilenos
4 - Pesos Mexicanos

Escoje una opcion
'''
opcion = int(input(menu))

def conversor_dolar(peso_pais, dolar):
        return peso_pais / dolar
# Peso Colombiano a dolar
if opcion == 1:
        pesos_colombianos = int(input('Cuantos pesos Colombianos tienes?: '))
        print(f'Tienes {conversor_dolar(pesos_colombianos, 0.00022)} dolares')

# Peso Argentino a dolar
if opcion == 2:
        pesos_argentinos = int(input('Cuantos pesos Argentinos tienes?: '))
        print(f'Tienes {conversor_dolar(pesos_argentinos, 0.0067)} dolares')

# Peso Chileno a dolar
if opcion == 3:
        pesos_chilenos = int(input('Cuantos pesos Chilenos tienes?: '))
        print(f'Tienes {round(conversor_dolar(pesos_chilenos, 938.18), 2)} dolares')

# Peso Mexicano a dolar
if opcion == 4:
        pesos_mexicanos = int(input('Cuantos pesos Mexicanos tienes?: '))
        print(f'Tienes {conversor_dolar(pesos_mexicanos, 0.050)} dolares')