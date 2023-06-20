''' 
While para arrancar f=2 por segundo
      para parar f=para de contar ; nos hace un sumatorio con el total de euros
        para movimiento f= arrancar+3 por segundo
class taxi (self, second):
arrancartaxi = 
datetime.second

secret_number=20

while True:
   number = input('Guess the number: ') 
   try:
       number = int(number)
   except:
       print('Sorry that is not a number')
       continue
   if number != secret_number:
       if number > secret_number:
           print(number, 'is greater than the secret number') 
       elif number < secret_number:
           print(number, 'is less than the secret number')
   else:
       print('You guessed the number:', secret_number)
       break ''' 






'''
Utilizar None en vez de 0 es más correcto para representar la ausencia de un valor, ya que al utilizar 0 uss un vaor númerico específico y no es necesario
'''


        
'''mensaje(), no hace falta hacerlo así, simplemente con poner self dentro de mensaje funciona'''   




'''
    1. He definido los strings 'Empezar', 'parar' y 'fin' como los comandos que van a ejecutar el taxi
    2. While:se ejecuta continuamente hasta que encuentre una instrucción de interrupción
    3. Utilizamos == para comparar la palabra 'Empezar' y si es correcto ejecutarlo
    4. Si está parado, 'Empezar' sería falso, indicandonos que está en movimiento y si no (self.inicio) nos reistraría el tiempo actual usando 'datetime.now()'
    y nos lo guarda en self.inicio, después nos muestra el mensaje.
    5. == 'parar' se está asegurando que el taxi no esté ya parado antes de realizar la acción de detenerlo. Si self.parado es False significa que el taxi está en 
    movimiento, por lo tanto se cumple la acción not self.parado. (NOT niega una condición). Basicamente not self.parado lo usamos para verificar que no esté 
    previamente parado antes de realizar la acción.
    5. finalizar_carrera() calcula el tiempo total transcurrido y se guarda en la variable total. Usa las variables self.inicio y self.fin
    6. f antes de comillas y con {} en el interior se llama f-string y se usa para formatear cadenas, permitiendo usar variables y expresiones, al tener {}, 
    python reconoce que esa parte debe ser evaluada y reemplazada.
    7.finalizar_carrera verifica si el taxi está en movimiento y si es así lo detiene estableciendo 'self.parado' en true. Después nos dice el momento de finalización
    en el atributo 'self.fin' utilizando 'datetime.now()'
    8.Realizamos una resta entre fin e inicio recibiendo un objeto de tipo timedelta que representa la difencia de tiempo entre los dos momentos y usamos '.total_seconds'
    también un método timdelta que nos devuelve la duración total 
    9.usamos 'self.fin' else 0 se utiliza en el caso de que no este definida, es decir, si la carrera no ha terminado y se estableceía 'tiempo_transcurrido' como 0.
    10. Timedelta es una clase en el módulo datetime que representa una duración o diferencia entre dos momentos en el tiempo. Proporciona métodos y atributos para realizar
    operaciones matemáticas y obtener info sobre la diferencia de tiempo y se crea mediante la resta de dos objetos
    11.'self.inicio' y 'self.fin' none indica que no hay ningun momento de inicio o fin registrado y se preprara para nueva carrera después de haber calculado el tiempo 
    transcurrido.
    12.el método finalizar_carrera() realiza el cálculo del tiempo transcurrido entre inicio y fin de carrera lo almacena en la variable 'tiempo_trancurrido' y nos lo devuelve
    con un return.
    13. Creamos un obejto llmado taxi que es una instancia de la clase Taxi. Con este objeto podemos llamar al método 'iniciar_carrera() para comenzar.
    Esta clase es esencial para poder utilizar la funcionalidad de Taxi. 
    14. Finalmente iniciamos la carrera
    ARREGLOS
    La función parar no sirve, ya que si paras el taxi, el tiempo que llevamos en marcha se convierte en 0 y el fin nos daría un total de 0.
    Cambios marcados con# a lo largo del código.

    '''
