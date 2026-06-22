# 🎰 Sistema de Gestión de Resultados de Lotería

Sistema CRUD completo en Python para gestionar números y resultados de lotería, con documentación UML y pruebas unitarias.

## 📋 Descripción

Este proyecto implementa un sistema de gestión de resultados de lotería que permite registrar, consultar, actualizar y eliminar números de lotería. Desarrollado en Python con arquitectura en capas y persistencia en JSON.

## 🏗️ Arquitectura

El proyecto sigue una arquitectura en **3 capas**:

```
┌─────────────────────────────┐
│      UI (Consola)           │  ← Interfaz de usuario
├─────────────────────────────┤
│   Servicio (Lógica)         │  ← Lógica de negocio
├─────────────────────────────┤
│  Repositorio (Persistencia) │  ← Acceso a datos (JSON)
├─────────────────────────────┤
│      Modelo (Datos)         │  ← Entidades
└─────────────────────────────┘
```

## 📁 Estructura del Proyecto

```
loteria/
├── main.py                     # Punto de entrada
├── README.md                   # Este archivo
├── requirements.txt            # Dependencias
├── src/
│   ├── modelo/
│   │   └── numero_loteria.py   # Modelo de datos
│   ├── repositorio/
│   │   └── repositorio_loteria.py  # Persistencia JSON
│   ├── servicio/
│   │   └── servicio_loteria.py     # Lógica de negocio
│   └── ui/
│       └── menu_principal.py       # Interfaz de consola
├── tests/
│   ├── test_modelo.py          # Tests del modelo
│   ├── test_repositorio.py     # Tests del repositorio
│   └── test_servicio.py        # Tests del servicio
├── docs/
│   ├── casos_de_uso.md         # Documentación de CU
│   ├── diagramas_secuencia.md  # Documentación de DS
│   ├── cu_*.puml               # Diagramas de Casos de Uso
│   └── ds_*.puml               # Diagramas de Secuencia
└── data/
    └── loteria.json            # Datos (generado automáticamente)
```

## 🚀 Instalación y Ejecución

### Requisitos Previos

- Python 3.10 o superior

### Clonar el Repositorio

```bash
git clone <url-del-repositorio>
cd loteria
```

### Ejecutar la Aplicación

```bash
python main.py
```

### Ejecutar los Tests

```bash
# Con unittest
python -m unittest discover -s tests -v

# Con pytest (si está instalado)
python -m pytest tests/ -v
```

## 🎯 Casos de Uso

| CU   | Nombre                    | Descripción                                |
|------|---------------------------|--------------------------------------------|
| CU01 | Registrar número          | Registrar un nuevo resultado de lotería    |
| CU02 | Actualizar número         | Modificar datos de un resultado existente  |
| CU03 | Borrar número             | Eliminar un resultado de lotería           |
| CU04 | Listar números            | Consultar todos los resultados registrados |

Para más detalles, consulte:
- [Casos de Uso detallados](docs/casos_de_uso.md)
- [Diagramas de Secuencia](docs/diagramas_secuencia.md)

## 📊 Modelo de Datos

| Campo          | Tipo     | Descripción                                  |
|----------------|----------|----------------------------------------------|
| `id`           | `str`    | Identificador único (UUID)                   |
| `numero`       | `str`    | Número de lotería (4 dígitos)                |
| `serie`        | `str`    | Serie de la lotería                          |
| `sorteo`       | `str`    | Identificador del sorteo                     |
| `fecha_sorteo` | `str`    | Fecha del sorteo (YYYY-MM-DD)                |
| `premio`       | `str`    | Categoría: Mayor, Seco, Aproximación, Terminal, Otro |
| `monto_premio` | `float`  | Monto del premio                             |
| `estado`       | `str`    | Estado: activo / inactivo                    |
| `fecha_registro`| `str`   | Fecha/hora de registro (automático)          |

## 🧪 Tests

El proyecto incluye **30+ tests unitarios** organizados en 3 archivos:

- **test_modelo.py**: Validaciones del modelo de datos (18 tests)
- **test_repositorio.py**: Operaciones CRUD del repositorio (12 tests)
- **test_servicio.py**: Lógica de negocio del servicio (16 tests)

## 📐 Diagramas UML

Los diagramas están en formato PlantUML (`.puml`) en la carpeta `docs/`:

### Casos de Uso
- `cu_general.puml` - Diagrama general del sistema
- `cu_registrar.puml` - CU01: Registrar
- `cu_actualizar.puml` - CU02: Actualizar
- `cu_borrar.puml` - CU03: Borrar
- `cu_listar.puml` - CU04: Listar

### Diagramas de Secuencia
- `ds_registrar.puml` - DS01: Registrar
- `ds_actualizar.puml` - DS02: Actualizar
- `ds_borrar.puml` - DS03: Borrar
- `ds_listar.puml` - DS04: Listar

## 🛠️ Tecnologías

- **Python 3.10+** - Lenguaje de programación
- **JSON** - Formato de persistencia
- **unittest** - Framework de testing
- **PlantUML** - Diagramas UML
- **UUID** - Generación de identificadores únicos

## 📝 Licencia

Este proyecto fue desarrollado con fines académicos.
