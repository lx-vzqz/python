#PRIMERA PARTE
def suma3(valor1, valor2, valor3):
    return valor1+valor2+valor3

a = suma3(1,2,3)
print(a)

#SEGUNDA PARTE
class coche:
    def __init__(self, puertas):
        self.puertas = puertas
    def sumar_puerta(self, puertas):
        self.puertas = self.puertas + puertas

miCoche = coche(3)
print(miCoche.puertas)

miCoche.sumar_puerta(1)
print(miCoche.puertas)

