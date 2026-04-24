from abc import ABC,abstractmethod
from errores import ErrorSistema
from errores import ErrorServicioNoDisponible
from errores import ErrorValidacion

"""
clase abstracta que representa a todos los servicios.
"""

class Servicio(ABC):

    def __init__(self,nombre:str,precio_base):
        self.validar_nombre_servicio(nombre)
        self.disponibilidad = True
        self.precio = precio_base


    def validar_nombre_servicio(self,nombre):
        if not nombre or not nombre.strip():
            raise ErrorValidacion(f"error en {self.__class__.__name__}:El nombre del servicio no puede estar vacío")

        self.nombre = nombre.strip()

    def validar_disponibilidad(self):
        if not self.disponibilidad:
            raise ErrorServicioNoDisponible(f"error en {self.__class__.__name__}:El servicio no está disponible")

    def activar(self):
        self.disponibilidad = True

    def desactivar(self):
        self.disponibilidad = False


    """
    corresponde a la sobrecarga de métodos, cada servicio implementará su propia lógica de cálculo de costo
    y validación de parámetros.
    """

    @abstractmethod
    def calcular_costo(self, *argumentos,**argumentos_nombrados):
        pass

    @abstractmethod
    def validar_parametros(self, *argumentos,**argumentos_nombrados):
        pass

    @abstractmethod
    def descripcion_servicio(self):
        pass




"""
implementacion de los 3 servicios, cada uno con su propia lógica de cálculo de costo y validación de parámetros.
cada servicio tiene su propia descripción que se muestra al listar los servicios disponibles.

"""

class ServicioReservaSala(Servicio):

    def __init__(self, nombre, precio_por_hora=50000):
        super().__init__(nombre, precio_por_hora)
        self._horas_reserva = 0
        self._descuento = 0
        self._costo_calculado = None


    def validar_parametros(self, horas: int):
        if not isinstance(horas, int) or horas <= 0:
            raise ErrorValidacion("Las horas de reserva deben ser un número entero positivo.")
        self._horas_reserva = horas


    def calcular_costo(self, horas, descuento: float = 0.0) -> float:
        self.validar_disponibilidad()
        self.validar_parametros(horas)

        if not isinstance(descuento, (int, float)) or descuento < 0:
            raise ErrorValidacion("El descuento debe ser un número no negativo. ")

        self._descuento = descuento
        costo_base = self._horas_reserva * self.precio
        costo_final = max(0, costo_base - self._descuento)
        self._costo_calculado = costo_final
        return costo_final






    def descripcion_servicio(self) -> str:
       descripcion_base = f"--- Servicio de Reserva de Sala ---\n" \
                           f"  Nombre: {self.nombre}\n" \
                           f"  Precio por hora: ${self.precio:.2f}\n" \
                           f"  Disponibilidad: {'Sí' if self.disponibilidad else 'No'}\n"
       if self._costo_calculado is not None and self._horas_reserva > 0:
            return descripcion_base + \
                   f"  Horas reservadas: {self._horas_reserva}\n" \
                   f"  Descuento aplicado: ${self._descuento:.2f}\n" \
                   f"  Costo actual: ${self._costo_calculado:.2f}\n" \
                   f"------------------------------------"
       else:
            return descripcion_base + \
                   f"  Costo: Debe calcularse primero (llame a calcular_costo).\n" \
                   f"------------------------------------"


    """
    creé estos métodos para obtener los datos del servicio. útil para procesar una reserva
    """

    def obtener_horas_reservas(self):
        return self._horas_reserva


    def obtener_valor_descuento(self):
        return self._descuento




class ServicioAlquilerEquipo(Servicio):
    """
    Servicio de alquiler de equipos.
    """

    def __init__(self, nombre, tipo_equipo, precio_por_dia=80000):
        super().__init__(nombre, precio_por_dia)
        self._tipo_equipo = tipo_equipo
        self._dias = 0
        self._cantidad = 0
        self._impuestos = 0

    def validar_parametros(self, dias, cantidad):
        """
        validar que días sea un número positivo y la cantidad de equipos a alquilar esté entre 1 y 100
        """
        if dias <= 0:
            raise ErrorValidacion(f"error en {self.__class__.__name__}: Los días deben ser mayores a 0")

        if cantidad < 1 or cantidad > 100:
            raise ErrorValidacion(f"error en {self.__class__.__name__}: La cantidad debe estar entre 1 y 100")

        self._dias = dias
        self._cantidad = cantidad


    def calcular_costo(self, dias, cantidad, impuestos=0):
        """
        calcula el costo de este servicio.
        dias: dias de alquiler del equipo
        cantidad: total de equipos de ese tipo
        impuesto: número entre 0 y 100 que representa el porcentaje de impuestos
        """

        self.validar_disponibilidad() #si no está disponible lanza una excepción
        self.validar_parametros(dias, cantidad)

        if impuestos < 0 or impuestos > 100:
            raise ErrorValidacion(f"error en {self.__class__.__name__}: El impuesto debe estar entre 0 y 100")

        self._impuestos = impuestos

        costo = dias * cantidad * self.precio
        costo += costo * (impuestos / 100) # sumo el impuesto

        return costo




    """
    métodos que devuelve string y se usan en la aplicación por consola para listar el servicio
    """


    def descripcion_servicio(self):
        try:
            costo = self.calcular_costo(self._dias, self._cantidad, self._impuestos)
            return f"{self.nombre} | Equipo: {self._tipo_equipo} | Días: {self._dias} | Cantidad: {self._cantidad} | Costo: ${costo}"
        except:
            return f"{self.nombre} | Equipo: {self._tipo_equipo} | Servicio no procesado"

    def obtener_dias_alquiler(self):
        return self._dias

    def obtener_cantidad(self):
        return self._cantidad

    def obtener_impuestos(self):
        return self._impuestos






class ServicioAsesoria(Servicio):
    """
    Servicio profesional de asesoría.
    """

    def __init__(self, nombre, especialidad, tarifa_por_hora=60000):
        super().__init__(nombre, tarifa_por_hora)
        self._especialidad = especialidad
        self._horas = 0
        self._urgencia = False

    def validar_parametros(self, horas):
        """
        valida que las horas de asesoría sea un número positivo
        """
        if horas <= 0:
            raise ErrorValidacion(f"error en {self.__class__.__name__}: Las horas deben ser mayores a 0")

        self._horas = horas

    def calcular_costo(self, horas, urgencia=False):
        """
        calcula el costo de la asesoria
        horas: horas de asesoria

        urgencia: True si es de urgencia. se simula un aumento del 20% del precio final en caso de que es un servicio
        al que se le tiene que dar prioridad
        """

        self.validar_disponibilidad()
        self.validar_parametros(horas)

        costo = horas * self.precio

        if urgencia:
            costo *= 1.2

        self._urgencia = urgencia

        return costo





    """
    métodos para listar el servicio en la aplicación por consola
    """

    def descripcion_servicio(self):
        try:
            costo = self.calcular_costo(self._horas, self._urgencia)
            return f"{self.nombre} | Especialidad: {self._especialidad} | Horas: {self._horas} | Costo: ${costo}"
        except:
            return f"{self.nombre} | Especialidad: {self._especialidad} | Servicio no procesado"

    def obtener_horas(self):
        return self._horas

    def obtener_urgencia(self):
        return self._urgencia
