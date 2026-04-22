from errores import Errorvalidacion

class cliente:
    def __init__(self,nombre,email,telefono):
        self.verifivar_nombre(nombre)
        self.verificar_email(email)
        self.verificar_telefono(telefono)

    def verificar_nombre(self,nombre):
        if not nombre or not nombre.strip():
            raise Errorvalidacion("El nombre no puede estar vacío")
        
        if any(char.isdigit() for char in nombre):
            raise Errorvalidacion("El nombre no puede contener números")
        
        self.nombre = nombre.strip()
        
    def verificar_email(self,email):
        if not email or not email.strip():
            raise Errorvalidacion("El email no puede estar vacío")
        
        if "@" not in email or "." not in email:
            raise Errorvalidacion("El email no es válido")
        
        self.email = email.strip()
        
    def verificar_telefono(self,telefono):

        if not telefono or not telefono.strip():
            raise Errorvalidacion("El teléfono no puede estar vacío")
        
        if not telefono.isdigit():
            raise Errorvalidacion("El teléfono debe contener solo números")
        
        if len(telefono) != 10:
            raise Errorvalidacion("El teléfono debe tener 10 dígitos")
        
        self.telefono = telefono.strip()

    
def obtener_nombre(self):
    return self.nombre

def obtener_email(self):
    return self.email 

def obtener_telefono(self):
    return self.telefono

def descripcion_cliente(self):
    return f"Nombre: {self.nombre}, Email: {self.email}, Teléfono: {self.telefono}"
  

  
  
