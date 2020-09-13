import sys
from connection.conn import Connection

class Usuario:
    def __init__(self, usuario_id, nombre, rol):
        self.usuario_id = usuario_id
        self.nombre = nombre
        self.rol = rol

class Registro(Usuario):
    def __init__(self, usuario_id, nombre, rol):
        Usuario.__init__(self,usuario_id,nombre,rol)

    def set_usuario(self):
        pass

    def mostrar_usuario(self):
        pass
    
    def guardar_datos(self):
        pass