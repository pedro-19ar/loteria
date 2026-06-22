"""Tests unitarios para el servicio de lotería."""

import unittest
import tempfile
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.servicio.servicio_loteria import ServicioLoteria
from src.repositorio.repositorio_loteria import RepositorioLoteria


class TestServicioLoteria(unittest.TestCase):
    """Tests para la clase ServicioLoteria."""

    def setUp(self):
        """Configurar servicio con repositorio temporal."""
        self.temp_dir = tempfile.mkdtemp()
        self.temp_file = os.path.join(self.temp_dir, "test_servicio.json")
        self.repo = RepositorioLoteria(ruta_archivo=self.temp_file)
        self.servicio = ServicioLoteria(repositorio=self.repo)
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

    # --- CU01: Registrar Número ---

    def test_registrar_numero_exitoso(self):
        """Test CU01: Registrar número con datos válidos."""
        resultado = self.servicio.registrar_numero(**self.datos_validos)
        self.assertEqual(resultado.numero, "0425")
        self.assertEqual(resultado.serie, "A")
        self.assertEqual(resultado.premio, "Mayor")
        self.assertIsNotNone(resultado.id)

    def test_registrar_numero_datos_invalidos(self):
        """Test CU01: Error al registrar con datos inválidos."""
        self.datos_validos["numero"] = "ABC"
        with self.assertRaises(ValueError):
            self.servicio.registrar_numero(**self.datos_validos)

    def test_registrar_multiples_numeros(self):
        """Test CU01: Registrar múltiples números."""
        self.servicio.registrar_numero(**self.datos_validos)
        self.datos_validos["numero"] = "1234"
        self.servicio.registrar_numero(**self.datos_validos)
        self.datos_validos["numero"] = "5678"
        self.servicio.registrar_numero(**self.datos_validos)
        numeros = self.servicio.listar_numeros()
        self.assertEqual(len(numeros), 3)

    # --- CU02: Actualizar Número ---

    def test_actualizar_numero_exitoso(self):
        """Test CU02: Actualizar número existente."""
        numero = self.servicio.registrar_numero(**self.datos_validos)
        actualizado = self.servicio.actualizar_numero(
            numero.id, serie="B", premio="Seco"
        )
        self.assertEqual(actualizado.serie, "B")
        self.assertEqual(actualizado.premio, "Seco")

    def test_actualizar_numero_inexistente(self):
        """Test CU02: Error al actualizar número inexistente."""
        with self.assertRaises(ValueError) as ctx:
            self.servicio.actualizar_numero("id-inexistente", serie="B")
        self.assertIn("No se encontró", str(ctx.exception))

    def test_actualizar_numero_datos_invalidos(self):
        """Test CU02: Error al actualizar con datos inválidos."""
        numero = self.servicio.registrar_numero(**self.datos_validos)
        with self.assertRaises(ValueError):
            self.servicio.actualizar_numero(numero.id, numero="ABC")

    def test_actualizar_estado(self):
        """Test CU02: Actualizar estado del número."""
        numero = self.servicio.registrar_numero(**self.datos_validos)
        actualizado = self.servicio.actualizar_numero(
            numero.id, estado="inactivo"
        )
        self.assertEqual(actualizado.estado, "inactivo")

    def test_actualizar_monto(self):
        """Test CU02: Actualizar monto del premio."""
        numero = self.servicio.registrar_numero(**self.datos_validos)
        actualizado = self.servicio.actualizar_numero(
            numero.id, monto_premio=2000000.00
        )
        self.assertEqual(actualizado.monto_premio, 2000000.00)

    # --- CU03: Borrar Número ---

    def test_borrar_numero_exitoso(self):
        """Test CU03: Borrar número existente."""
        numero = self.servicio.registrar_numero(**self.datos_validos)
        resultado = self.servicio.borrar_numero(numero.id)
        self.assertTrue(resultado)
        numeros = self.servicio.listar_numeros()
        self.assertEqual(len(numeros), 0)

    def test_borrar_numero_inexistente(self):
        """Test CU03: Error al borrar número inexistente."""
        with self.assertRaises(ValueError) as ctx:
            self.servicio.borrar_numero("id-inexistente")
        self.assertIn("No se encontró", str(ctx.exception))

    def test_borrar_no_afecta_otros(self):
        """Test CU03: Borrar un número no afecta a los demás."""
        n1 = self.servicio.registrar_numero(**self.datos_validos)
        self.datos_validos["numero"] = "1234"
        n2 = self.servicio.registrar_numero(**self.datos_validos)
        self.servicio.borrar_numero(n1.id)
        numeros = self.servicio.listar_numeros()
        self.assertEqual(len(numeros), 1)
        self.assertEqual(numeros[0].id, n2.id)

    # --- CU04: Listar Números ---

    def test_listar_numeros_vacio(self):
        """Test CU04: Listar cuando no hay registros."""
        numeros = self.servicio.listar_numeros()
        self.assertEqual(len(numeros), 0)

    def test_listar_numeros_con_datos(self):
        """Test CU04: Listar con registros existentes."""
        self.servicio.registrar_numero(**self.datos_validos)
        self.datos_validos["numero"] = "9999"
        self.servicio.registrar_numero(**self.datos_validos)
        numeros = self.servicio.listar_numeros()
        self.assertEqual(len(numeros), 2)

    # --- Búsquedas ---

    def test_obtener_numero_por_id(self):
        """Test: Obtener número por ID."""
        numero = self.servicio.registrar_numero(**self.datos_validos)
        resultado = self.servicio.obtener_numero(numero.id)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.numero, "0425")

    def test_obtener_numero_inexistente(self):
        """Test: Obtener número inexistente retorna None."""
        resultado = self.servicio.obtener_numero("id-inexistente")
        self.assertIsNone(resultado)

    def test_buscar_por_numero(self):
        """Test: Buscar por número de lotería."""
        self.servicio.registrar_numero(**self.datos_validos)
        self.datos_validos["sorteo"] = "S-2026-002"
        self.servicio.registrar_numero(**self.datos_validos)
        resultados = self.servicio.buscar_por_numero("0425")
        self.assertEqual(len(resultados), 2)

    def test_buscar_por_numero_sin_resultados(self):
        """Test: Buscar número que no existe."""
        resultados = self.servicio.buscar_por_numero("9999")
        self.assertEqual(len(resultados), 0)

    def test_buscar_por_sorteo(self):
        """Test: Buscar por sorteo."""
        self.servicio.registrar_numero(**self.datos_validos)
        resultados = self.servicio.buscar_por_sorteo("S-2026-001")
        self.assertEqual(len(resultados), 1)

    # --- Flujo completo ---

    def test_flujo_crud_completo(self):
        """Test: Flujo completo CRUD (crear, leer, actualizar, eliminar)."""
        # Crear
        numero = self.servicio.registrar_numero(**self.datos_validos)
        self.assertIsNotNone(numero.id)

        # Leer
        leido = self.servicio.obtener_numero(numero.id)
        self.assertEqual(leido.numero, "0425")

        # Actualizar
        actualizado = self.servicio.actualizar_numero(
            numero.id, numero="9999", serie="Z"
        )
        self.assertEqual(actualizado.numero, "9999")
        self.assertEqual(actualizado.serie, "Z")

        # Listar
        lista = self.servicio.listar_numeros()
        self.assertEqual(len(lista), 1)

        # Eliminar
        self.servicio.borrar_numero(numero.id)
        lista = self.servicio.listar_numeros()
        self.assertEqual(len(lista), 0)


if __name__ == "__main__":
    unittest.main()
