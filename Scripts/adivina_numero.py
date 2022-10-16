import random

def run():
        numero_aleatorio = random.randint(1, 100)
        numero_elejido = int(input('Ingresa un numero entre el 1 y el 100: '))
        while numero_elejido != numero_aleatorio:
                if numero_elejido < numero_aleatorio:
                        print('Busca un numero mas grande')
                else:
                        print('Busca un numero mas pequeño')
                numero = int(input('Ingresa otro numero: '))
        print('!Ganaste¡')

if __name__ == '__main__':
        run()