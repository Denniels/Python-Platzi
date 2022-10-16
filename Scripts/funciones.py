'''def imprimir_mensaje():
        print('Mensaje especial: ')
        print('Estoy aprendiendo a usar funciones')'''

def conversacion(mensaje):
        '''
        Docstring
        '''
        print(f'''
                Hola
                Como estas
                {mensaje}
                Adios''')

opcion = int(input('Elije una opcion (1, 2, 3): '))

if opcion == 1:
        conversacion('Elejiste la opcion 1')
elif opcion == 2:
        conversacion('Elejiste la opcion 2')
elif opcion == 3:
        conversacion('Elejiste la opcion 3')
else:
        print('Escribe una opcion correcta')