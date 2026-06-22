"""Punto de entrada principal del Sistema de Gestión de Lotería."""

import sys
import os

# Agregar el directorio raíz del proyecto al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.ui.menu_principal import MenuPrincipal


def main():
    """Función principal que inicia la aplicación."""
    print("Iniciando Sistema de Gestión de Resultados de Lotería...")
    menu = MenuPrincipal()
    menu.ejecutar()


if __name__ == "__main__":
    main()
