#!/usr/bin/env python
from serializable import Serializable

class Proyecto(Serializable):
    def __init__(self, indice, nombre, lenguaje="", monto=0):
        path='./administrador_proyectos.txt'
        super().__init__(indice, path, "Proyecto")
        self.nombre=nombre
        self.lenguaje=lenguaje
        self.monto=monto

    def ingresar_informacion(self):
        self.nombre=input(f"Ingrese nombre: ") or self.nombre
        self.lenguaje=input(f"Ingrese lenguaje: ") or self.lenguaje
        self.monto=input(f"Ingrese monto: ") or self.monto

    def listar(self):
        proyectos=self.obtener()
        for proyecto in proyectos:
            print(proyecto.__str__())
    
    def update(self):
        self.ingresar_informacion()
        registros=self.obtener()
        for indice in range(0, len(registros)):
            if registros[indice].indice == self.indice:
                registros[indice]=self
                break
        self.update_file(registros)

    def delete(self):
        registros=self.obtener()
        filtrados = list(filter(lambda proyecto: proyecto.indice != self.indice, registros))
        self.update_file(filtrados)

    def obtener(self):
        proyectos=self.obtener_registros()
        return list(map(lambda array: self.parsear(array), proyectos))

    def seleccionar(self):
        self.listar()
        indice=input("Ingresar indice: ")
        proyectos=self.obtener()
        return list(filter(lambda proyecto: proyecto.indice == indice, proyectos))[0]

    def parsear(self, data):
        return Proyecto(data[0],data[1],data[2],data[3])

    def menu_proyecto(self):
        comando=1
        while comando!="0":
            persona=Persona(0,0)
            tarea=Tarea(0,0,0)
            print("""Seleccione una opcion:
            \t1) Editar proyecto
            \t2) Borrar proyecto
            \t3) Listar personas
            \t4) Listar tareas
            \t5) Ingresar nueva persona
            \t6) Seleccionar persona
            \t7) Ingresar nueva tarea
            \t8) Seleccionar tarea
            \t0) Salir
            """)
            comando=input("Opcion: ")
            if comando == "1":
                self.update()
            elif comando == "2":
                self.delete()
                comando="0"
            elif comando == "3":
                persona.listar(self.indice)
            elif comando == "4":
                tarea.listar_proyecto(self.indice)
            elif comando == "5":
                persona.ingresar_informacion(self.indice)
                persona.insert()
            elif comando == "6":
                persona=persona.seleccionar(self.indice)
                persona.menu_persona()
            elif comando == "7":
                tarea.ingresar_informacion(self.indice, 0)
                tarea.insert()
            elif comando == "8":
                tarea=tarea.seleccionar(self.indice)
                tarea.menu_tarea()

class Persona(Serializable):
    def __init__(self, indice, proyecto, nombre="", apellido=""):
        path='./administrador_personas.txt'
        super().__init__(indice, path,"Persona")
        self.proyecto=proyecto
        self.nombre=nombre
        self.apellido=apellido

    def ingresar_informacion(self, proyecto):
        self.proyecto=proyecto
        self.nombre=input(f"Ingrese nombre: ")
        self.apellido=input(f"Ingrese apellido: ")

    def update(self):
        self.ingresar_informacion(self.proyecto)
        registros=self.obtener()
        for indice in range(0, len(registros)):
            if registros[indice].indice == self.indice:
                registros[indice]=self
                break
        self.update_file(registros)

    def delete(self):
        registros=self.obtener()
        filtrados = list(filter(lambda persona: persona.indice != self.indice, registros))
        self.update_file(filtrados)

    def seleccionar(self, proyecto):
        self.listar(proyecto)
        indice=input("Ingresar indice: ")
        proyectos=self.obtener()
        return list(filter(lambda proyecto: proyecto.indice == indice, proyectos))[0]

    def listar(self, proyecto):
        personas=self.obtener()
        filtrados = list(filter(lambda persona: persona.proyecto == proyecto, personas))
        for persona in filtrados:
            print(persona.__str__())

    def obtener(self):
        personas=self.obtener_registros()
        personas=list(map(lambda array: self.parsear(array), personas))
        return personas

    def parsear(self, data):
        return Persona(data[0],data[1],data[2],data[3])

    def menu_persona(self):
        comando=1
        while comando!="0":
            persona=Persona(0,0)
            tarea=Tarea(0,0,0)
            print("""Seleccione una opcion:
            \t1) Editar persona
            \t2) Borrar persona
            \t3) Listar tareas
            \t4) Ingresar nueva tarea
            \t5) Seleccionar tarea
            \t0) Salir
            """)
            comando=input("Opcion: ")
            if comando == "1":
                self.update()
            elif comando == "2":
                self.delete()
                comando="0"
            elif comando == "3":
                tarea.listar_persona(self.indice)
            elif comando == "4":
                tarea.ingresar_informacion(self.proyecto, self.indice)
                tarea.insert()
            elif comando == "5":
                tarea=tarea.seleccionar(self.indice)
                tarea.menu_tarea()

