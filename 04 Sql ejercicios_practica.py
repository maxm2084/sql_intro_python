#!/usr/bin/env python
'''
SQL Introducción [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import sqlite3

# https://extendsclass.com/sqlite-browser.html


def create_schema():

    # Conectarnos a la base de datos
    # En caso de que no exista el archivo se genera
    # como una base de datos vacia
    conn = sqlite3.connect('secundaria.db')

    # Crear el cursor para poder ejecutar las querys
    c = conn.cursor()

    # Ejecutar una query
    c.execute("""
                DROP TABLE IF EXISTS estudiante;
            """)

    # Ejecutar una query
    c.execute("""
            CREATE TABLE estudiante(
                [id] INTEGER PRIMARY KEY AUTOINCREMENT,
                [name] TEXT NOT NULL,
                [age] INTEGER NOT NULL,
                [grade] INTEGER,
                [tutor] TEXT
            );
            """)

    # Para salvar los cambios realizados en la DB debemos
    # ejecutar el commit, NO olvidarse de este paso!
    conn.commit()

    # Cerrar la conexión con la base de datos
    conn.close()


def fill():
    print('Completemos esta tablita!')
    # Llenar la tabla de la secundaria con al menos 5 estudiantes
    # Cada estudiante tiene los posibles campos:
    # id --> este campo es auto incremental por lo que no deberá completarlo
    # name --> El nombre del estudiante (puede ser solo nombre sin apellido)
    # age --> cuantos años tiene el estudiante
    # grade --> en que año de la secundaria se encuentra (1-6)
    # tutor --> nombre de su tutor

    # Se debe utilizar la sentencia INSERT.
    # Observar que hay campos como "grade" y "tutor" que no son obligatorios
    # en el schema creado, puede obivar en algunos casos completar esos campos
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()

    values1 = ["Juan Perez", 17, 4,"Hector el father"]
    
    c. execute("""
            INSERT INTO estudiante (name, age, grade,tutor) 
            VALUES (?,?,?,?);""", values1)
    
    values2 = ["Maria Garcia", 15, 3,"Patricia Bullrich"]
    
    c. execute("""
            INSERT INTO estudiante (name, age, grade,tutor) 
            VALUES (?,?,?,?);""", values2)
    
    values3 = ["Mia Kalifa", 34, 5,"Daddy Yankee"]
    
    c. execute("""
            INSERT INTO estudiante (name, age, grade,tutor) 
            VALUES (?,?,?,?);""", values3)
    
    values4 = ["Cristian Castro", 17, 4,"Luis Miguel"]

    
    
    c. execute("""
            INSERT INTO estudiante (name, age, grade,tutor) 
            VALUES (?,?,?,?);""", values4)
    
    values5 = ["Lionel Messi", 35, 6,"La Mosca"]
    
    c. execute("""
            INSERT INTO estudiante (name, age, grade,tutor) 
            VALUES (?,?,?,?);""", values5)
    
    conn.commit()
    # Cerrar la conexión con la base de datos
    conn.close()
    
def fetch():
    print('Comprobemos su contenido, ¿qué hay en la tabla?')
    # Utilizar la sentencia SELECT para imprimir en pantalla
    # todas las filas con todas sus columnas
    # Utilizar fetchone para imprimir de una fila a la vez
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()
    
    c.execute('SELECT * FROM estudiante')
    
    data = c.fetchall()
    
    print(data)

    c.execute('SELECT * FROM estudiante')
    print('Recorrer los datos desde el cursor')
    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)


def search_by_grade(grade):
    print('Operación búsqueda!')
    # Utilizar la sentencia SELECT para imprimir en pantalla
    # aquellos estudiantes que se encuentra en en año "grade"

    # De la lista de esos estudiantes el SELECT solo debe traer
    # las siguientes columnas por fila encontrada:
    # id / name / age
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()
    
    c.execute('SELECT id, name, age FROM estudiante WHERE grade = ?', (grade,) )
    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)

    conn.close()


def insert(grade):
    print('Nuevos ingresos!')
    # Utilizar la sentencia INSERT para ingresar nuevos estudiantes
    # a la secundaria
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()

    values1 = ["Juan Valdez", 14, 1,"La tercera"]
    
    c. execute("""
            INSERT INTO estudiante (name, age, grade,tutor) 
            VALUES (?,?,?,?);""", values1)
    
    conn.commit()
    # Cerrar la conexión con la base de datos
    conn.close()


def modify(id, name):
    print('Modificando la tabla')
    # Utilizar la sentencia UPDATE para modificar aquella fila (estudiante)
    # cuyo id sea el "id" pasado como parámetro,
    # modificar su nombre por "name" pasado como parámetro
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()

    rowcount = c.execute("UPDATE estudiante SET name =? WHERE id =?",
                (name, id)).rowcount

    print('Filas actualizadas:', rowcount)

    # Save
    conn.commit()
    # Cerrar la conexión con la base de datos
    conn.close()

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    create_schema()   # create and reset database (DB)
    fill()
    fetch()

    grade = 3
    search_by_grade(grade)

    new_student = ['You', 16]
    insert(new_student)

    name = 'Carolina Herrera'
    id = 2
    modify(id, name)
