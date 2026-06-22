"""Repositorio para persistencia de números de lotería en archivo JSON."""

import json
import os
from typing import List, Optional

from src.modelo.numero_loteria import NumeroLoteria


class RepositorioLoteria:
    """Gestiona la persistencia de números de lotería en un archivo JSON."""

    def __init__(self, ruta_archivo: str = None):
        if ruta_archivo is None:
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(
                os.path.abspath(__file__))))
            ruta_archivo = os.path.join(base_dir, "data", "loteria.json")
        self.ruta_archivo = ruta_archivo
        self._asegurar_archivo()

    def _asegurar_archivo(self):
        """Crea el archivo y directorios si no existen."""
        directorio = os.path.dirname(self.ruta_archivo)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio, exist_ok=True)
        if not os.path.exists(self.ruta_archivo):
            self._guardar_todos([])

    def _cargar_todos(self) -> List[dict]:
        """Carga todos los registros del archivo JSON."""
        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def _guardar_todos(self, datos: List[dict]):
        """Guarda todos los registros en el archivo JSON."""
        with open(self.ruta_archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=2, ensure_ascii=False)

    def crear(self, numero: NumeroLoteria) -> NumeroLoteria:
        """Registra un nuevo número de lotería."""
        datos = self._cargar_todos()
        # Verificar duplicados por ID
        for registro in datos:
            if registro["id"] == numero.id:
                raise ValueError(f"Ya existe un registro con ID: {numero.id}")
        datos.append(numero.to_dict())
        self._guardar_todos(datos)
        return numero

    def obtener_por_id(self, id: str) -> Optional[NumeroLoteria]:
        """Obtiene un número de lotería por su ID."""
        datos = self._cargar_todos()
        for registro in datos:
            if registro["id"] == id:
                return NumeroLoteria.from_dict(registro)
        return None

    def obtener_todos(self) -> List[NumeroLoteria]:
        """Obtiene todos los números de lotería."""
        datos = self._cargar_todos()
        return [NumeroLoteria.from_dict(d) for d in datos]

    def actualizar(self, numero: NumeroLoteria) -> NumeroLoteria:
        """Actualiza un número de lotería existente."""
        datos = self._cargar_todos()
        for i, registro in enumerate(datos):
            if registro["id"] == numero.id:
                datos[i] = numero.to_dict()
                self._guardar_todos(datos)
                return numero
        raise ValueError(f"No se encontró el registro con ID: {numero.id}")

    def eliminar(self, id: str) -> bool:
        """Elimina un número de lotería por su ID."""
        datos = self._cargar_todos()
        datos_filtrados = [d for d in datos if d["id"] != id]
        if len(datos_filtrados) == len(datos):
            raise ValueError(f"No se encontró el registro con ID: {id}")
        self._guardar_todos(datos_filtrados)
        return True

    def eliminar_todos(self):
        """Elimina todos los registros."""
        self._guardar_todos([])

    def contar(self) -> int:
        """Retorna la cantidad de registros."""
        return len(self._cargar_todos())
