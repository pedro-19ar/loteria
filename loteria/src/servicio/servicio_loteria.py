"""Servicio de lógica de negocio para gestión de números de lotería."""

from typing import List, Optional

from src.modelo.numero_loteria import NumeroLoteria
from src.repositorio.repositorio_loteria import RepositorioLoteria


class ServicioLoteria:
    """Capa de servicio que gestiona la lógica de negocio de la lotería."""

    def __init__(self, repositorio: RepositorioLoteria = None):
        self.repositorio = repositorio or RepositorioLoteria()

    def registrar_numero(self, numero: str, serie: str, sorteo: str,
                         fecha_sorteo: str, premio: str,
                         monto_premio: float) -> NumeroLoteria:
        """
        CU01 - Registrar un nuevo número de lotería.

        Args:
            numero: Número de lotería (4 dígitos).
            serie: Serie de la lotería.
            sorteo: Identificador del sorteo.
            fecha_sorteo: Fecha del sorteo (YYYY-MM-DD).
            premio: Categoría del premio.
            monto_premio: Monto del premio.

        Returns:
            NumeroLoteria: El número registrado.

        Raises:
            ValueError: Si los datos son inválidos.
        """
        nuevo_numero = NumeroLoteria(
            numero=numero,
            serie=serie,
            sorteo=sorteo,
            fecha_sorteo=fecha_sorteo,
            premio=premio,
            monto_premio=monto_premio
        )
        return self.repositorio.crear(nuevo_numero)

    def actualizar_numero(self, id: str, **kwargs) -> NumeroLoteria:
        """
        CU02 - Actualizar un número de lotería existente.

        Args:
            id: Identificador del registro a actualizar.
            **kwargs: Campos a actualizar (numero, serie, sorteo,
                      fecha_sorteo, premio, monto_premio, estado).

        Returns:
            NumeroLoteria: El número actualizado.

        Raises:
            ValueError: Si el registro no existe o los datos son inválidos.
        """
        existente = self.repositorio.obtener_por_id(id)
        if existente is None:
            raise ValueError(f"No se encontró el número de lotería con ID: {id}")

        campos_actualizables = [
            "numero", "serie", "sorteo", "fecha_sorteo",
            "premio", "monto_premio", "estado"
        ]
        for campo, valor in kwargs.items():
            if campo in campos_actualizables:
                setattr(existente, campo, valor)

        existente.validar()
        return self.repositorio.actualizar(existente)

    def borrar_numero(self, id: str) -> bool:
        """
        CU03 - Borrar un número de lotería.

        Args:
            id: Identificador del registro a eliminar.

        Returns:
            bool: True si se eliminó correctamente.

        Raises:
            ValueError: Si el registro no existe.
        """
        existente = self.repositorio.obtener_por_id(id)
        if existente is None:
            raise ValueError(f"No se encontró el número de lotería con ID: {id}")
        return self.repositorio.eliminar(id)

    def listar_numeros(self) -> List[NumeroLoteria]:
        """
        CU04 - Listar todos los números de lotería.

        Returns:
            List[NumeroLoteria]: Lista de todos los números registrados.
        """
        return self.repositorio.obtener_todos()

    def obtener_numero(self, id: str) -> Optional[NumeroLoteria]:
        """
        Obtener un número de lotería por su ID.

        Args:
            id: Identificador del registro.

        Returns:
            Optional[NumeroLoteria]: El número encontrado o None.
        """
        return self.repositorio.obtener_por_id(id)

    def buscar_por_numero(self, numero: str) -> List[NumeroLoteria]:
        """
        Buscar números de lotería por su valor numérico.

        Args:
            numero: Número a buscar.

        Returns:
            List[NumeroLoteria]: Lista de coincidencias.
        """
        todos = self.repositorio.obtener_todos()
        return [n for n in todos if n.numero == numero]

    def buscar_por_sorteo(self, sorteo: str) -> List[NumeroLoteria]:
        """
        Buscar números de lotería por sorteo.

        Args:
            sorteo: Identificador del sorteo.

        Returns:
            List[NumeroLoteria]: Lista de coincidencias.
        """
        todos = self.repositorio.obtener_todos()
        return [n for n in todos if n.sorteo == sorteo]
