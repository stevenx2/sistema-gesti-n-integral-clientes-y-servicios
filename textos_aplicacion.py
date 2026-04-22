
"""
clase de recursos de textos usados en la aplicación. Permite que el código principal esté más ordenado
"""


class RecursosTexto:
    PEDIR_NOMBRE_SERVICIO = """Ingrese el nombre del servicio (no puede estar vacío):"""
    PEDIR_HORAS_RESERVA_SALA = """Ingrese la cantidad de horas de reserva de la sala:"""
    PEDIR_NOMBRE_EQUIPO_A_ALQUILAR = """Ingrese el nombre del equipo que se va a alquilar (no puede estar vacío):"""
    PEDIR_CANTIDAD_EQUIPOS_A_ALQUILAR = """Ingrese la cantidad de equipos que se van a incluir en el servicio de alquiler (1-100):"""
    PEDIR_CANTIDAD_DIAS_ALQUILER = """Ingrese la cantidad de días de alquiler del equipo:"""
    PEDIR_PORCENTAJE_IMPUESTOS = """Ingrese el porcentaje de impuestos a aplicar al servicio (solo el número, sin %):"""
    PEDIR_ESPECIALIDAD_ASESORIA = """Ingrese la especialidad de la asesoría (no puede estar vacía):"""
    PEDIR_HORAS_ASESORIA = """Ingrese la cantidad de horas de la asesoría:"""
    MENSAJE_ERROR_URGENCIA_SERVICIO_INVALIDA = """\nOpción inválida. Ingrese 'S' para sí o 'N' para no."""
    PEDIR_NOMBRE_CLIENTE = """Ingrese el nombre del cliente:"""
    PEDIR_TELEFONO_CLIENTE = """Ingrese el teléfono del cliente (solo números, sin espacios ni símbolos, 10 dígitos):"""
    PEDIR_EMAIL_CLIENTE = """Ingrese el correo electrónico del cliente:"""
    MENSAJE_CLIENTE_REGISTRADO = """\nCliente registrado correctamente."""
    PEDIR_URGENCIA_SERVICIO = """¿La asesoría es de urgencia? (S/N):"""
    MENSAJE_SERVICIO_REGISTRADO = """\nServicio registrado correctamente."""
    MENSAJE_ERROR_OPCION_NO_VALIDA_MENU_INICIAL = """\nOpción inválida. Por favor seleccione un número entre 1 y 11."""
    MENSAJE_ERROR_OPCION_SERVICIO_NO_VALIDA= """\nOpción inválida. Seleccione un tipo de servicio entre 1 y 3."""
    MENSAJE_LISTADO_SERVICIOS_VACIO = """\nNo hay servicios registrados."""
    MENSAJE_LISTADO_CLIENTES_SERVICIOS_VACIO_CREAR_RESERVA = """\nNo se puede crear una reserva sin clientes y servicios registrados."""
    MENSAJE_ERROR_SELECCIONAR_CLIENTE = """\nError: el número ingresado no corresponde a ningún cliente del listado."""
    PEDIR_SELECCION_CLIENTE = """Ingrese el número del cliente que realizará la reserva según el listado mostrado:"""
    MENSAJE_ERROR_SELECCION_SERVICIO = """\nError: el número ingresado no corresponde a ningún servicio del listado."""
    PEDIR_SELECCION_SERVICIO = """Seleccione el servicio que desea asociar a la reserva:"""
    MENSAJE_RESERVA_REGISTRADA = """\nReserva registrada correctamente."""
    MENSAJE_ERROR_SELECCION_RESERVA = """\nError: el número ingresado no corresponde a ninguna reserva del listado."""
    PEDIR_SELECCION_RESERVA = """Seleccione la reserva que desea procesar:"""
    MENSAJE_RESERVA_PROCESADA = """\nReserva procesada correctamente."""
    MENSAJE_ERROR_PROCESAR_RESERVA = """\nError al procesar la reserva."""
    MENSAJE_LISTA_RESERVAS_VACIA = """\nNo hay reservas registradas."""
    PEDIR_SELECCION_RESERVA_A_CANCELAR = """Seleccione la reserva que desea cancelar:"""
    MENSAJE_RESERVA_CANCELADA = """\nReserva cancelada correctamente."""
    MENSAJE_ERROR_CANCELAR_RESERVA = """\nError al cancelar la reserva."""
    PEDIR_SERVICIO_A_HABILITAR = """Seleccione el servicio que desea habilitar:"""
    PEDIR_SERVICIO_A_DESHABILITAR = """Seleccione el servicio que desea deshabilitar:"""
    MENSAJE_SERVICIO_DESHABILITADO = """\nServicio deshabilitado correctamente."""
    MENSAJE_SERVICIO_HABILITADO = """\nServicio habilitado correctamente."""
    MENSAJE_LISTADO_CLIENTES_VACIO = """\nNo hay clientes registrados."""

    TITULO_DESHABILITAR_SERVICIO = """\n========================================
DESHABILITAR SERVICIO
========================================"""


    TITULO_HABILITAR_SERVICIO = """\n========================================
HABILITAR SERVICIO
========================================"""


    TITULO_LISTADO_CLIENTES = """\n========================================
LISTADO DE CLIENTES
========================================"""

    TITULO_LISTADO_RESERVAS = """\n========================================
LISTADO DE RESERVAS
========================================"""


    TITULO_CANCELACION_RESERVA = """\n========================================
CANCELACIÓN DE RESERVA
========================================"""

    TITULO_PROCESAMIENTO_RESERVA = """\n========================================
PROCESAMIENTO DE RESERVA
========================================"""


    MENSAJE_SELECCION_SERVICIO = """\n========================================
SELECCIÓN DE SERVICIO
========================================"""



    MENSAJE_SELECCION_CLIENTE = """\n========================================
SELECCIÓN DE CLIENTE
========================================"""


    TITULO_LISTADO_SERVICIOS = """\n========================================
LISTADO DE SERVICIOS
========================================"""

    MENSAJE_OPCIONES_SERVICIO = """\n========================================
TIPOS DE SERVICIO DISPONIBLES
========================================

1.Precio base: $50.000 - Servicio de reserva de sala
2.Precio base: $80.000 - Servicio de alquiler de equipo
3.Precio base: $60.000 - Servicio de asesoría
4.volver al menú inicial

----------------------------------------
NOTA: El precio final puede incrementarse según la duración, cantidad de recursos utilizados u otros parámetros
que se solicitarán durante el proceso.
========================================
Seleccione el tipo de servicio:"""


    MENSAJE_MENU_INICIAL = """\n========================================
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
9. habilitar servicio
10. deshabilitar servicio
11. Salir
========================================
Seleccione una opción:"""







    def obtener_mensaje_descuento_sala(self,costo):
        return f"""\nActualmente su servicio tiene un valor de ${costo}.
Ingrese el valor total en dinero que desea aplicar como descuento.
Nota: El valor debe ser un monto fijo, no un porcentaje.
:"""
