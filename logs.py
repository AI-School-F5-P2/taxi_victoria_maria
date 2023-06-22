'''
LOGGING:

Rastrea los eventos que ocurren cuando se ejecuta algún software. 
Las funciones de registro se denominan según el nivel o la gravedad de los eventos que se utilizan para rastrear. 

DEBUG (logging.info() o logging.debug()): Información detallada, típicamente de interés sólo durante el diagnóstico de problemas.
INFO (print()): Confirmación de que las cosas están funcionando como se esperaba.
WARNING (warnings.warn()): Un indicio de que algo inesperado sucedió, o indicativo de algún problema en el futuro cercano (por ejemplo, 
«espacio de disco bajo»). El software sigue funcionando como se esperaba.
ERROR (logging.error()): Debido a un problema más grave, el software no ha sido capaz de realizar alguna función.
CRITICIAL (logging.critical() ): Un grave error, que indica que el programa en sí mismo puede ser incapaz de seguir funcionando.


El nivel por defecto es WARNING, lo que significa que sólo los eventos de este nivel y superiores serán rastreados, a menos que 
el paquete de registro esté configurado para hacer lo contrario.

'''

import logging
import time

logging.basicConfig(filename = 'registro_taxi.log', level = logging.DEBUG)

class ConversorTiempo:
    def __init__(self, segundos):
        horas = int(segundos / 60 / 60)
        segundos -= horas*60*60
        minutos = int(segundos/60)
        segundos -= minutos*60
        return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

class Cronometro:
    def __init__(self):
        self.inicio = 0
        self.tiempo_pausado = 0
        self.tiempo_transcurrido = 0
        self.en_ejecucion = False
        logging.info("Cronómetro iniciado.")
        
        #es una booleana que indica si el crono esta en ejecución o no. Se inicia en 0 porque está parado.
 
    def empezar(self):
        if not self.en_ejecucion:
            self.inicio = time.time() - self.tiempo_pausado
            #time.time nos dice el valor actual del tiempo
            self.en_ejecucion = True
            #empezamos a contar
            logging.info("Cronómetro empezado.")

    def parar(self):
        if self.en_ejecucion:
            self.tiempo_pausado = time.time() - self.inicio
            #calcula el tiempo que pasa desde que inicia hasta la pausa.
            logging.info("El cronómetro está pausado.")

    def reanudar(self):
        if not self.en_ejecucion:
            self.inicio = time.time() - self.tiempo_pausado
            self.en_ejecucion = True
            logging.info("Cronómetro reanudado.")

    def finalizar(self):
        if self.en_ejecucion:
            self.tiempo_transcurrido = time.time() - self.inicio
            self.en_ejecucion = False
            logging.info("Cronómetro finalizado.")
            
        logging.info("Tiempo total transcurrido: " + "{0:.2f}".format(self.tiempo_transcurrido) + " segundos.")

class Taxi:
    def __init__(self):
        self.cronometro = Cronometro()
        #cada objeto taxi tendrá su propio obj crono asociado para restrear el tiempo
        self.estado = "parado"
        self.tiempo_pausado = 0

    def empezar(self):
        if self.estado == "parado":
            self.cronometro.empezar()
            self.estado = "en marcha"
            logging.info("El taxi está en marcha.")

    def parar(self):
        if self.estado == "en marcha":
            self.cronometro.parar()
            self.estado = "parado"
            logging.info("El taxi está parado.")
            self.tiempo_pausado = time.time()

    def reanudar(self):
        if self.estado == "parado":
            self.cronometro.reanudar()
            self.estado = "en marcha"
            tiempo_pausa = time.time() - self.tiempo_pausado
            self.tpprecio = tiempo_pausa* 0.02
          
            #valor actual menos tiempo pausado, se hace parar tener en cuenta el tiempo que ha pasado durante la pause y ajustar el tiempo de inicio
            logging.info("El taxi ha sido reanudado. Tiempo de pausa: " + "{0:.2f}".format(tiempo_pausa) + " seg. Con un precio total de " + "{0:.2f}".format(self.tpprecio) + " €")

    def finalizar(self):
        self.cronometro.finalizar()
        self.estado = "finalizado"
        logging.info("El taxi ha finalizado su servicio. Total: PRECIO TOTAL")

# Ejemplo de uso
taxi = Taxi()

while True:
    comando = input("Introduce un comando (empezar, parar, reanudar, finalizar): ")
    logging.info(f"Comando ingresado: {comando}")

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
        logging.warning("Comando inválido ingresado.")

logging.info("Programa finalizado.")

