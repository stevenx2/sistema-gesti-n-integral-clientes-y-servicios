# 📌 Sistema Integral de Gestión - Software FJ

## 📖 Descripción

Este proyecto consiste en una aplicación de consola desarrollada en Python que permite gestionar clientes, servicios y reservas para la empresa **Software FJ**.

El sistema está diseñado bajo el paradigma de programación orientada a objetos (POO) y no utiliza bases de datos. Toda la información se maneja mediante estructuras en memoria (listas) y archivos de texto para el registro de logs.

---

## 🎯 Objetivo

Implementar un sistema robusto que demuestre el uso de:

* Abstracción
* Herencia
* Polimorfismo
* Encapsulación
* Manejo avanzado de excepciones

Garantizando que la aplicación continúe funcionando incluso ante errores.

---

## ⚙️ Tecnologías utilizadas

* Python 3
* Programación orientada a objetos
* Manejo de archivos (`logs.txt`)

---

## ▶️ Ejecución del programa

Ubícate en la carpeta del proyecto y ejecuta:

```bash
python main.py
```

Opcionalmente, puedes activar datos de prueba modificando:

```python
app = Aplicacion(datos_iniciales=True)
```

---

## 🧱 Arquitectura del sistema

### Clases principales

* `Cliente`: Maneja la información de los clientes con validaciones estrictas.
* `Servicio` (abstracta): Define la estructura base de los servicios.

Subclases de `Servicio`:

* `ServicioReservaSala`

* `ServicioAlquilerEquipo`

* `ServicioAsesoria`

* `Reserva`: Gestiona la relación entre cliente y servicio.

* `Aplicacion`: Controla el flujo del sistema.

---

## 🧠 Programación Orientada a Objetos

### ✔ Abstracción

Uso de la clase abstracta `Servicio` con métodos obligatorios:

* `calcular_costo`
* `validar_parametros`
* `describir_servicio`

### ✔ Herencia

Tres tipos de servicios heredan de `Servicio`.

### ✔ Polimorfismo

Cada servicio implementa su propia lógica de cálculo.

### ✔ Encapsulación

Uso de atributos protegidos (`_nombre`, `_email`, etc.) y acceso mediante métodos.

---

## ⚠️ Manejo de excepciones

El sistema implementa excepciones personalizadas:

* `ErrorSistema`
* `ErrorValidacion`
* `ErrorServicioNoDisponible`

Se utilizan estructuras como:

* `try / except`
* `try / except / else`
* `try / except / finally`

✔ Los errores no detienen la ejecución del sistema.

---

## 🪵 Sistema de logs

Todos los errores y eventos importantes se registran en:

```
logs.txt
```

Ejemplos de registros:

* Errores de validación
* Reservas procesadas
* Cancelaciones
* Intentos fallidos

---

## 🖥️ Uso del sistema

### 📋 Menú principal

```text
========================================
SISTEMA SOFTWARE FJ - MENÚ PRINCIPAL
====================================
1. Crear cliente
2. Crear servicio
3. Listar servicios
4. Crear reserva
5. Procesar reserva
6. Cancelar reserva
7. Mostrar reservas
8. Listar clientes
9. Habilitar servicio
10. Deshabilitar servicio
11. Salir
========================================
Seleccione una opción:
```

---

### 👤 1. Crear cliente

Permite registrar un cliente solicitando:

* Nombre (solo letras)
* Email (debe contener `@` y `.`)
* Teléfono (10 dígitos numéricos)

✔ El sistema valida los datos antes de crear el cliente.

---

### 🛠️ 2. Crear servicio

Permite elegir el tipo de servicio:

```text
========================================
TIPOS DE SERVICIO DISPONIBLES
========================================

1. Precio base: $50.000 - Servicio de reserva de sala
2. Precio base: $80.000 - Servicio de alquiler de equipo
3. Precio base: $60.000 - Servicio de asesoría
4. Volver al menú inicial

----------------------------------------
NOTA: El precio final puede variar según los parámetros ingresados.
========================================
Seleccione el tipo de servicio:
```

#### Tipos de servicios:

**Reserva de sala**

* Horas
* Descuento (valor fijo)

**Alquiler de equipo**

* Tipo de equipo
* Cantidad (1–100)
* Días
* Impuestos (%)

**Asesoría**

* Especialidad
* Horas
* Urgencia (incrementa el costo)

---

### 📄 3. Listar servicios

Muestra todos los servicios registrados junto con su descripción.

---

### 📅 4. Crear reserva

* Selecciona un cliente
* Selecciona un servicio

✔ Solo se puede crear si existen clientes y servicios.

---

### ⚙️ 5. Procesar reserva

* Calcula el costo final
* Cambia el estado a **confirmada**

✔ Si ocurre un error (por ejemplo, servicio deshabilitado), la reserva se marca como fallida.

---

### ❌ 6. Cancelar reserva

* Solo se pueden cancelar reservas previamente **confirmadas**

---

### 📊 7. Mostrar reservas

Lista todas las reservas con:

* Cliente
* Servicio
* Estado
* Costo

---

### 📋 8. Listar clientes

Muestra todos los clientes registrados.

---

### 🔓 9. Habilitar servicio

Permite activar un servicio previamente deshabilitado.

---

### 🔒 10. Deshabilitar servicio

Impide que un servicio pueda ser procesado.

---

### 🚪 11. Salir

Finaliza la ejecución del programa.

---

## 🔄 Estados de una reserva

* `pendiente`
* `confirmada`
* `cancelada`
* `fallido`

---

## ✅ Características destacadas

* ✔ Sistema funcional sin base de datos
* ✔ Manejo robusto de excepciones
* ✔ Validaciones estrictas
* ✔ Uso correcto de POO
* ✔ Registro de eventos en archivo
* ✔ Interfaz de consola estructurada

---

## 👤 Autores

* Johan Steven Mendoza Ruiz
* Theo Junior Pérez Herrera
* Dayana Ramos Tapias
* Anyis Paola Teran Rodrigez

---

## 📌 Notas finales

El sistema está diseñado para simular un entorno real de gestión, manejando errores de forma controlada y permitiendo la continuidad de la ejecución sin interrupciones.
