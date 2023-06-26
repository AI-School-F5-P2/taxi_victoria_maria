import time

#Clase para el cronómetro
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
            #time.time nos dice el valor actual del tiempo
            self.en_ejecucion = True
            #empezamos a contar
            #print("Cronómetro empezado.")

    def parar(self):
        if self.en_ejecucion:
            self.tiempo_pausado = time.time() - self.inicio
            #calcula el tiempo que pasa desde que inicia hasta la pausa.
            #print("El cronómetro está pausado.")

    def reanudar(self):
        if not self.en_ejecucion:
            self.inicio = time.time() - self.tiempo_pausado
            self.en_ejecucion = True
            #print("Cronómetro reanudado.")

    def finalizar(self):
        if self.en_ejecucion:
            self.tiempo_transcurrido = time.time() - self.inicio          
            self.en_ejecucion = False
            #print("Cronómetro finalizado.")
            
       
#conversor de tiempo en horas, minutos y segundos

class Taxi (Cronometro):
    def __init__(self):
        self.cronometro = Cronometro()
        #cada objeto taxi tendrá su propio obj crono asociado para restrear el tiempo
        self.estado = "parado"
        self.tiempo_pausa_total= 0
        self.tiempo_acumulado = 0
        self.precioparado = 0.02 #precio parada
        self.preciomarcha = 0.05 #precio en marcha

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
            self.tiempo_pausado = time.time()

    def reanudar(self):
        if self.estado == "parado":
            self.cronometro.reanudar()
            self.estado = "en marcha"
            tiempo_pausa = time.time() - self.tiempo_pausado
            self.tiempo_acumulado += tiempo_pausa #incremento de pausas
            self.tpprecio = self.tiempo_acumulado* self.precioparado #precio total de pausas
          
            #La valores mostrados son: El tiempo de la pausa, el total de todas las pausas y el dinero que es en total las pausas
            print("El taxi ha sido reanudado. Tiempo de esta pausa: " + "{0:.2f}".format(tiempo_pausa) + " seg. Tiempo total de pausas: " + "{0:.2f}".format(self.tiempo_acumulado) + " seg. Total pausas: " + "{0:.2f}".format(self.tpprecio) + " €")

    def fin(self):
        self.cronometro.finalizar()
        self.estado = "finalizado"
        tiempo_transcurrido = self.cronometro.tiempo_transcurrido
        self.tiempo_final = tiempo_transcurrido - self.tiempo_acumulado 
        self.preciototal = self.tiempo_final * self.preciomarcha
        #Sumatorio total sin hacer ningún tipo de parada
        print("El taxi ha finalizado su servicio. Total:" +"{0:.2f}".format(tiempo_transcurrido) + " seg. Precio total de carrera " + "{0:.2f}".format(self.preciototal) +" €") 
    
        
    def finalizar(self):
        self.cronometro.finalizar()
        self.estado = "finalizado"
        tiempo_transcurrido = self.cronometro.tiempo_transcurrido
        self.tiempo_final = tiempo_transcurrido - self.tiempo_acumulado #resta para averiguar cual segundos es el total
        self.preciototal = (self.tiempo_final * self.preciomarcha) + self.tpprecio #precio real
        #Se muestran los valores de: Total de la carrera, cuand han sido los segundos en REALES en marcha, y el total de la carrera. 
        print("El taxi ha finalizado su servicio. Total:" +"{0:.2f}".format(tiempo_transcurrido) + " seg. Segundos reales en marcha "  + "{0:.2f}".format(self.tiempo_final) + " seg. Precio total de carrera " + "{0:.2f}".format(self.preciototal) +" €")    
    
    def reiniciar(self):
        self.cronometro.finalizar()
        self.cronometro = Cronometro()
        self.tiempo_acumulado = 0 #resetea todo lo antes calculado
        self.estado = "parado"
        print("Inicia una nueva carrera")

# Ejemplo de uso
taxi = Taxi()
while True:
    comando = input("Introduce un comando. empezar, parar, reanudar, fin (finalizar sin paradas), finalizar): ")
#comandos que usamos para mover nuestro taxi
    if comando == "empezar":
        taxi.empezar()   
    elif comando == "parar":
        taxi.parar()
    elif comando == "reanudar":
        taxi.reanudar()
    elif comando == "fin":
        taxi.fin()
        reiniciar = input("¿Deseas inciciar una nueva carrera? (si/no): ")
        if reiniciar.lower() == "si": 
            taxi.reiniciar()
    elif comando == "finalizar":
        taxi.finalizar()
        reiniciar = input("¿Deseas inciciar una nueva carrera? (si/no): ")
        if reiniciar.lower() == "si": 
            taxi.reiniciar()
        else:    
            break
    else:
        print("Comando inválido.")