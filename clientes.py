from errores import ErrorValidacion

"""
clase maneja todos los clientes del sistema
"""
class cliente:
    def __init__(self,nombre,email,telefono):
        self.verifivar_nombre(nombre)
        self.verificar_email(email)
        self.verificar_telefono(telefono)
"""
funciones para verificar los nombres, y datos de cada cliente, mas validaciones de error especificas
"""
    def verificar_nombre(self,nombre):
        if not nombre or not nombre.strip():
            raise ErrorValidacion("El nombre no puede estar vacío")

        if any(char.isdigit() for char in nombre):
            raise ErrorValidacion("El nombre no puede contener números")

        self.nombre = nombre.strip()

    def verificar_email(self,email):
        if not email or not email.strip():
            raise ErrorValidacion("El email no puede estar vacío")

        if "@" not in email or "." not in email:
            raise ErrorValidacion("El email no es válido")

        self.email = email.strip()

    def verificar_telefono(self,telefono):

        if not telefono or not telefono.strip():
            raise ErrorValidacion("El teléfono no puede estar vacío")

        if not telefono.isdigit():
            raise ErrorValidacion("El teléfono debe contener solo números")

        if len(telefono) != 10:
            raise ErrorValidacion("El teléfono debe tener 10 dígitos")

        self.telefono = telefono.strip()

"""
funciones para obtener datos de clientes
"""
def obtener_nombre(self):
    return self.nombre

def obtener_email(self):
    return self.email

def obtener_telefono(self):
    return self.telefono

def descripcion_cliente(self):
    return f"Nombre: {self.nombre}, Email: {self.email}, Teléfono: {self.telefono}"




