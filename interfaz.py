from connection.conn import Connection
from pprint import pprint

def menu():
    print('Bienvenido al gestor de datos del colegio Perez de Cuellar')
    print('Que seleccione la acción que desea realizar: ')
    print('\t1 - Registrar Docentes')
    print('\t2 - Registrar Alumnos')
    print('\t3 - Gestionar catedras de Docentes')
    print('\t4 - Gestionar notas de Alumnos')
    print('\t5 - Ver Docentes')
    print('\t6 - Ver Alumnos')
    print('\t7 - Ver notas')
    print('\t8 - Salir')

def continuar(self):
    pass

def insert_usuario(self):
    pass

def insert_catedras(self):
    pass

def insert_notas(self):
    pass

def mostrar_docentes(self):
    pass

def mostrar_alumnos(self):
    pass

def mostrar_notas(self):
    pass


c = Connection()
usuarios = c.execute_query('Select * from usuario')
list_usuarios = list(usuarios)
pprint(list_usuarios)