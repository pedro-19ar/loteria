# Casos de Uso - Sistema de Gestión de Resultados de Lotería

## Índice

1. [CU01 - Registrar Número de Lotería](#cu01---registrar-número-de-lotería)
2. [CU02 - Actualizar Número de Lotería](#cu02---actualizar-número-de-lotería)
3. [CU03 - Borrar Número de Lotería](#cu03---borrar-número-de-lotería)
4. [CU04 - Listar Números de Lotería](#cu04---listar-números-de-lotería)

---

## CU01 - Registrar Número de Lotería

| Campo | Descripción |
|-------|-------------|
| **Identificador** | CU01 |
| **Nombre** | Registrar Número de Lotería |
| **Actor Principal** | Administrador |
| **Descripción** | Permite al administrador registrar un nuevo resultado de lotería en el sistema. |
| **Precondiciones** | El sistema está iniciado y muestra el menú principal. |
| **Postcondiciones** | El número de lotería queda almacenado en el sistema con un ID único. |

### Flujo Principal

1. El administrador selecciona la opción "Registrar número de lotería" del menú principal.
2. El sistema solicita los siguientes datos:
   - Número de lotería (4 dígitos)
   - Serie
   - Identificador del sorteo
   - Fecha del sorteo
   - Categoría del premio
   - Monto del premio
3. El administrador ingresa los datos solicitados.
4. El sistema valida los datos ingresados.
5. El sistema genera un ID único (UUID) y registra la fecha de registro.
6. El sistema almacena el nuevo registro en el archivo de datos.
7. El sistema muestra un mensaje de confirmación con los detalles del registro.

### Flujo Alternativo

**FA01 - Datos inválidos:**
- En el paso 4, si algún dato no cumple con las validaciones:
  - El sistema muestra un mensaje de error específico.
  - El sistema retorna al menú principal.

### Reglas de Negocio

| Regla | Descripción |
|-------|-------------|
| RN01 | El número debe contener exactamente 4 dígitos numéricos. |
| RN02 | La serie no puede estar vacía. |
| RN03 | El sorteo no puede estar vacío. |
| RN04 | La fecha del sorteo no puede estar vacía. |
| RN05 | El premio debe ser uno de: Mayor, Seco, Aproximación, Terminal, Otro. |
| RN06 | El monto del premio debe ser un número positivo o cero. |
| RN07 | El estado inicial es "activo" por defecto. |

---

## CU02 - Actualizar Número de Lotería

| Campo | Descripción |
|-------|-------------|
| **Identificador** | CU02 |
| **Nombre** | Actualizar Número de Lotería |
| **Actor Principal** | Administrador |
| **Descripción** | Permite al administrador modificar los datos de un resultado de lotería existente. |
| **Precondiciones** | Existe al menos un número de lotería registrado en el sistema. |
| **Postcondiciones** | Los datos del número de lotería quedan actualizados en el sistema. |

### Flujo Principal

1. El administrador selecciona la opción "Actualizar número de lotería" del menú principal.
2. El sistema muestra la lista de números de lotería registrados.
3. El administrador selecciona el número que desea actualizar.
4. El sistema muestra los datos actuales del número seleccionado.
5. El sistema solicita los nuevos datos (campos vacíos mantienen el valor actual).
6. El administrador ingresa los datos a modificar.
7. El sistema valida los nuevos datos.
8. El sistema actualiza el registro en el archivo de datos.
9. El sistema muestra un mensaje de confirmación con los datos actualizados.

### Flujo Alternativo

**FA01 - No hay registros:**
- En el paso 2, si no hay números registrados:
  - El sistema muestra el mensaje "No hay números registrados".
  - El sistema retorna al menú principal.

**FA02 - Índice fuera de rango:**
- En el paso 3, si el índice seleccionado es inválido:
  - El sistema muestra "Índice fuera de rango".
  - El sistema retorna al menú principal.

**FA03 - Datos inválidos:**
- En el paso 7, si algún dato no cumple con las validaciones:
  - El sistema muestra un mensaje de error específico.
  - El sistema retorna al menú principal.

**FA04 - Sin modificaciones:**
- En el paso 6, si el administrador no ingresa ningún dato nuevo:
  - El sistema muestra "No se modificaron datos".
  - El sistema retorna al menú principal.

### Reglas de Negocio

| Regla | Descripción |
|-------|-------------|
| RN01 | Solo se actualizan los campos que el usuario modifica. |
| RN02 | Las validaciones se aplican a todos los campos después de la actualización. |
| RN03 | Se pueden actualizar: número, serie, sorteo, fecha, premio, monto y estado. |

---

## CU03 - Borrar Número de Lotería

| Campo | Descripción |
|-------|-------------|
| **Identificador** | CU03 |
| **Nombre** | Borrar Número de Lotería |
| **Actor Principal** | Administrador |
| **Descripción** | Permite al administrador eliminar un resultado de lotería del sistema. |
| **Precondiciones** | Existe al menos un número de lotería registrado en el sistema. |
| **Postcondiciones** | El número de lotería queda eliminado del sistema de forma permanente. |

### Flujo Principal

1. El administrador selecciona la opción "Borrar número de lotería" del menú principal.
2. El sistema muestra la lista de números de lotería registrados.
3. El administrador selecciona el número que desea eliminar.
4. El sistema muestra los datos del número seleccionado.
5. El sistema solicita confirmación de eliminación.
6. El administrador confirma la eliminación.
7. El sistema elimina el registro del archivo de datos.
8. El sistema muestra un mensaje de confirmación.

### Flujo Alternativo

**FA01 - No hay registros:**
- En el paso 2, si no hay números registrados:
  - El sistema muestra "No hay números registrados".
  - El sistema retorna al menú principal.

**FA02 - Cancelar eliminación:**
- En el paso 6, si el administrador no confirma:
  - El sistema muestra "Operación cancelada".
  - El sistema retorna al menú principal.

**FA03 - Índice fuera de rango:**
- En el paso 3, si el índice seleccionado es inválido:
  - El sistema muestra "Índice fuera de rango".
  - El sistema retorna al menú principal.

### Reglas de Negocio

| Regla | Descripción |
|-------|-------------|
| RN01 | La eliminación es permanente y no se puede deshacer. |
| RN02 | Se requiere confirmación explícita del administrador. |
| RN03 | La eliminación de un registro no afecta a los demás registros. |

---

## CU04 - Listar Números de Lotería

| Campo | Descripción |
|-------|-------------|
| **Identificador** | CU04 |
| **Nombre** | Listar Números de Lotería |
| **Actor Principal** | Administrador |
| **Descripción** | Permite al administrador consultar todos los resultados de lotería registrados. |
| **Precondiciones** | El sistema está iniciado y muestra el menú principal. |
| **Postcondiciones** | El sistema muestra la información solicitada sin modificar datos. |

### Flujo Principal

1. El administrador selecciona la opción "Listar números de lotería" del menú principal.
2. El sistema consulta todos los registros almacenados.
3. El sistema muestra una tabla con la información de todos los números:
   - Índice, Número, Serie, Sorteo, Fecha, Premio, Monto, Estado.
4. El sistema muestra el total de registros encontrados.

### Flujo Alternativo

**FA01 - Sin registros:**
- En el paso 2, si no hay registros almacenados:
  - El sistema muestra "No hay números registrados".

### Reglas de Negocio

| Regla | Descripción |
|-------|-------------|
| RN01 | Se muestran todos los registros, tanto activos como inactivos. |
| RN02 | La consulta no modifica ningún dato del sistema. |
| RN03 | Los datos se muestran en formato de tabla para facilitar la lectura. |
