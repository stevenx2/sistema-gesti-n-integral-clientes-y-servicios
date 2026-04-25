from clientes import cliente
from textos_aplicacion import RecursosTexto
from errores import ErrorSistema
from errores import ErrorValidacion
from reserva import Reserva
from servicios import Servicio
from servicios import ServicioReservaSala



"""
este archivo tiene la clase para hacer reservas, la aplicación por consola y un método que permite escribir logs de error
en el archivo "logs.txt"
"""


def registrar_log(mensaje):
    """
    método que registra logs en archivo 'logs.txt'
    """
    with open("logs.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{mensaje}\n")





class Aplicacion:
    """
    es la aplicación por consola que integra las reservas de servicios, los clientes y las reservas
    """

    def __init__(self,datos_iniciales = False):
        self._clientes: list[cliente] = []
        self._reservas:list[Reserva] = []
        self._servicios:list[Servicio] = []
        self._recursos_texto = RecursosTexto()
        self._datos_iniciales = datos_iniciales


    def _pedir_opcion(self, mensaje="", opciones_validas=None, mensaje_error="Opción inválida"):
     """
     pedir una opción entre las dadas, si no se elije una de ellas informa por consola y registra el log en "logs.txt"
     mensaje: es el mensaje que sale por consola para pedirte el dato, ej: 'ingrese su edad:'
     opciones_validas: array de strings que contempla las opciones válidas, si pasas el array ['1','2'] y luego por consola escribes una diferente, entonces muestra un mensaje de error y vuelve a pedir el dato
     mensaje_error: mensaje que aparece cuando no se escribe por consola una de las opciones válidas. registra log y muestra en consola
     retorna: la opción elegida
     """

     if opciones_validas is None:
         opciones_validas = []

     while True:
         opcion = input(mensaje).strip()


         # validación
         if opciones_validas and opcion not in opciones_validas:
            print(f"{mensaje_error}\n")
            mensaje_error_log = mensaje_error.strip()
            registrar_log(f"{mensaje_error_log}")
            continue

         return opcion






    def iniciar(self):
        """
        punto de incio de la aplicación
        """


        while (True):
            """
            bucle infinito que pide una opción y hace una tarea según la respuesta
            """

            accion = self._pedir_opcion(
                opciones_validas=["1","2","3","4","5","6","7","8","9","10","11"],
                mensaje_error=self._recursos_texto.MENSAJE_ERROR_OPCION_NO_VALIDA_MENU_INICIAL,
                mensaje= self._recursos_texto.MENSAJE_MENU_INICIAL)

            match accion:


                case "1":
                    """
                    crear cliente
                    """
                    pass






                case "2":
                    """
                    crear servicio
                    """


                    pass





                case "3":
                    """
                    listar los servicios registrados
                    """
                    print(self._recursos_texto.TITULO_LISTADO_SERVICIOS)

                    if not self._servicios:
                        print(self._recursos_texto.MENSAJE_LISTADO_SERVICIOS_VACIO)
                    else:
                        for i, servicio in enumerate(self._servicios, start=1):
                            print(f"{i}. {servicio.descripcion_servicio()}")




                case "4":
                    """
                    crear reserva
                    """

                    """
                    si no tengo clientes ni servicios inscritos muestro un mensaje avisando. para crear una reserva
                    debe existir al menor un servicio y un cliente que lo reserva
                    """

                    if not self._servicios or not self._clientes:
                        print(self._recursos_texto.MENSAJE_LISTADO_CLIENTES_SERVICIOS_VACIO_CREAR_RESERVA)


                    else:
                        """
                        si hay elementos entonces los listo para que el usuario elija
                        """

                        #indices que representan las opciones válidas al pedir dato por consola
                        indices_permitidos = []

                        print(self._recursos_texto.MENSAJE_SELECCION_CLIENTE)

                        # listo clientes y pido que elija uno para asignarle un servicio
                        for c in self._clientes:
                            indice = self._clientes.index(c) + 1
                            print(f"""{indice}. {c.descripcion_cliente()}""")
                            indice_str = str(indice)
                            indices_permitidos.append(indice_str)

                        indice_cliente = self._pedir_opcion(
                            opciones_validas=indices_permitidos,
                            mensaje_error=self._recursos_texto.MENSAJE_ERROR_SELECCIONAR_CLIENTE,
                            mensaje=self._recursos_texto.PEDIR_SELECCION_CLIENTE)


                        """
                        lo mismo con los servicios, las listo y pido al usuario que elija uno.
                        """

                        indices_permitidos = []


                        print(self._recursos_texto.MENSAJE_SELECCION_SERVICIO)

                        # listo servicios y pido la elección de uno para asignar a la reserva
                        for s in self._servicios:
                            indice = self._servicios.index(s) +1
                            print(f"""{indice}. {s.describir_servicio()}""") # aquí listo una reserva
                            indice_str = str(indice)
                            indices_permitidos.append(indice_str)


                        indice_servicio = self._pedir_opcion(
                            opciones_validas= indices_permitidos,
                            mensaje_error=RecursosTexto.MENSAJE_ERROR_SELECCION_SERVICIO,
                            mensaje=self._recursos_texto.PEDIR_SELECCION_SERVICIO)



                        try:
                          """
                          a este índice le resto 1 porque anteriormente lo sumé para mostrar valores de 1 en adelante por consola
                          """
                          indice_cliente  = int(indice_cliente) - 1
                          indice_servicio= int(indice_servicio) -1

                          reserva = Reserva(cliente=self._clientes[indice_cliente],servicio=self._servicios[indice_servicio])
                          self._reservas.append(reserva)

                          print(self._recursos_texto.MENSAJE_RESERVA_REGISTRADA)

                        except ValueError as e:
                            """
                            este error nunca se lanza porque ya lo tengo previsto, de todas maneras atrapo la excepción.
                            """
                            registrar_log(f"""error en {self.__class__.__name__}:error al convertir un string a int""")
                            continue





                case "5":
                    """
                    procesar reserva
                    """

                    pass





                case "6":
                    """
                    cancelar reserva
                    """
                    pass




                case "7":
                    """
                    listar reservas
                    """

                    print(self._recursos_texto.TITULO_LISTADO_RESERVAS)

                    if not self._reservas:
                        print(self._recursos_texto.MENSAJE_LISTA_RESERVAS_VACIA)
                    else:
                        for i, reserva in enumerate(self._reservas, start=1):
                            print(f"\n{i}. {reserva.mostrar()}")




                case "8":
                    """
                    listar clientes
                    """

                    pass



                case "9":
                     """
                     habilitar servicio
                     """
                     pass






                case "10":
                    """
                    deshabilitar servicio
                    """
                    pass


                case "11":
                    exit()




