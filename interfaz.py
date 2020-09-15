from connection.conn import Connection
from time import sleep
from pprint import pprint

c = Connection()
def menu(c):
    while True:
        print('Bienvenido al gestor de datos del colegio Perez de Cuellar')
        #docentes
        #alumnos
        #salones
        #cursos
        #notas
        #periodo_escolar
        print('Seleccione la acción que desea realizar: ')
        print('\t1 - Registrar Docente')
        print('\t2 - Registrar Alumno')
        print('\t3 - Gestionar catedras de Docentes')
        print('\t4 - Gestionar notas de Alumnos')
        print('\t5 - Ver Docentes')
        print('\t6 - Ver Alumnos')
        print('\t7 - Ver notas')
        print('\t8 - Salir')
        opcion = input("> ")
        if opcion == "1":
            mostrar_alumnos(c)
        elif opcion == "6":
            mostrar_alumnos(c)
        elif opcion == "8":
            print("\nGracias por usar esta aplicación")
            sleep(2)
            quit()
        else:
            print("\nHas introducido una opción errónea")


def continuar():
    pass

def insert_usuario():
    pass

def insert_catedras():
    pass

def insert_notas():
    pass

def mostrar_docentes():
    pass

def mostrar_alumnos(c):
    usuarios = c.execute_query('Select * from usuario')
    list_usuarios = list(usuarios)
    pprint(list_usuarios)
    pass

def mostrar_notas():
    pass
