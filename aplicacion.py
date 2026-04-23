import errores
from clientes import cliente
from textos_aplicacion import RecursosTexto
import datetime


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

    def __init__(self):
        self._clientes: list[cliente] = []
        self._recursos_texto = RecursosTexto()


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
            registrar_log(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]{mensaje_error_log}")
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
                    while True:

                   # Pide los datos del cliente por consola      

                        nombre = input(self._recursos_texto.PEDIR_NOMBRE_CLIENTE).strip()

                        email = input(self._recursos_texto.PEDIR_EMAIL_CLIENTE).strip()
                        
                        telefono = input(self._recursos_texto.PEDIR_TELEFONO_CLIENTE).strip()

                        try:
                            cliente = cliente(nombre,email,telefono)
                        except ErrorSistema as e:
                            registrar_log(f"Error al crear cliente: {str(e)}")
                            print(f"Error: {str(e)}\n")
                            continue

                        else:
                            self._clientes.append(cliente)
                            print(self._recursos_texto.MENSAJE_CLIENTE_REGISTRADO)
                            break

                    

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
                    pass




                case "4":
                    """
                    crear reserva
                    """

                    pass



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

                    pass




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

                         print(f"""\n{indice}. {i.descripcion()}""")


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



app = Aplicacion()

app.iniciar()
