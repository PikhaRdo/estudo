#nested classes

class Computador:
    def __init__(self,modelo,gpu_nome,gpu_memoria,cpu_nome,cpu_processadores,cpu_cores,cpu_clock):
        self.modelo=modelo
        self.gpu= self.GPU (gpu_nome,gpu_memoria) #link com a classe GPU
        self.cpu=self.CPU(cpu_nome,cpu_processadores,cpu_cores,cpu_clock)
    def mostrar_config(self):
        print (f'Computador: {self.modelo}')
        self.gpu.mostrar_gpu() #link da def mostrar_gpu
        self.cpu.mostrar_cpu() #link da def mostrar_cpu
    class GPU: #nested
        def __init__(self,nome,memoria):
            self.nome = nome
            self.memoria= memoria
        def mostrar_gpu(self):
            print(f'''GPU: {self.nome} - Memoria:{self.memoria}GBs''')
    class CPU: #nested
        def __init__(self,nome,processadores,cores,clock):
            self.nome = nome
            self.processadores=processadores
            self.cores = cores
            self.clock = clock
        def mostrar_cpu(self):
            print(f'''CPU: {self.nome} - N° processadores: {self.processadores} - N° cores: {self.cores} - Clock Máximo: {self.clock}''')


#utilização

pc1= Computador('Dell', 'Nvidia RTX 3090', 12, 'I5-12100h', 12, 6, '4.1 GHz')

pc1.mostrar_config()
