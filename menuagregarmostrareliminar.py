
from math import floor



class opciones:
    choise = ""



    def __init__(self) -> None:
        self.opciones()

    def opciones(self):
        print('------------------------------------------')
        print('------------------------------------------')
        print('------------------------------------------')
        print('1: mostrar empleados')
        print('')
        print('')
        print('2: añadir empleado')
        print('')
        print('')
        print('3: suprimir  empleado de la base de datos')
        print('')
        print('')
        print('4: salir')
        print('------------------------------------------')
        print('------------------------------------------')
        print('------------------------------------------')

    
        
        self.choise = input('por favor seleccione una opcion : ')



    def main(self):
        while True:
            if self.choise == '1':
                self.verLista()
            elif self.choise == "2":
                self.añadirempleado()
            elif self.choise == "3":
                self.suprimiremp()
            elif self.choise == "4":
                break
            print("")
            print("")
            input('Presione enter para continuar:')
            self.opciones()






class Main(opciones):



    def __init__(self) -> None:
        super().__init__()



        self.__lista = []
        self.__subsidioTransporte = 60000
        self.__subsidioAlimentacion = 80000
        self.__fondovejez = 0.04
        self.__salud = 0.033751

        self.__total = 0

        self.main()



    def verLista(self):
        if self.__lista == []:


            print ("no hay datos almacenados aun ")


        else: 
            
            [print(f"Posicion[{p}]: {x}") for (p, x) in enumerate(self.__lista)]




    def añadirempleado(self):
        sal = float(input('digite salario:'))

        datosTrabajador = {
            'Nombre': input('Digite nombre:'),

            'Edad': int(input('Digite edad:')),

            'Salario': sal,

            "Devengado": self._deveng(sal),

            'Deduciones': self._deduc(sal),

            'SalarioFinal': self._salarioNeto(sal)
        }

        self.__lista.append(datosTrabajador)
        print('Empleado añadido de manera exitosa.')



    def suprimiremp(self):

        empleado = input('digite Nombre de empleado a suprimir: ')
        for elemento in self.__lista:

            if elemento['Nombre'] == empleado:

                self.__lista.remove(elemento)
                print("")
                print('El empleado suprimido de  manera exitosa.')
            else:
                print('datos no coindiden ,reingrese nombre.')



    def _deveng(self,salario) -> float:
        if salario < 2000000:
            return (self.__subsidioAlimentacion + self.__subsidioTransporte)
        else:
            return 0                      


    def _deduc(self,salario):
        
        pen = salario * self.__fondovejez
        costosalud = salario * self.__salud
        seguridadsocial = pen + costosalud
        
        return seguridadsocial
               

    def _salarioNeto(self,salario):
       deducciones = self._deduc(salario)
       devengado = self._deveng(salario)



       return salario + devengado - deducciones


if __name__ == "__main__":
    Main()