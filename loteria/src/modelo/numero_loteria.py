"""Modelo de datos para Número de Lotería."""

import uuid
from datetime import datetime


class NumeroLoteria:
    """Representa un resultado de lotería."""

    PREMIOS_VALIDOS = ["Mayor", "Seco", "Aproximación", "Terminal", "Otro"]
    ESTADOS_VALIDOS = ["activo", "inactivo"]

    def __init__(self, numero: str, serie: str, sorteo: str,
                 fecha_sorteo: str, premio: str, monto_premio: float,
                 estado: str = "activo", id: str = None,
                 fecha_registro: str = None):
        self.id = id or str(uuid.uuid4())
        self.numero = numero
        self.serie = serie
        self.sorteo = sorteo
        self.fecha_sorteo = fecha_sorteo
        self.premio = premio
        self.monto_premio = monto_premio
        self.estado = estado
        self.fecha_registro = fecha_registro or datetime.now().isoformat()
        self.validar()

    def validar(self):
        """Valida los datos del número de lotería."""
        if not self.numero or not self.numero.strip():
            raise ValueError("El número de lotería no puede estar vacío.")
        if not self.numero.isdigit():
            raise ValueError("El número de lotería debe contener solo dígitos.")
        if len(self.numero) != 4:
            raise ValueError("El número de lotería debe tener exactamente 4 dígitos.")
        if not self.serie or not self.serie.strip():
            raise ValueError("La serie no puede estar vacía.")
        if not self.sorteo or not self.sorteo.strip():
            raise ValueError("El sorteo no puede estar vacío.")
        if not self.fecha_sorteo or not self.fecha_sorteo.strip():
            raise ValueError("La fecha del sorteo no puede estar vacía.")
        if self.premio not in self.PREMIOS_VALIDOS:
            raise ValueError(f"Premio inválido. Debe ser uno de: {', '.join(self.PREMIOS_VALIDOS)}")
        if not isinstance(self.monto_premio, (int, float)) or self.monto_premio < 0:
            raise ValueError("El monto del premio debe ser un número positivo.")
        if self.estado not in self.ESTADOS_VALIDOS:
            raise ValueError(f"Estado inválido. Debe ser uno de: {', '.join(self.ESTADOS_VALIDOS)}")

    def to_dict(self) -> dict:
        """Convierte el objeto a diccionario."""
        return {
            "id": self.id,
            "numero": self.numero,
            "serie": self.serie,
            "sorteo": self.sorteo,
            "fecha_sorteo": self.fecha_sorteo,
            "premio": self.premio,
            "monto_premio": self.monto_premio,
            "estado": self.estado,
            "fecha_registro": self.fecha_registro
        }

    @classmethod
    def from_dict(cls, datos: dict) -> "NumeroLoteria":
        """Crea una instancia desde un diccionario."""
        return cls(
            numero=datos["numero"],
            serie=datos["serie"],
            sorteo=datos["sorteo"],
            fecha_sorteo=datos["fecha_sorteo"],
            premio=datos["premio"],
            monto_premio=datos["monto_premio"],
            estado=datos.get("estado", "activo"),
            id=datos.get("id"),
            fecha_registro=datos.get("fecha_registro")
        )

    def __repr__(self):
        return (f"NumeroLoteria(id={self.id!r}, numero={self.numero!r}, "
                f"serie={self.serie!r}, sorteo={self.sorteo!r}, "
                f"premio={self.premio!r}, monto={self.monto_premio})")

    def __eq__(self, other):
        if not isinstance(other, NumeroLoteria):
            return False
        return self.id == other.id
