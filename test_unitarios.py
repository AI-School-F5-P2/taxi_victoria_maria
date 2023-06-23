#Test unitarios
import unittest
#módulo que proporciona la funcionalidad para escribir y ejecutar pruebas unitarias
from io import StringIO
#redirige la salida estandar.
from contextlib import redirect_stdout
#lo que te permite llevarlo a StringIO
from taxi_OK import Taxi

class TestTaxi(unittest.TestCase):
    #TestTaxi esta clase hereda de:unittest.TestCase que es una clase base propocionada por unittest
    def setUp(self):
        #setup se ejecuta antes de de cada prueba y se usa para cualquier config necesaria antes de la prueba
        self.taxi = Taxi()
        self.taxi.empezar()
    #este codigo prepara un escenario inicial común para cada prueba dentro de la clase TestTaxi creando el obj Taxi
    # asegurandonos de que cada prueba se ejecute en un contexto consistente evitandonos la necesidad de escribir el
    # codigo por cada prueba    

    def tearDown(self):
        # tearDown se ejecuta después de cada prueba, lo contrario que setUp
        self.taxi.finalizar()

    def test_empezar(self):
        self.assertEqual(self.taxi.estado, "en marcha")
        #assertEqual se utiliza para comparar el valor actual del estado del objeto Taxi con el valor esperado "en marcha".
        #con la línea de arriba verificamos que los dos valores sean iguales.

    def test_parar(self):
        self.taxi.parar()
        self.assertEqual(self.taxi.estado, "parado")
        #lo mismo que arriba, compramos el estado actual con el valor esperado.

    def test_reanudar(self):
        self.taxi.parar()
        self.taxi.reanudar()
        self.assertEqual(self.taxi.estado, "en marcha")
        #verifica que los dos métodos del obj taxi establecen bien su estado de parado y cambia a en marcha.

    def test_finalizar(self):
        with redirect_stdout(StringIO()):
            #redirige la salida estandar al obj stringIO para ejecutar cualquier salida y evitar la impresión en la consola
            self.taxi.finalizar()
        self.assertEqual(self.taxi.estado, "finalizado")
        #comparamos el valor actual con el esperado


if __name__ == '__main__':
    #verificamos que el módulo actual se ejecute como el programa principal y no desde un módulo importado
    unittest.main()
    #esta función nos ejecuta todos los test definidos en la clase TestCase que esten en el mismo archivo.
    #Ejecuta todos los métodos de prueba que tienen nomnres empezados por la palabra test.
