"""Tests unitarios para el modelo NumeroLoteria."""

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.modelo.numero_loteria import NumeroLoteria


class TestNumeroLoteria(unittest.TestCase):
    """Tests para la clase NumeroLoteria."""

    def setUp(self):
        """Configurar datos de prueba."""
        self.datos_validos = {
            "numero": "0425",
            "serie": "A",
            "sorteo": "S-2026-001",
            "fecha_sorteo": "2026-06-15",
            "premio": "Mayor",
            "monto_premio": 1000000.00
        }

    def test_crear_numero_valido(self):
        """Test: Crear un número de lotería con datos válidos."""
        numero = NumeroLoteria(**self.datos_validos)
        self.assertEqual(numero.numero, "0425")
        self.assertEqual(numero.serie, "A")
        self.assertEqual(numero.sorteo, "S-2026-001")
        self.assertEqual(numero.fecha_sorteo, "2026-06-15")
        self.assertEqual(numero.premio, "Mayor")
        self.assertEqual(numero.monto_premio, 1000000.00)
        self.assertEqual(numero.estado, "activo")
        self.assertIsNotNone(numero.id)
        self.assertIsNotNone(numero.fecha_registro)

    def test_numero_vacio(self):
        """Test: Error al crear número con valor vacío."""
        self.datos_validos["numero"] = ""
        with self.assertRaises(ValueError) as ctx:
            NumeroLoteria(**self.datos_validos)
        self.assertIn("vacío", str(ctx.exception))

    def test_numero_no_digitos(self):
        """Test: Error al crear número con caracteres no numéricos."""
        self.datos_validos["numero"] = "AB12"
        with self.assertRaises(ValueError) as ctx:
            NumeroLoteria(**self.datos_validos)
        self.assertIn("dígitos", str(ctx.exception))

    def test_numero_longitud_invalida(self):
        """Test: Error al crear número con longitud diferente a 4."""
        self.datos_validos["numero"] = "123"
        with self.assertRaises(ValueError) as ctx:
            NumeroLoteria(**self.datos_validos)
        self.assertIn("4 dígitos", str(ctx.exception))

    def test_serie_vacia(self):
        """Test: Error al crear número con serie vacía."""
        self.datos_validos["serie"] = ""
        with self.assertRaises(ValueError):
            NumeroLoteria(**self.datos_validos)

    def test_sorteo_vacio(self):
        """Test: Error al crear número con sorteo vacío."""
        self.datos_validos["sorteo"] = ""
        with self.assertRaises(ValueError):
            NumeroLoteria(**self.datos_validos)

    def test_fecha_sorteo_vacia(self):
        """Test: Error al crear número con fecha vacía."""
        self.datos_validos["fecha_sorteo"] = ""
        with self.assertRaises(ValueError):
            NumeroLoteria(**self.datos_validos)

    def test_premio_invalido(self):
        """Test: Error al crear número con premio inválido."""
        self.datos_validos["premio"] = "Invalido"
        with self.assertRaises(ValueError) as ctx:
            NumeroLoteria(**self.datos_validos)
        self.assertIn("Premio inválido", str(ctx.exception))

    def test_monto_negativo(self):
        """Test: Error al crear número con monto negativo."""
        self.datos_validos["monto_premio"] = -100
        with self.assertRaises(ValueError) as ctx:
            NumeroLoteria(**self.datos_validos)
        self.assertIn("positivo", str(ctx.exception))

    def test_estado_invalido(self):
        """Test: Error al crear número con estado inválido."""
        self.datos_validos["estado"] = "invalido"
        with self.assertRaises(ValueError):
            NumeroLoteria(**self.datos_validos)

    def test_to_dict(self):
        """Test: Conversión a diccionario."""
        numero = NumeroLoteria(**self.datos_validos)
        d = numero.to_dict()
        self.assertEqual(d["numero"], "0425")
        self.assertEqual(d["serie"], "A")
        self.assertEqual(d["sorteo"], "S-2026-001")
        self.assertEqual(d["premio"], "Mayor")
        self.assertEqual(d["monto_premio"], 1000000.00)
        self.assertIn("id", d)
        self.assertIn("fecha_registro", d)

    def test_from_dict(self):
        """Test: Creación desde diccionario."""
        numero_original = NumeroLoteria(**self.datos_validos)
        d = numero_original.to_dict()
        numero_copia = NumeroLoteria.from_dict(d)
        self.assertEqual(numero_original.id, numero_copia.id)
        self.assertEqual(numero_original.numero, numero_copia.numero)
        self.assertEqual(numero_original.serie, numero_copia.serie)

    def test_igualdad(self):
        """Test: Dos números con el mismo ID son iguales."""
        numero1 = NumeroLoteria(**self.datos_validos)
        numero2 = NumeroLoteria.from_dict(numero1.to_dict())
        self.assertEqual(numero1, numero2)

    def test_desigualdad(self):
        """Test: Dos números con diferente ID son distintos."""
        numero1 = NumeroLoteria(**self.datos_validos)
        numero2 = NumeroLoteria(**self.datos_validos)
        self.assertNotEqual(numero1, numero2)

    def test_repr(self):
        """Test: Representación string del objeto."""
        numero = NumeroLoteria(**self.datos_validos)
        repr_str = repr(numero)
        self.assertIn("0425", repr_str)
        self.assertIn("Mayor", repr_str)

    def test_premios_validos(self):
        """Test: Verificar todos los premios válidos."""
        for premio in NumeroLoteria.PREMIOS_VALIDOS:
            self.datos_validos["premio"] = premio
            numero = NumeroLoteria(**self.datos_validos)
            self.assertEqual(numero.premio, premio)

    def test_estados_validos(self):
        """Test: Verificar todos los estados válidos."""
        for estado in NumeroLoteria.ESTADOS_VALIDOS:
            self.datos_validos["estado"] = estado
            numero = NumeroLoteria(**self.datos_validos)
            self.assertEqual(numero.estado, estado)

    def test_monto_cero(self):
        """Test: Monto cero es válido."""
        self.datos_validos["monto_premio"] = 0
        numero = NumeroLoteria(**self.datos_validos)
        self.assertEqual(numero.monto_premio, 0)


if __name__ == "__main__":
    unittest.main()
