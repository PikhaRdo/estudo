
#classes
class Motor:
    def __init__(self,marca,potencia):
        self.marca = marca
        self.potencia = potencia
        pass

class Carro:
    def __init__(self):
        self.motores = []
    def adic_motor(self, motor):
        self.motores.append(motor)
    def listar_motores(self):
        for motor in self.motores:
            print(f"{motor.marca} - {motor.potencia}")


#criação dos objetos
motor_v6 = Motor('ford', 300)
motor_v8 = Motor('Ferrari', 600)
motor_v12= Motor('Lmaborghini', 950)
#criação do carro e adicionando o motor a ele
carro = Carro()
carro.adic_motor(motor_v6)
carro.adic_motor(motor_v8)
carro.adic_motor(motor_v12)
#listagem dos motores
carro.listar_motores()