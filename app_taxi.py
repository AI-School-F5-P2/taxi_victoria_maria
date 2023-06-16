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
       break 



from datetime import datetime
import tkinter as tk

def mensaje():
    print("Bienvenidos/as al taxiguay.EXPLICACION DE FUNCIONAMIENTO.")
    print("Para inicar AQUI LA FUNCIÓN")
    print("Para parar por tráfico, semáforo AQUÍ LA FUNCIÓN")
    print("Para fin de carrera AQUÍ LA FUNCIÓN")
        
mensaje()


from datetime import datetime
import tkinter as tk

#Cronómetro y ventana emergente que nos muestra el tiempo que ha transcurrido desde el inicio. 

hora_inicio = datetime.now()
intervalos = 1000


def segundos_total(segundos): #formatea el timedate.now convirtiendolo en 00:00:00
    horas = int(segundos /60/60)
    segundos -= horas *60*60
    minutos= int (segundos/60)
    segundos -= minutos*60
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

#Comprobación de si funciona la función
segundos = refresh_tiempo
resultado = segundos_total(segundos)
print(resultado)

def t_formateado ():
    seg_transcurridos= (datetime.now()- hora_inicio).total_seconds()
    return segundos_total(int(seg_transcurridos))

seg_transcurridos = 40  # Valor específico para seg_transcurridos
formateo = t_formateado()
print(formateo)

def refresh_tiempo():
    print()
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

import time
from datetime import datetime, timedelta

inicio = time.time()

count = 0
end_time = time.time() + 2
while time.time() < end_time:
    count += 1
fin = time.time()

segundos_totales = fin - inicio

print(f"Segundos transcurridos: {segundos_totales:.2f} segundos")


inicio = int(segundos_totales * 5)
parada = segundos_totales*0,2
fin= inicio + parada

print("inicio",inicio)
print("parada",parada)
print("fin",fin)