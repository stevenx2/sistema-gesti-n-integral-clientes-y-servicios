from clientes import Cliente
from textos_aplicacion import RecursosTexto
import datetime
from errores import ErrorSistema
from errores import ErrorValidacion
from reserva import Reserva
from servicios import Servicio
from servicios import ServicioReservaSala
from servicios import ServicioAlquilerEquipo
from servicios import ServicioAsesoria



"""
este archivo tiene la clase para hacer reservas, la aplicación por consola y un método que permite escribir logs de error
en el archivo "logs.txt"
"""


def registrar_log(mensaje):
    """
    método que registra logs en archivo 'logs.txt'
    """
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("logs.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"[{fecha_hora}]{mensaje}\n")





class Aplicacion:
    """
    es la aplicación por consola que integra las reservas de servicios, los clientes y las reservas
    """

    def __init__(self,datos_iniciales = False):
        self._clientes: list[Cliente] = []
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





    def _crear_servicio(self,tipo) -> Servicio:
        """
        método para crear un servicio por consola
        tipo: subclase de servicio que representa el servicio que quieres crear. es la clase NO una instancia
        retorna el servicio creado
        """

        servicio = None
        while True:

         try:

             nombre_servicio = input(self._recursos_texto.PEDIR_NOMBRE_SERVICIO)

             """
             tipo ==  ServicioReservaSala
             """
             if tipo == ServicioReservaSala:
                 horas_alquiler = int(input(self._recursos_texto.PEDIR_HORAS_RESERVA_SALA))


                 servicio = ServicioReservaSala(nombre_servicio)

                 mensaje_descuento = self._recursos_texto.obtener_mensaje_descuento_sala(servicio.calcular_costo(horas_alquiler))

                 descuento = int(input(mensaje_descuento))

                 """
                 lanzar excepción en caso que el descuento es mayor al precio base
                 """
                 if descuento > servicio.calcular_costo(horas_alquiler):
                     raise ErrorValidacion(f"""error en {self.__class__.__name__}:el valor del descuento no puede ser mayor al precio del servicio""")

                 #calculo el precio para que los atributos de la clase se actualizen
                 servicio.calcular_costo(horas_alquiler,descuento=descuento)

                 return servicio




             elif tipo == ServicioAlquilerEquipo:
              """
               tipo == ServicioAlquilerEquipo:
              """
              tipo_equipo = input(self._recursos_texto.PEDIR_NOMBRE_EQUIPO_A_ALQUILAR)

              if not tipo_equipo or not tipo_equipo.strip():
                  raise ErrorValidacion(f"""error en {self.__class__.__name__}:el nombre del equipo a alquilar no pueda estar vacio""")

              servicio = ServicioAlquilerEquipo(nombre_servicio,tipo_equipo)

              cantidad_equipos = int(input(self._recursos_texto.PEDIR_CANTIDAD_EQUIPOS_A_ALQUILAR))

              dias_alquiler = int(input(self._recursos_texto.PEDIR_CANTIDAD_DIAS_ALQUILER))


              costo = servicio.calcular_costo(dias_alquiler,cantidad_equipos)

              impuestos = int(input(self._recursos_texto.PEDIR_PORCENTAJE_IMPUESTOS))


              servicio.calcular_costo(dias_alquiler,cantidad_equipos,impuestos=impuestos)
              return servicio


             elif tipo == ServicioAsesoria:
                 """
                 tipo == ServicioAsesoria
                 """
                 especialidad = input(self._recursos_texto.PEDIR_ESPECIALIDAD_ASESORIA)

                 if not especialidad or not especialidad.strip():
                  raise ErrorValidacion(f"""error en {self.__class__.__name__}:la especialidad del servicio de asesoría no puede estar vacio""")


                 horas = int(input(self._recursos_texto.PEDIR_HORAS_ASESORIA))

                 urgencia = self._pedir_opcion(
                     opciones_validas=["s","n","S","N"],
                     mensaje_error=self._recursos_texto.MENSAJE_ERROR_URGENCIA_SERVICIO_INVALIDA,
                     mensaje=self._recursos_texto.PEDIR_URGENCIA_SERVICIO)

                 urgencia = urgencia.lower() == "s"

                 servicio = ServicioAsesoria(nombre_servicio,especialidad)

                 servicio.calcular_costo(horas,urgencia)
                 return servicio


         except ErrorSistema as error:
             registrar_log(error)
             print(f"{error}")
             continue


         except ValueError as error:
             registrar_log(f"Error en {self.__class__.__name__} al crear servicio : valores como el impuesto, días, cantidad deben ser numéricos.")
             print("""\nError : debe ingresar valores numéricos válidos""")
             continue




    def _cargar_datos_iniciales(self):
        """
        carga datos iniciales en la aplicación. solo lo usa para pruebas
        """
        self._clientes.append(Cliente("clienteUno", "cliente1@gmail.com", "1111111111"))
        self._clientes.append(Cliente("clienteDos", "cliente2@gmail.com", "2222222222"))
        self._clientes.append(Cliente("clienteTres", "cliente3@gmail.com", "3333333333"))
        self._clientes.append(Cliente("clienteCuatro", "cliente4@gmail.com", "4444444444"))
        self._clientes.append(Cliente("clienteCinco", "cliente5@gmail.com", "5555555555"))

        servicio1 = ServicioAlquilerEquipo("alquiler de tecnología de última generación","Computador")
        servicio1.calcular_costo(2,10)

        servicio2 = ServicioAsesoria("servicio asesoría de software","crear sitio web")
        servicio2.calcular_costo(2,urgencia=True)

        servicio3 = ServicioReservaSala("reserva de instalaciones de recreación")
        servicio3.calcular_costo(2,descuento=10000)

        self._servicios.append(servicio1)
        self._servicios.append(servicio2)
        self._servicios.append(servicio3)




    def iniciar(self):
        """
        punto de incio de la aplicación
        """

        if self._datos_iniciales:
            self._cargar_datos_iniciales()


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
                    while True:

                   # Pide los datos del cliente por consola

                        nombre = input(self._recursos_texto.PEDIR_NOMBRE_CLIENTE).strip()

                        email = input(self._recursos_texto.PEDIR_EMAIL_CLIENTE).strip()

                        telefono = input(self._recursos_texto.PEDIR_TELEFONO_CLIENTE).strip()

                        try:
                            cliente = Cliente(nombre,email,telefono)
                        except ErrorSistema as e:
                            registrar_log(f"Error al crear cliente: {str(e)}")
                            print(f"Error: {str(e)}\n")
                            continue

                        else:
                            self._clientes.append(cliente)
                            print(self._recursos_texto.MENSAJE_CLIENTE_REGISTRADO)
                            break







                case "2":
                    """
                    crear servicio
                    """

                    """
                    usa el método que pide un dato hasta que se inserte una de las opciones válidas, en este caso ["1","2","3","4"]
                    """
                    tipo_servicio = self._pedir_opcion(
                        opciones_validas=["1","2","3","4"],
                        mensaje_error= self._recursos_texto.MENSAJE_ERROR_OPCION_SERVICIO_NO_VALIDA,
                        mensaje= self._recursos_texto.MENSAJE_OPCIONES_SERVICIO)

                    servicio = None

                    """"
                    dependiendo el número de teclado, creo un servicio de un tipo.
                    la opción 4 es para volver al menú principal
                    """

                    match tipo_servicio:
                        case "1":
                            servicio = self._crear_servicio(ServicioReservaSala)

                        case "2":
                            servicio = self._crear_servicio(ServicioAlquilerEquipo)


                        case "3":
                            servicio = self._crear_servicio(ServicioAsesoria)

                        case "4":
                            continue

                    #agrego el servicio a la lista
                    self._servicios.append(servicio)

                    print(self._recursos_texto.MENSAJE_SERVICIO_REGISTRADO)








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
                            print(f"""{indice}. {s.descripcion_servicio()}""") # aquí listo una reserva
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
                    print(self._recursos_texto.TITULO_PROCESAMIENTO_RESERVA)


                    # muestro mensaje si no hay reservas
                    if not self._reservas:
                        print(self._recursos_texto.MENSAJE_LISTA_RESERVAS_VACIA)

                    # listo las reservas y pido que el usuario elija una opción
                    else:

                     indices_permitidos = []

                     for r in self._reservas:
                         indice = self._reservas.index(r) + 1

                         print(f"""{indice}. {r.mostrar()}""")
                         indice_str = str(indice)
                         indices_permitidos.append(indice_str)


                     indice_reserva = self._pedir_opcion(
                         opciones_validas=indices_permitidos,
                         mensaje_error=self._recursos_texto.MENSAJE_ERROR_SELECCION_RESERVA,
                         mensaje=self._recursos_texto.PEDIR_SELECCION_RESERVA)



                     try:
                         """
                         dependiendo la instancia del servicio de esta reserva, lo proceso
                         """
                         indice_reserva = int(indice_reserva) -1
                         reserva = self._reservas[indice_reserva]

                         servicio = reserva.obtener_servicio()

                         if isinstance(servicio,ServicioReservaSala):
                           reserva.procesar(servicio.obtener_horas_reservas(),descuento=servicio.obtener_valor_descuento())


                         elif isinstance(servicio,ServicioAlquilerEquipo):
                            reserva.procesar(servicio.obtener_dias_alquiler(),servicio.obtener_cantidad(),impuestos=servicio.obtener_impuestos())


                         elif isinstance(servicio,ServicioAsesoria):
                            reserva.procesar(servicio.obtener_horas(), urgencia=servicio.obtener_urgencia())


                         print(self._recursos_texto.MENSAJE_RESERVA_PROCESADA)


                     except ValueError as err:
                         print(self._recursos_texto.MENSAJE_ERROR_PROCESAR_RESERVA)

                     except ErrorSistema as err:
                          """
                          esta excepción es lanzada por el método procesar() de reserva cuando se quiere procesar una reserva que tiene un servicio inhabilitado
                          """
                          registrar_log(err)
                          print(f"""{err}.""")







                case "6":
                    """
                    cancelar reserva
                    """
                    print(self._recursos_texto.TITULO_CANCELACION_RESERVA)



                    if not self._reservas:
                        print(self._recursos_texto.MENSAJE_LISTA_RESERVAS_VACIA)


                    else:

                     indices_permitidos = []

                     for r in self._reservas:
                         indice = self._reservas.index(r) + 1
                         print(f"""{indice}. {r.mostrar()}""")
                         indice_str = str(indice)
                         indices_permitidos.append(indice_str)


                     indice_reserva = self._pedir_opcion(
                         opciones_validas=indices_permitidos,
                         mensaje_error=self._recursos_texto.MENSAJE_ERROR_SELECCION_RESERVA,
                         mensaje=self._recursos_texto.PEDIR_SELECCION_RESERVA_A_CANCELAR )


                     try:
                         indice_reserva = int(indice_reserva) -1
                         reserva = self._reservas[indice_reserva]

                         reserva.cancelar() # cancelar la reserva

                         print(self._recursos_texto.MENSAJE_RESERVA_CANCELADA)


                     except ValueError as err:
                         print(self._recursos_texto.MENSAJE_ERROR_CANCELAR_RESERVA)

                     except ErrorSistema as err:
                          registrar_log(err)
                          print(f"""{err}.""")




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
                    lista clientes
                    """

                    print(self._recursos_texto.TITULO_LISTADO_CLIENTES)

                    #mensaje en caso de lista vacia
                    if not self._clientes:
                        print(self._recursos_texto.MENSAJE_LISTADO_CLIENTES_VACIO)

                    # listar clientes si la lista tiene elementos
                    else:
                     for i in self._clientes:
                         indice = self._clientes.index(i) + 1

                         print(f"""\n{indice}. {i.descripcion_cliente()}""")




                case "9":
                     """
                     habilitar servicio
                     """

                     print(self._recursos_texto.TITULO_HABILITAR_SERVICIO)

                     if not self._servicios:
                         print(self._recursos_texto.MENSAJE_LISTADO_SERVICIOS_VACIO)
                         continue

                     indices_permitidos = []
                     print(self._recursos_texto.MENSAJE_SELECCION_SERVICIO)
                     for s in self._servicios:
                         indice = self._servicios.index(s) + 1
                         print(f"""{indice}. {s.descripcion_servicio()}""")
                         indice_str = str(indice)
                         indices_permitidos.append(indice_str)

                     try:
                         opcion_servicio = self._pedir_opcion(
                             opciones_validas=indices_permitidos,
                             mensaje=self._recursos_texto.PEDIR_SERVICIO_A_HABILITAR,
                             mensaje_error=self._recursos_texto.MENSAJE_ERROR_SELECCION_SERVICIO
                         )


                         indice_servicio = int(opcion_servicio) - 1
                         servicio_a_habilitar = self._servicios[indice_servicio]
                         servicio_a_habilitar.activar()
                         print(self._recursos_texto.MENSAJE_SERVICIO_HABILITADO)

                     except ValueError:
                         """
                         este error nunca se lanza porque ya lo tengo previsto, de todas maneras atrapo la excepción.
                         """
                         registrar_log(f"error en {self.__class__.__name__}: error al convertir un string a int al habilitar servicio")
                         continue
                     except Exception as e:
                         registrar_log(f"error en {self.__class__.__name__}: {e}")
                         print("Ocurrió un error inesperado al habilitar el servicio.")
                         continue







                case "10":
                    """
                    deshabilitar servicio
                    """

                    print(self._recursos_texto.TITULO_DESHABILITAR_SERVICIO)

                    if not self._servicios:
                        print(self._recursos_texto.MENSAJE_LISTADO_SERVICIOS_VACIO)
                        continue
                    indices_permitidos = []


                    print(self._recursos_texto.MENSAJE_SELECCION_SERVICIO)
                    for s in self._servicios:
                        indice = self._servicios.index(s) + 1
                        print(f"""{indice}. {s.descripcion_servicio()}""")
                        indice_str = str(indice)
                        indices_permitidos.append(indice_str)

                    try:
                        opcion_servicio = self._pedir_opcion(
                            opciones_validas=indices_permitidos,
                            mensaje=self._recursos_texto.PEDIR_SERVICIO_A_DESHABILITAR,
                            mensaje_error=self._recursos_texto.MENSAJE_ERROR_SELECCION_SERVICIO
                        )


                        indice_servicio = int(opcion_servicio) - 1
                        servicio_a_deshabilitar = self._servicios[indice_servicio]
                        servicio_a_deshabilitar.desactivar()
                        print(self._recursos_texto.MENSAJE_SERVICIO_DESHABILITADO)

                    except ValueError:
                        """
                        este error nunca se lanza porque ya lo tengo previsto, de todas maneras atrapo la excepción.
                        """
                        registrar_log(f"error en {self.__class__.__name__}: error al convertir un string a int al deshabilitar servicio")
                        continue
                    except Exception as e:
                        registrar_log(f"error en {self.__class__.__name__}: {e}")
                        print("Ocurrió un error inesperado al deshabilitar el servicio.")
                        continue


                case "11":
                    exit()




