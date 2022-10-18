from car import Car

if __name__ == '__main__':
        print('Listado de cars')
        car = Car()
        car.license = 'BZZZ-74'
        car.driver = 'Andres Herrera'
        print(vars(car))

        car2 = Car()
        car2.license = 'GTZZ-74'
        car2.driver = 'Andrea Herrera'
        print(vars(car2))