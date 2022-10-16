nombre = input('¿Cual es tu nombre?: ')
print(f'''
        {nombre}
        {nombre.upper()}
        {nombre.lower()}
        {nombre.capitalize()}''')

nombre1 = nombre.capitalize()
print(nombre1)
nombre2 = nombre1.replace('e', 'a')

print(nombre2)
print(nombre2[2])
print(len(nombre2))