class Tarea(Serializable):
    def __init__(self, indice, proyecto, persona, descripcion="", duracion=0):
        path='./administrador_tareas.txt'
        super().__init__(indice, path,"Tarea")
        self.proyecto=proyecto
        self.persona=persona
        self.descripcion=descripcion
        self.duracion=duracion

    def reasignar(self, persona):
        self.persona=persona
        registros=self.obtener()
        for indice in range(0, len(registros)):
            if registros[indice].indice == self.indice:
                registros[indice]=self
                break
        self.update_file(registros)

    def update(self):
        self.ingresar_informacion(self.proyecto, self.persona)
        registros=self.obtener()
        for indice in range(0, len(registros)):
            if registros[indice].indice == self.indice:
                registros[indice]=self
                break
        self.update_file(registros)

    def delete(self):
        registros=self.obtener()
        filtrados = list(filter(lambda persona: persona.indice != self.indice, registros))
        self.update_file(filtrados)

    def seleccionar(self, proyecto):
        self.listar_proyecto(proyecto)
        indice=input("Ingresar indice: ")
        proyectos=self.obtener()
        return list(filter(lambda proyecto: proyecto.indice == indice, proyectos))[0]

    def ingresar_informacion(self, proyecto, persona):
        self.persona=persona
        self.proyecto=proyecto
        self.descripcion=input(f"Ingrese descripcion: ")
        self.duracion=input(f"Ingrese duracion: ")

    def listar_persona(self, persona):
        tareas=self.obtener()
        filtrados = list(filter(lambda tarea: tarea.proyecto == persona, tareas))
        for tarea in filtrados:
            print(tarea.__str__())

    def listar_proyecto(self, proyecto):
        tareas=self.obtener()
        filtrados = list(filter(lambda tarea: tarea.proyecto == proyecto, tareas))
        for tarea in filtrados:
            print(tarea.__str__())

    def obtener(self):
        personas=self.obtener_registros()
        return list(map(lambda array: self.parsear(array), personas))

    def parsear(self, data):
        return Tarea(data[0],data[1],data[2],data[3],data[4])

    def menu_tarea(self):
        comando=1
        while comando!="0":
            persona=Persona(0,0)
            tarea=Tarea(0,0,0)
            print("""Seleccione una opcion:
            \t1) Editar tarea
            \t2) Borrar tarea
            \t3) Reasignar tarea
            \t0) Salir
            """)
            comando=input("Opcion: ")
            if comando == "1":
                self.update()
            elif comando == "2":
                self.delete()
                comando="0"
            elif comando == "3":
                persona.listar(self.proyecto)
                nuevo=input("ingresar persona: ")
                self.reasignar(nuevo)

def iniciar_sistema():
    comando=1
    proyecto=Proyecto(0,"nombre")
    while comando!="0":
        print("""Seleccione una opcion:
        \t1) Ingresar nuevo proyecto
        \t2) Seleccionar Proyecto
        \t3) Listar Proyectos
        \t0) Salir
        """)
        comando=input("Opcion: ")
        if comando == "1":
            proyecto.ingresar_informacion()
            proyecto.insert()
            proyecto=Proyecto(0, "nombre")
        elif comando == "2":
            proyecto=proyecto.seleccionar()
            proyecto.menu_proyecto()
            proyecto=Proyecto(0, "nombre")
        elif comando == "3":
            proyecto.listar()

iniciar_sistema()
