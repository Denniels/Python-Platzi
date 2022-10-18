class Main {
        Run | Debug
        public static void main(String[] args){
                System.out.println('Hola Mundo')
                Car car = new Car();
                car.licence = 'BZZZ-74';
                car.driver = 'Jorgue Curioso'
                car.passeger = 4
                car.printDataCar();

                Car car2 = bew Car();
                car2.licence = 'GTZZ74';
                car2.driver = 'Andrea Herrera';
                car2.passeger = 3;
                System.out.println('Car licenses: ' + car2.licence)
        }
}