'''
from datetime import datetime
import tkinter as tk





class Taxi:
    def __init__(self):
        self.parado =  True
        self.inicio = None
        self.fin = None
        self.tiempo_detenido = 0
        # se añade el tiempo detenido.


    def iniciar_carrera(self):
        print("Bienvenidos/as al taxiguay.EXPLICACION DE FUNCIONAMIENTO.")
        print("Para inicar pulse: 'Empezar'.")
        print("Para parar por tráfico, semáforo, pulse: 'parar'. ")
        print("Para reiniciar el taxi, pulse: 'reiniciar'.")
        print("Para fin de carrera pulsa 'fin'.")




        while True: 
            comando = input("Ingresa un comando:")

            if comando == "Empezar":
                if self.parado:
                    self.parado = False
                    self.inicio = datetime.now()
                print("Taxi en movimiento.")

            elif comando == 'parar':
                if not self.parado:
                    self.parado = True
                    tiempo_detenido_actual = (datetime.now() - self.inicio).total_seconds()
                    #Calcula el tiempo desde el inicio hasta el actual. Lo hacems restando self.inicio del actual datetime.now y utilizando
                    # .total_seconds() obtenemos en resultado en seg.
                    self.tiempo_detenido += tiempo_detenido_actual
                    #Suma el tiempo detenido actual, al tiempo total acumulado
                    print(f"Taxi detenido. Tiempo total detenido: {self.tiempo_detenido} segundos.")
                else:
                    print("El taxi ya está detenido.")

            elif comando == 'reiniciar':
                if self.parado:
                    #verifica si está detenido y si es True ejecuta el bloque de código
                    self.parado = False
                    #Al establecerlo en False indicamos que está en mov de nuevo
                    print("Taxi en marcha de nuevo.")
                    #añadimos reiniciar con parado en False para que lo detecte y vuelva a contar.

            elif comando == "fin":
                total = self.finalizar_carrera()
                print(f"Viaje finalizado. Total de tiempo en el taxi: {total} segundos")  
                #print con f-string para poder cambiar valores.
                break

            else:
                print("Comando inválido. Por favor, ingrese 'Empezar', 'parar', 'reiniciar' o 'fin'.")
                #Si ya está detenido nos imprime esto.

    def finalizar_carrera(self):
            if not self.parado:
                self.parado = True
                self.fin = datetime.now()
                tiempo_transcurrido = (self.fin - self.inicio).total_seconds() - self.tiempo_detenido
                #cambiamos self.fin else 0 por la resta del tiempo detenido
            else:  
                tiempo_transcurrido = self.tiempo_detenido  
                #añadimos este else para que no se puede detener varias veces, si está ya detenido, te lo dicef 


            self.inicio = None
            self.fin = None
            self.tiempo_detenido = 0
            # restablece el tiempo total detenido



            return tiempo_transcurrido




taxi = Taxi()
taxi.iniciar_carrera()
'''




'''

ESTE ES EL CODIGO CON MIS ANOTACIONES PARA HAY ALGO MAL
import os
import time
from datetime import datetime
import tkinter as tk
import threading


class Taxi:
    def __init__(self):
        self.parado = True
        #Está inicialmente detenido
        self.inicio = None
        #Almacenará la marca del tiempo cuando se empiece a mover
        self.tiempo_detenido = 0
        #Llevará un seguimiento del tiempo en segundos que ha estado parado(útil para distiguir el tiempo que costara 2 cent)
        self.mostrando_tiempo = False


    def empezar(self):
        if self.parado:
            self.parado = False
            self.inicio = datetime.now()
            print("Taxi en movimiento.")
            if not self.mostrando_tiempo:
                self.mostrando_tiempo = True
                threading.Thread(target=self.mostrar_tiempo).start()
        else:
            print("El taxi ya está en marcha.")

    def parar(self):
        if self.parado:
            print("El taxi ya está detenido.")
            
        else:
            self.tiempo_detenido += (datetime.now() - self.inicio).total_seconds()
            #calculamos el tiempo que estuve detenido hasta el momento actual restando la marca de 
            #tiempo actual menos la de inicio y utilizamos .t_s() para obtener duracion en seg
            # ver self.tiempo_detenido += tiempo_detenido_actual
            #esto nos permite acumular el tiempo detenido el las paradas
            self.parado = True
            #indicamos que está detenido e imprimimos
            print("Taxi detenido.")       

    def reanudar(self):
        if self.parado:
            self.parado = False
            self.inicio = datetime.now()
            #actualizamos la marca de tiempo de inicio con la actual, sirve para calcular
            #un nuevo punto de partida 
            print("Taxi reanudado.")
        else:
            print("El taxi ya está en marcha.")

    def finalizar(self):
        # esto anterior if self.parado:
        if self.inicio is None:
            print("El taxi no ha sido iniciado.")
            return 0
        
        if not self.parado:
            self.parar()
            
        tiempo_transcurrido = (datetime.now() - self.inicio).total_seconds() + self.tiempo_detenido

        self.inicio = None 
        self.parado = True
        self.tiempo_detenido = 0

        return tiempo_transcurrido
             
    


taxi = Taxi()
opcion = None
#se asegura de que el bucle se ejecute al menos una vez antes de empezar a hacer el resto

while opcion != "salir": 
    #!= verifica si el valor es distinto de salir y si es así ejecuta lo siguiente   
    print("¿Qué deseas hacer?")
    print("1. Empezar")
    print("2. Parar")
    print("3. Reanudar")
    print("4. Finalizar")
    print("5. Salir")
while True:
    
        opcion = input("Ingresa la opción: ")

        if opcion.lower() == "empezar":
            taxi.empezar()
        elif opcion.lower() == "parar":
            taxi.parar()
        elif opcion.lower() == "reanudar":
            taxi.reanudar()
        elif opcion.lower() == "finalizar":
            total = taxi.finalizar()
            print(f"Viaje finalizado. Total de tiempo en el taxi: {total} segundos")
        elif opcion.lower() == "salir":
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")
    



'''
'''
#Cronómetro y ventana emergente que nos muestra el tiempo que ha transcurrido desde el inicio. 

hora_inicio = datetime.now()
intervalos = 500 

def segundos_total(segundos):
    horas = int(segundos /60/60)
    segundos -= horas *60*60
    minutos= int (segundos/60)
    segundos -= minutos*60
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

def t_formateado ():
    seg_transcurridos= (datetime.now()- hora_inicio).total_seconds()
    return segundos_total(int(seg_transcurridos))

def refresh_tiempo():
    print("funciona")
    v_hora_actual.set(t_formateado())
    raiz.after(intervalos, refresh_tiempo)

raiz= tk.Tk()
v_hora_actual = tk.StringVar(raiz, value = t_formateado())
raiz.etiqueta= tk.Label(
    raiz, textvariable=v_hora_actual, font=f"Consolas 60")
raiz.etiqueta.pack(side="top")
app = tk.Frame()
raiz.title("prueba")
refresh_tiempo()
app.pack()
app.mainloop()
'''
'''segundos = datetime.now() #fecha para los datos
print(segundos.second)'''


