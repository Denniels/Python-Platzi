'''def run():
        for contador in range(1000):
                if contador % 2 != 0:
                        continue
                print(contador)'''

'''def run():
        for i in range(10000):
                print(i)
                if i == 5687:
                        break'''

def run():
        texto = input('Esscribe un texto: ')
        for letras in texto:
                if letras == 'o':
                        break
                print(letras)

if __name__ == '__main__':
        run()