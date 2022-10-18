from datetime import datetime

datetime = datetime.now()
print(datetime)

str = datetime.strftime('%d/%m/%Y')
str_uno = datetime.strftime('%m/%d/%Y')
str_dos = datetime.strftime('Estamos en el año %Y')

print(f'''Formato de fechas
Formato de LATAM: {str}
Formato de USA: {str_uno}
Formato Random: {str_dos}''')