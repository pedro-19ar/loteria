"""Interfaz de usuario por consola para gestión de lotería."""

import os
import sys

from src.servicio.servicio_loteria import ServicioLoteria
from src.modelo.numero_loteria import NumeroLoteria


class MenuPrincipal:
    """Menú interactivo de consola para gestionar números de lotería."""

    def __init__(self, servicio: ServicioLoteria = None):
        self.servicio = servicio or ServicioLoteria()

    def limpiar_pantalla(self):
        """Limpia la pantalla de la consola."""
        os.system("cls" if os.name == "nt" else "clear")

    def mostrar_encabezado(self):
        """Muestra el encabezado del sistema."""
        print("=" * 60)
        print("   SISTEMA DE GESTION DE RESULTADOS DE LOTERIA")
        print("=" * 60)

    def mostrar_menu(self):
        """Muestra el menú principal."""
        print("\nMENU PRINCIPAL")
        print("-" * 40)
        print("  1. Registrar numero de loteria")
        print("  2. Actualizar numero de loteria")
        print("  3. Borrar numero de loteria")
        print("  4. Listar numeros de loteria")
        print("  5. Buscar por numero")
        print("  6. Salir")
        print("-" * 40)

    def leer_opcion(self) -> str:
        """Lee la opción del usuario."""
        return input("\nSeleccione una opcion: ").strip()

    def pausar(self):
        """Pausa la ejecución hasta que el usuario presione Enter."""
        input("\nPresione Enter para continuar...")

    def mostrar_numero(self, numero: NumeroLoteria):
        """Muestra los detalles de un número de lotería."""
        print(f"\n  ID:             {numero.id}")
        print(f"  Numero:         {numero.numero}")
        print(f"  Serie:          {numero.serie}")
        print(f"  Sorteo:         {numero.sorteo}")
        print(f"  Fecha Sorteo:   {numero.fecha_sorteo}")
        print(f"  Premio:         {numero.premio}")
        print(f"  Monto Premio:   ${numero.monto_premio:,.2f}")
        print(f"  Estado:         {numero.estado}")
        print(f"  Fecha Registro: {numero.fecha_registro}")

    def registrar_numero(self):
        """CU01 - Registrar un nuevo número de lotería."""
        print("\n" + "=" * 50)
        print("   REGISTRAR NUMERO DE LOTERIA")
        print("=" * 50)

        try:
            numero = input("  Numero (4 digitos): ").strip()
            serie = input("  Serie: ").strip()
            sorteo = input("  Sorteo (ej: S-2026-001): ").strip()
            fecha_sorteo = input("  Fecha del sorteo (YYYY-MM-DD): ").strip()

            print(f"\n  Premios validos: {', '.join(NumeroLoteria.PREMIOS_VALIDOS)}")
            premio = input("  Premio: ").strip()

            monto_str = input("  Monto del premio: ").strip()
            monto_premio = float(monto_str)

            resultado = self.servicio.registrar_numero(
                numero=numero,
                serie=serie,
                sorteo=sorteo,
                fecha_sorteo=fecha_sorteo,
                premio=premio,
                monto_premio=monto_premio
            )

            print("\n  Numero registrado exitosamente!")
            self.mostrar_numero(resultado)

        except ValueError as e:
            print(f"\n  Error de validacion: {e}")
        except Exception as e:
            print(f"\n  Error inesperado: {e}")

    def actualizar_numero(self):
        """CU02 - Actualizar un número de lotería."""
        print("\n" + "=" * 50)
        print("   ACTUALIZAR NUMERO DE LOTERIA")
        print("=" * 50)

        try:
            numeros = self.servicio.listar_numeros()
            if not numeros:
                print("\n  No hay numeros registrados.")
                return

            print("\n  Numeros disponibles:")
            for i, n in enumerate(numeros, 1):
                print(f"    {i}. [{n.numero}] Serie: {n.serie} - Sorteo: {n.sorteo} (ID: {n.id[:8]}...)")

            seleccion = input("\n  Seleccione el numero a actualizar (indice): ").strip()
            idx = int(seleccion) - 1

            if idx < 0 or idx >= len(numeros):
                print("\n  Indice fuera de rango.")
                return

            numero_actual = numeros[idx]
            print(f"\n  Datos actuales:")
            self.mostrar_numero(numero_actual)

            print("\n  Ingrese los nuevos datos (deje vacio para mantener el actual):")

            campos = {}
            nuevo_numero = input(f"  Numero [{numero_actual.numero}]: ").strip()
            if nuevo_numero:
                campos["numero"] = nuevo_numero

            nueva_serie = input(f"  Serie [{numero_actual.serie}]: ").strip()
            if nueva_serie:
                campos["serie"] = nueva_serie

            nuevo_sorteo = input(f"  Sorteo [{numero_actual.sorteo}]: ").strip()
            if nuevo_sorteo:
                campos["sorteo"] = nuevo_sorteo

            nueva_fecha = input(f"  Fecha sorteo [{numero_actual.fecha_sorteo}]: ").strip()
            if nueva_fecha:
                campos["fecha_sorteo"] = nueva_fecha

            print(f"  Premios validos: {', '.join(NumeroLoteria.PREMIOS_VALIDOS)}")
            nuevo_premio = input(f"  Premio [{numero_actual.premio}]: ").strip()
            if nuevo_premio:
                campos["premio"] = nuevo_premio

            nuevo_monto = input(f"  Monto [{numero_actual.monto_premio}]: ").strip()
            if nuevo_monto:
                campos["monto_premio"] = float(nuevo_monto)

            nuevo_estado = input(f"  Estado [{numero_actual.estado}] (activo/inactivo): ").strip()
            if nuevo_estado:
                campos["estado"] = nuevo_estado

            if not campos:
                print("\n  No se modificaron datos.")
                return

            resultado = self.servicio.actualizar_numero(numero_actual.id, **campos)
            print("\n  Numero actualizado exitosamente!")
            self.mostrar_numero(resultado)

        except ValueError as e:
            print(f"\n  Error de validacion: {e}")
        except Exception as e:
            print(f"\n  Error inesperado: {e}")

    def borrar_numero(self):
        """CU03 - Borrar un número de lotería."""
        print("\n" + "=" * 50)
        print("   BORRAR NUMERO DE LOTERIA")
        print("=" * 50)

        try:
            numeros = self.servicio.listar_numeros()
            if not numeros:
                print("\n  No hay numeros registrados.")
                return

            print("\n  Numeros disponibles:")
            for i, n in enumerate(numeros, 1):
                print(f"    {i}. [{n.numero}] Serie: {n.serie} - Sorteo: {n.sorteo} (ID: {n.id[:8]}...)")

            seleccion = input("\n  Seleccione el numero a borrar (indice): ").strip()
            idx = int(seleccion) - 1

            if idx < 0 or idx >= len(numeros):
                print("\n  Indice fuera de rango.")
                return

            numero_a_borrar = numeros[idx]
            print(f"\n  Se eliminara:")
            self.mostrar_numero(numero_a_borrar)

            confirmacion = input("\n  Esta seguro? (s/n): ").strip().lower()
            if confirmacion == "s":
                self.servicio.borrar_numero(numero_a_borrar.id)
                print("\n  Numero eliminado exitosamente!")
            else:
                print("\n  Operacion cancelada.")

        except ValueError as e:
            print(f"\n  Error: {e}")
        except Exception as e:
            print(f"\n  Error inesperado: {e}")

    def listar_numeros(self):
        """CU04 - Listar todos los números de lotería."""
        print("\n" + "=" * 50)
        print("   LISTADO DE NUMEROS DE LOTERIA")
        print("=" * 50)

        numeros = self.servicio.listar_numeros()
        if not numeros:
            print("\n  No hay numeros registrados.")
            return

        print(f"\n  Total de registros: {len(numeros)}\n")
        print(f"  {'#':<4} {'Numero':<8} {'Serie':<6} {'Sorteo':<14} {'Fecha':<12} {'Premio':<14} {'Monto':>12} {'Estado':<10}")
        print("  " + "-" * 84)

        for i, n in enumerate(numeros, 1):
            print(f"  {i:<4} {n.numero:<8} {n.serie:<6} {n.sorteo:<14} {n.fecha_sorteo:<12} {n.premio:<14} ${n.monto_premio:>10,.2f} {n.estado:<10}")

    def buscar_por_numero(self):
        """Buscar números de lotería por valor."""
        print("\n" + "=" * 50)
        print("   BUSCAR POR NUMERO")
        print("=" * 50)

        numero = input("  Ingrese el numero a buscar: ").strip()
        resultados = self.servicio.buscar_por_numero(numero)

        if not resultados:
            print(f"\n  No se encontraron resultados para '{numero}'.")
            return

        print(f"\n  Se encontraron {len(resultados)} resultado(s):")
        for r in resultados:
            self.mostrar_numero(r)
            print("  " + "-" * 40)

    def ejecutar(self):
        """Bucle principal del menú."""
        while True:
            self.limpiar_pantalla()
            self.mostrar_encabezado()
            self.mostrar_menu()
            opcion = self.leer_opcion()

            if opcion == "1":
                self.registrar_numero()
                self.pausar()
            elif opcion == "2":
                self.actualizar_numero()
                self.pausar()
            elif opcion == "3":
                self.borrar_numero()
                self.pausar()
            elif opcion == "4":
                self.listar_numeros()
                self.pausar()
            elif opcion == "5":
                self.buscar_por_numero()
                self.pausar()
            elif opcion == "6":
                print("\n  Hasta luego! Gracias por usar el sistema.")
                sys.exit(0)
            else:
                print("\n  Opcion no valida. Intente de nuevo.")
                self.pausar()
