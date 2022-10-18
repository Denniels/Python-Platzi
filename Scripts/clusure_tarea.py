def make_division(n):
        def repeter(integer):
                return integer / n
        return repeter

def run():
        division_by_3 = make_division(3)
        print(division_by_3(18))# resultado esperado 6

        division_by_5 = make_division(5) 
        print(division_by_5(100))# resultado esperado 20

        division_by_18 = make_division(18)
        print(division_by_18(54))# resultado esperado 3

if __name__ == '__main__':
        run()