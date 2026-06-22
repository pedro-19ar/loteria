"""Tests unitarios para el repositorio de lotería."""

import unittest
import tempfile
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.modelo.numero_loteria import NumeroLoteria
from src.repositorio.repositorio_loteria import RepositorioLoteria


class TestRepositorioLoteria(unittest.TestCase):
    """Tests para la clase RepositorioLoteria."""

    def setUp(self):
        """Configurar repositorio con archivo temporal."""
        self.temp_dir = tempfile.mkdtemp()
        self.temp_file = os.path.join(self.temp_dir, "test_loteria.json")
        self.repo = RepositorioLoteria(ruta_archivo=self.temp_file)
        self.datos_validos = {
            "numero": "0425",
            "serie": "A",
            "sorteo": "S-2026-001",
            "fecha_sorteo": "2026-06-15",
            "premio": "Mayor",
            "monto_premio": 1000000.00
        }

    def tearDown(self):
        """Limpiar archivos temporales."""
        if os.path.exists(self.temp_file):
            os.remove(self.temp_file)
        if os.path.exists(self.temp_dir):
            os.rmdir(self.temp_dir)

    def _crear_numero(self, **kwargs):
        """Helper para crear un número de lotería."""
        datos = {**self.datos_validos, **kwargs}
        return NumeroLoteria(**datos)

    def test_crear_registro(self):
        """Test: Crear un registro en el repositorio."""
        numero = self._crear_numero()
        resultado = self.repo.crear(numero)
        self.assertEqual(resultado.numero, "0425")
        self.assertEqual(self.repo.contar(), 1)

    def test_crear_duplicado(self):
        """Test: Error al crear registro duplicado."""
        numero = self._crear_numero()
        self.repo.crear(numero)
        with self.assertRaises(ValueError) as ctx:
            self.repo.crear(numero)
        self.assertIn("Ya existe", str(ctx.exception))

    def test_obtener_por_id(self):
        """Test: Obtener registro por ID."""
        numero = self._crear_numero()
        self.repo.crear(numero)
        resultado = self.repo.obtener_por_id(numero.id)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.numero, "0425")

    def test_obtener_por_id_inexistente(self):
        """Test: Obtener registro con ID inexistente."""
        resultado = self.repo.obtener_por_id("id-inexistente")
        self.assertIsNone(resultado)

    def test_obtener_todos(self):
        """Test: Obtener todos los registros."""
        self.repo.crear(self._crear_numero(numero="0001"))
        self.repo.crear(self._crear_numero(numero="0002"))
        self.repo.crear(self._crear_numero(numero="0003"))
        resultados = self.repo.obtener_todos()
        self.assertEqual(len(resultados), 3)

    def test_obtener_todos_vacio(self):
        """Test: Obtener todos cuando no hay registros."""
        resultados = self.repo.obtener_todos()
        self.assertEqual(len(resultados), 0)

    def test_actualizar_registro(self):
        """Test: Actualizar un registro existente."""
        numero = self._crear_numero()
        self.repo.crear(numero)
        numero.serie = "B"
        numero.validar()
        resultado = self.repo.actualizar(numero)
        self.assertEqual(resultado.serie, "B")
        verificacion = self.repo.obtener_por_id(numero.id)
        self.assertEqual(verificacion.serie, "B")

    def test_actualizar_inexistente(self):
        """Test: Error al actualizar registro inexistente."""
        numero = self._crear_numero()
        with self.assertRaises(ValueError) as ctx:
            self.repo.actualizar(numero)
        self.assertIn("No se encontró", str(ctx.exception))

    def test_eliminar_registro(self):
        """Test: Eliminar un registro."""
        numero = self._crear_numero()
        self.repo.crear(numero)
        resultado = self.repo.eliminar(numero.id)
        self.assertTrue(resultado)
        self.assertEqual(self.repo.contar(), 0)

    def test_eliminar_inexistente(self):
        """Test: Error al eliminar registro inexistente."""
        with self.assertRaises(ValueError) as ctx:
            self.repo.eliminar("id-inexistente")
        self.assertIn("No se encontró", str(ctx.exception))

    def test_eliminar_todos(self):
        """Test: Eliminar todos los registros."""
        self.repo.crear(self._crear_numero(numero="0001"))
        self.repo.crear(self._crear_numero(numero="0002"))
        self.repo.eliminar_todos()
        self.assertEqual(self.repo.contar(), 0)

    def test_contar(self):
        """Test: Contar registros."""
        self.assertEqual(self.repo.contar(), 0)
        self.repo.crear(self._crear_numero(numero="0001"))
        self.assertEqual(self.repo.contar(), 1)
        self.repo.crear(self._crear_numero(numero="0002"))
        self.assertEqual(self.repo.contar(), 2)

    def test_persistencia(self):
        """Test: Los datos se persisten correctamente en el archivo."""
        numero = self._crear_numero()
        self.repo.crear(numero)
        # Crear nueva instancia del repositorio con el mismo archivo
        repo2 = RepositorioLoteria(ruta_archivo=self.temp_file)
        resultado = repo2.obtener_por_id(numero.id)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.numero, "0425")


if __name__ == "__main__":
    unittest.main()
