import unittest
from io import StringIO
from contextlib import redirect_stdout
from datetime import datetime
from taxi_OK import Taxi


class TaxiTest(unittest.TestCase):
    def test_empezar(self):
        taxi = Taxi()
        taxi.empezar()
        self.assertEqual(taxi.estado, "en marcha")

    def test_parar(self):
        taxi = Taxi()
        taxi.empezar()
        taxi.parar()
        self.assertEqual(taxi.estado, "parado")

    def test_reanudar(self):
        taxi = Taxi()
        taxi.empezar()
        taxi.parar()
        taxi.reanudar()
        self.assertEqual(taxi.estado, "en marcha")

    def test_finalizar(self):
        taxi = Taxi()
        taxi.empezar()
        taxi.finalizar()
        self.assertEqual(taxi.estado, "finalizado")

    def test_reiniciar(self):
        taxi = Taxi()
        taxi.empezar()
        taxi.finalizar()
        taxi.reiniciar()
        self.assertEqual(taxi.estado, "parado")

    def test_output(self):
        taxi = Taxi()
        input_commands = ["empezar", "parar", "reanudar", "finalizar"]
        expected_output = [
            "El taxi está en marcha.\n",
            "El taxi está parado.\n",
            "El taxi ha sido reanudado. Tiempo de esta pausa: 0.00 seg. Tiempo total de pausas: 0.00 seg. Total pausas: 0.00 €\n",
            "El taxi ha finalizado su servicio. Total: 0.00 seg. Segundos reales en marcha 0.00 seg. Precio total de carrera 0.00 €\n",
        ]

        with redirect_stdout(StringIO()) as stdout:
            for command, output in zip(input_commands, expected_output):
                with self.subTest(command=command):
                    stdin = StringIO(command + "\n")
                    with redirect_stdout(stdout):
                        with unittest.mock.patch("builtins.input", lambda: stdin.readline().strip()):
                            taxi = Taxi()
                            taxi.start_service()

                self.assertEqual(stdout.getvalue(), output)
                stdout.truncate(0)
                stdout.seek(0)


if __name__ == "__main__":
    unittest.main()
