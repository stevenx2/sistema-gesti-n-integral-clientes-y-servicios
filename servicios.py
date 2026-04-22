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
        costo_base = self.obtener_horas_reservas() * self.precio
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


