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

    '''
from datetime import datetime
import tkinter as tk





class Taxi:
    def __init__(self):
        self.parado =  True
        self.inicio = None
        self.fin = None


    def iniciar_carrera(self):
        print("Bienvenidos/as al taxiguay.EXPLICACION DE FUNCIONAMIENTO.")
        print("Para inicar pulse: 'Empezar'.")
        print("Para parar por tráfico, semáforo, pulse: 'parar'. ")
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
                print("Taxi detenido.")

            elif comando == "fin":
             total = self.finalizar_carrera()
             print(f"Viaje finalizado. Total de tiempo en el taxi: {total} segundos")  
             break

            else:
             print("Comando inválido. Por favor, ingrese 'Empezar', 'parar' o 'fin'.")

    def finalizar_carrera(self):
        if not self.parado:
            self.parado = True
            self.fin = datetime.now()

        tiempo_transcurrido = (self.fin - self.inicio).total_seconds() if self.fin else 0
        self.inicio = None
        self.fin = None


        return tiempo_transcurrido




taxi = Taxi()
taxi.iniciar_carrera()

from datetime import datetime
import tkinter as tk

from http.client import OK



def mensaje():
    print("Bienvenidos/as al taxiguay.EXPLICACION DE FUNCIONAMIENTO.")
    print("Para inicar AQUI LA FUNCIÓN")
    print("Para parar por tráfico, semáforo AQUÍ LA FUNCIÓN")
    print("Para fin de carrera AQUÍ LA FUNCIÓN")
        
mensaje()


total = OK
class Taxi:
    def __init__(self):
        self.parado =  True
        self.inicio = 0
        self.fin = 0





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

'''segundos = datetime.now() #fecha para los datos
print(segundos.second)'''


