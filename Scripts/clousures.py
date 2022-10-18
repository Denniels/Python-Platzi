# Hola -> HolaHolaHola

def make_repeter_of(n):
        def repeter(string):
                assert type(string) == str, 'Solo puedes utilizar cadenas'
                return string * n
        return repeter

def run():
        repeat_5 = make_repeter_of(5)
        print(repeat_5('Integral'))
        repeat_10 = make_repeter_of(10)
        print(repeat_10('Service'))

if __name__ == '__main__':
        run()