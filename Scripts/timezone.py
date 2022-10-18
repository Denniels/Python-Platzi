from datetime import datetime
import pytz

santiago_timezone = pytz.timezone('America/Santiago')
santiago_date = datetime.now(santiago_timezone)
print(f'Santiago: {santiago_date.strftime("%d/%m/%Y %H:%M:%S")}')

mexico_timezone = pytz.timezone('America/Mexico_City')
mexico_date = datetime.now(mexico_timezone)
print(f'Mexico: {mexico_date.strftime("%d/%m/%Y %H:%M:%S")}')

colombia_timezone = pytz.timezone('America/Bogota')
colombia_date = datetime.now(colombia_timezone)
print(f'Colombia: {colombia_date.strftime("%d/%m/%Y %H:%M:%S")}')

caracas_timezone = pytz.timezone('America/Caracas')
caracas_date = datetime.now(caracas_timezone)
print(f'Caracas: {caracas_date.strftime("%d/%m/%Y %H:%M:%S")}')