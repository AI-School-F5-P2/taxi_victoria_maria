#Test unitarios
import unittest
#módulo que proporciona la funcionalidad para escribir y ejecutar pruebas unitarias
from io import StringIO
#redirige la salida estandar.
from contextlib import redirect_stdout
#lo que te permite llevarlo a StringIO
from taxi_OK import Taxi

class TestTaxi(unittest.TestCase):
    def setUp(self):
        self.taxi = Taxi()
        self.taxi.empezar()

    def tearDown(self):
        self.taxi.finalizar()

    def test_empezar(self):
        self.assertEqual(self.taxi.estado, "en marcha")

    def test_parar(self):
        self.taxi.parar()
        self.assertEqual(self.taxi.estado, "parado")

    def test_reanudar(self):
        self.taxi.parar()
        self.taxi.reanudar()
        self.assertEqual(self.taxi.estado, "en marcha")

    def test_finalizar(self):
        with redirect_stdout(StringIO()):
            self.taxi.finalizar()
        self.assertEqual(self.taxi.estado, "finalizado")

    def test_reiniciar(self):
        self.taxi.reiniciar()
        self.assertEqual(self.taxi.estado, "parado")

if __name__ == '__main__':
    unittest.main()
