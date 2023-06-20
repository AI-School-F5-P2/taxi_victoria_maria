import time

class Cronometro:
    def __init__(self):
        self.inicio = 0
        self.tiempo_pausado = 0
        self.tiempo_transcurrido = 0
        self.en_ejecucion = False
        #es una booleana que indica si el crono esta en ejecución o no. Se inicia en 0 porque está parado.

    def empezar(self):
        if not self.en_ejecucion:
            self.inicio = time.time() - self.tiempo_pausado
            self.en_ejecucion = True
            print("Cronómetro empezado.")

    def parar(self):
        if self.en_ejecucion:
            self.tiempo_pausado = time.time() - self.inicio
            print("El cronómetro sigue en marcha.")

    def reanudar(self):
        if not self.en_ejecucion:
            self.inicio = time.time() - self.tiempo_pausado
            self.en_ejecucion = True
            print("Cronómetro continúa.")

    def finalizar(self):
        if self.en_ejecucion:
            self.tiempo_transcurrido = time.time() - self.inicio
            self.en_ejecucion = False
            print("Cronómetro finalizado.")
        print(f"Tiempo total transcurrido: {self.tiempo_transcurrido} segundos.")

class Taxi:
    def __init__(self):
        self.cronometro = Cronometro()
        self.estado = "parado"

    def empezar(self):
        if self.estado == "parado":
            self.cronometro.empezar()
            self.estado = "en marcha"
            print("El taxi está en marcha.")

    def parar(self):
        if self.estado == "en marcha":
            self.cronometro.parar()
            self.estado = "parado"
            print("El taxi está parado.")

    def reanudar(self):
        if self.estado == "parado":
            self.cronometro.reanudar()
            self.estado = "en marcha"
            print("El taxi ha sido reanudado.")

    def finalizar(self):
        self.cronometro.finalizar()
        self.estado = "finalizado"
        print("El taxi ha finalizado su servicio.")


taxi = Taxi()

while True:
    comando = input("Introduce un comando (empezar, parar, reanudar, finalizar): ")

    if comando == "empezar":
        taxi.empezar()
    elif comando == "parar":
        taxi.parar()
    elif comando == "reanudar":
        taxi.reanudar()
    elif comando == "finalizar":
        taxi.finalizar()
        break
    else:
        print("Comando inválido.")
