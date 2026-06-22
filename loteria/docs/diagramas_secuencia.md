# Diagramas de Secuencia - Sistema de Gestión de Resultados de Lotería

## Índice

1. [DS01 - Registrar Número de Lotería](#ds01---registrar-número-de-lotería)
2. [DS02 - Actualizar Número de Lotería](#ds02---actualizar-número-de-lotería)
3. [DS03 - Borrar Número de Lotería](#ds03---borrar-número-de-lotería)
4. [DS04 - Listar Números de Lotería](#ds04---listar-números-de-lotería)

---

## Participantes del Sistema

| Participante | Estereotipo | Descripción |
|---|---|---|
| Administrador | Actor | Usuario que gestiona los resultados de lotería |
| MenuPrincipal | Boundary | Interfaz de consola que interactúa con el usuario |
| ServicioLoteria | Control | Capa de lógica de negocio que procesa las operaciones |
| NumeroLoteria | Entity | Modelo de datos que representa un resultado de lotería |
| RepositorioLoteria | Entity | Capa de persistencia que gestiona el almacenamiento |
| loteria.json | Database | Archivo de almacenamiento de datos en formato JSON |

---

## DS01 - Registrar Número de Lotería

**Archivo PlantUML:** `ds_registrar.puml`

**Descripción:** Este diagrama muestra la secuencia de interacciones que ocurren cuando el administrador registra un nuevo número de lotería en el sistema.

### Flujo de Mensajes

| # | Origen | Destino | Mensaje |
|---|--------|---------|---------|
| 1 | Administrador | MenuPrincipal | Selecciona opción "1" |
| 2 | MenuPrincipal | Administrador | Solicita datos (número, serie, sorteo, fecha, premio, monto) |
| 3 | Administrador | MenuPrincipal | Ingresa datos |
| 4 | MenuPrincipal | ServicioLoteria | `registrar_numero(datos)` |
| 5 | ServicioLoteria | NumeroLoteria | `new NumeroLoteria(datos)` |
| 6 | NumeroLoteria | NumeroLoteria | `validar()` |
| 7 | ServicioLoteria | RepositorioLoteria | `crear(numero_loteria)` |
| 8 | RepositorioLoteria | loteria.json | Leer → Agregar → Guardar |
| 9 | RepositorioLoteria | ServicioLoteria | `numero_registrado` |
| 10 | ServicioLoteria | MenuPrincipal | `numero_registrado` |
| 11 | MenuPrincipal | Administrador | Muestra confirmación y detalles |

---

## DS02 - Actualizar Número de Lotería

**Archivo PlantUML:** `ds_actualizar.puml`

**Descripción:** Este diagrama muestra la secuencia de interacciones que ocurren cuando el administrador actualiza un número de lotería existente.

### Flujo de Mensajes

| # | Origen | Destino | Mensaje |
|---|--------|---------|---------|
| 1 | Administrador | MenuPrincipal | Selecciona opción "2" |
| 2 | MenuPrincipal | ServicioLoteria | `listar_numeros()` |
| 3 | ServicioLoteria | RepositorioLoteria | `obtener_todos()` |
| 4 | RepositorioLoteria | loteria.json | Leer archivo |
| 5 | MenuPrincipal | Administrador | Muestra lista de números |
| 6 | Administrador | MenuPrincipal | Selecciona número e ingresa nuevos datos |
| 7 | MenuPrincipal | ServicioLoteria | `actualizar_numero(id, datos)` |
| 8 | ServicioLoteria | RepositorioLoteria | `obtener_por_id(id)` |
| 9 | ServicioLoteria | NumeroLoteria | `setattr()` + `validar()` |
| 10 | ServicioLoteria | RepositorioLoteria | `actualizar(numero)` |
| 11 | RepositorioLoteria | loteria.json | Leer → Actualizar → Guardar |
| 12 | MenuPrincipal | Administrador | Muestra confirmación y datos actualizados |

---

## DS03 - Borrar Número de Lotería

**Archivo PlantUML:** `ds_borrar.puml`

**Descripción:** Este diagrama muestra la secuencia de interacciones que ocurren cuando el administrador elimina un número de lotería del sistema.

### Flujo de Mensajes

| # | Origen | Destino | Mensaje |
|---|--------|---------|---------|
| 1 | Administrador | MenuPrincipal | Selecciona opción "3" |
| 2 | MenuPrincipal | ServicioLoteria | `listar_numeros()` |
| 3 | ServicioLoteria | RepositorioLoteria | `obtener_todos()` |
| 4 | RepositorioLoteria | loteria.json | Leer archivo |
| 5 | MenuPrincipal | Administrador | Muestra lista de números |
| 6 | Administrador | MenuPrincipal | Selecciona número a borrar |
| 7 | MenuPrincipal | Administrador | Solicita confirmación |
| 8 | Administrador | MenuPrincipal | Confirma ("s") |
| 9 | MenuPrincipal | ServicioLoteria | `borrar_numero(id)` |
| 10 | ServicioLoteria | RepositorioLoteria | `obtener_por_id(id)` |
| 11 | ServicioLoteria | RepositorioLoteria | `eliminar(id)` |
| 12 | RepositorioLoteria | loteria.json | Leer → Filtrar → Guardar |
| 13 | MenuPrincipal | Administrador | Muestra confirmación de eliminación |

---

## DS04 - Listar Números de Lotería

**Archivo PlantUML:** `ds_listar.puml`

**Descripción:** Este diagrama muestra la secuencia de interacciones que ocurren cuando el administrador consulta todos los números de lotería registrados.

### Flujo de Mensajes

| # | Origen | Destino | Mensaje |
|---|--------|---------|---------|
| 1 | Administrador | MenuPrincipal | Selecciona opción "4" |
| 2 | MenuPrincipal | ServicioLoteria | `listar_numeros()` |
| 3 | ServicioLoteria | RepositorioLoteria | `obtener_todos()` |
| 4 | RepositorioLoteria | loteria.json | Leer archivo |
| 5 | RepositorioLoteria | RepositorioLoteria | Convertir dict[] a NumeroLoteria[] |
| 6 | ServicioLoteria | MenuPrincipal | `List[NumeroLoteria]` |
| 7 | MenuPrincipal | Administrador | Muestra tabla con todos los registros |

---

## Archivos PlantUML

Para generar las imágenes de los diagramas, utilice PlantUML con los siguientes archivos:

| Archivo | Diagrama |
|---------|----------|
| `cu_general.puml` | Diagrama General de Casos de Uso |
| `cu_registrar.puml` | CU01 - Registrar (Caso de Uso) |
| `cu_actualizar.puml` | CU02 - Actualizar (Caso de Uso) |
| `cu_borrar.puml` | CU03 - Borrar (Caso de Uso) |
| `cu_listar.puml` | CU04 - Listar (Caso de Uso) |
| `ds_registrar.puml` | DS01 - Registrar (Secuencia) |
| `ds_actualizar.puml` | DS02 - Actualizar (Secuencia) |
| `ds_borrar.puml` | DS03 - Borrar (Secuencia) |
| `ds_listar.puml` | DS04 - Listar (Secuencia) |

### Comando para generar imágenes

```bash
# Instalar PlantUML (requiere Java)
# Generar todos los diagramas como PNG
java -jar plantuml.jar docs/*.puml
```