'''

FINALLLLLLLLLL

from datetime import datetime
import tkinter as tk


class Taxi:
    def __init__(self):
        self.parado = True
        self.inicio = None
        self.tiempo_detenido = 0

    def empezar(self):
        if self.parado:
            self.parado = False
            self.inicio = datetime.now()
            print("Taxi en movimiento.")
        else:
            print("El taxi ya está en movimiento.")

    def parar(self):
        if not self.parado:
            self.parado = True
            tiempo_detenido_actual = (datetime.now() - self.inicio).total_seconds()
            self.tiempo_detenido += tiempo_detenido_actual
            print("Taxi detenido.")
        else:
            print("El taxi ya está detenido.")

    def reanudar(self):
        if self.parado:
            self.parado = False
            self.inicio = datetime.now()
            print("Taxi reanudar.")
        else:
            print("El taxi ya está en movimiento.")

    def finalizar(self):
        if not self.parado:
            self.parado = True
            tiempo_transcurrido = (datetime.now() - self.inicio).total_seconds() + self.tiempo_detenido
        else:
            tiempo_transcurrido = self.tiempo_detenido

        self.inicio = None
        self.tiempo_detenido = 0

        return tiempo_transcurrido


taxi = Taxi()

while True:
    opcion = input("Ingresa la opción: ")

    if opcion.lower() == "empezar":
        taxi.empezar()
    elif opcion.lower() == "parar":
        taxi.parar()
    elif opcion.lower() == "reanudar":
        taxi.reanudar()
    elif opcion.lower() == "finalizar":
        total = taxi.finalizar()
        print(f"Viaje finalizado. Total de tiempo en el taxi: {total} segundos")
        break
    elif opcion.lower() == "salir":
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")

'''
import threading
from datetime import datetime
import time

class Taxi:
    def __init__(self):
        self.parado = True
        self.inicio = None
        self.tiempo_detenido = 0

    def empezar(self):
        if self.parado:
            self.parado = False
            self.inicio = datetime.now()
            print("Taxi en movimiento.")
        else:
            print("El taxi ya está en movimiento.")

    def parar(self):
        if not self.parado:
            self.parado = True
            tiempo_detenido_actual = (datetime.now() - self.inicio).total_seconds()
            self.tiempo_detenido += tiempo_detenido_actual
            print("Taxi detenido.")
        else:
            print("El taxi ya está detenido.")

    def reiniciar(self):
        if self.parado:
            self.parado = False
            self.inicio = datetime.now()
            print("Taxi reiniciado.")
        else:
            print("El taxi ya está en movimiento.")

    def finalizar(self):
        if not self.parado:
            self.parado = True
            tiempo_transcurrido = (datetime.now() - self.inicio).total_seconds() + self.tiempo_detenido
        else:
            tiempo_transcurrido = self.tiempo_detenido

        self.inicio = None
        self.tiempo_detenido = 0

        return tiempo_transcurrido

def contador_segundos():
    segundos = 0
    while True:
        segundos += 1
        print(f"Segundos transcurridos: {segundos}")
        time.sleep(1)

taxi = Taxi()

hilo_contador = threading.Thread(target=contador_segundos)
hilo_contador.start()

while True:
    opcion = input("Ingresa la opción: ")

    if opcion.lower() == "empezar":
        taxi.empezar()
    elif opcion.lower() == "parar":
        taxi.parar()
    elif opcion.lower() == "reiniciar":
        taxi.reiniciar()
    elif opcion.lower() == "finalizar":
        total = taxi.finalizar()
        print(f"Viaje finalizado. Total de tiempo en el taxi: {total} segundos")
        break
    elif opcion.lower() == "salir":
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")
