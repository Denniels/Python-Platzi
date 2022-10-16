def run():
        mi_diccionario = {
                'llave_1':1,
                'llave_2':2,
                'llave_3':3
        }
#        print(f'''
#        {mi_diccionario['llave_1']}
#        {mi_diccionario['llave_2']}
#        {mi_diccionario['llave_3']}''')
        poblacion_paises = {
                'Argentina': 44938712,
                'Brazil':210147125,
                'Colombia':50372424
        }
#        print(poblacion_paises['Argentina'])

#        for pais in poblacion_paises.keys():
#                print(pais)
#        for pais in poblacion_paises.values():
#                print(pais)

        for pais, poblacion in poblacion_paises.items():
                print(f'{pais} tiene {poblacion} habitantes')

if __name__ == '__main__':
        run()