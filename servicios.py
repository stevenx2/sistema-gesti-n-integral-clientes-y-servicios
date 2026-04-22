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

