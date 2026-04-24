from clientes import Cliente
from servicios import Servicio
from errores import ErrorSistema
from errores import ErrorValidacion
import datetime



def registrar_log(mensaje):
    """
    método que registra logs en archivo 'logs.txt'
    """
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("logs.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"[{fecha_hora}]{mensaje}\n")





class Reserva:
    """
    maneja la reserva de un servicio a un cliente
    cliente: el cliente que va a realizar la reserva
    servicio: el servicio reservado
    estado: estado de la reserva. puede ser 'pendiente' (por defecto), 'confirmada' (cuando se procesa), 'cancelada' (cuando se procesa y luego se cancela) o 'fallida' (cuando se intentó procesar pero ocurrió un error)
    costo: cuando se procesa se calcula el precio de la reserva. en realidad el precio ya se podría saber pero lo hago para simular que el procesamiento calcula el precio
    """
    def __init__(self,cliente:Cliente,servicio:Servicio):
        self._cliente = cliente
        self._servicio = servicio
        self._estado = "pendiente"
        self._costo = 0


    def procesar(self, *argumentos,**argumentos_nombrados):
        """
        procesa la reserva. llama al método calcular_costo() de la implementación especifica del Servicio
        argumentos: lista de argumentos.
        argumentos_nombrados: diccionario de argumentos, son los que hay que poner el nombre del argumento y el valor
        nota: yo controlo la pasa de parámetros según la instancia de Servicio y los argumentos que pide su método calcular_costo()
        """
        try:
            self._costo = self._servicio.calcular_costo(*argumentos,**argumentos_nombrados)

        #registrar log en casa de error y cambiar estado de reserva
        except ErrorSistema as error:
            self._estado = "fallido"
            registrar_log(f"ERROR:{error}")
            raise

        else:
            self._estado = "confirmada"
            registrar_log(
                f"Reserva confirmada para {self._cliente.obtener_nombre()} - "
                f"{self._servicio.descripcion_servicio()} - Costo: {self._costo}"
            )


        finally:
            registrar_log("Intento de procesamiento de reserva finalizado\n")



    def cancelar(self):
        """
        cancelo la reserva. solo se pueden cancelar reservas previamente procesadas, de otro modo de lanza una excepción.
        """
        try:
            if self._estado != "confirmada":
                raise ErrorValidacion("No se puede cancelar una reserva no confirmada")

            self._estado = "cancelada"

        except ErrorSistema as e:
            registrar_log(f"ERROR al cancelar: {e}")
            raise

        else:
            registrar_log(
                f"Reserva cancelada para {self._cliente.obtener_nombre()}"
            )




    def mostrar(self):
        """
        usado cuando se quieren listar las reservas por consola
        """
        if self._estado != "confirmada":
            self._costo = "debe procesar la reserva para ver el precio"


        return (
            f"Cliente: {self._cliente.descripcion_cliente()} | \n"
            f"Servicio: {self._servicio.descripcion_servicio()} | \n"
            f"Estado: {self._estado} | \n"
            f"Costo: {self._costo} \n"
        )



    """
    obtener datos de la reserva
    """

    def obtener_servicio(self):
        return self._servicio


    def obetener_costo(self):
        self._costo
