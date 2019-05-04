class Serializable:
    excluded=["indice","path","nombre_clase"]
    def __init__(self, indice, path, nombre_clase):
        self.indice=indice
        self.path=path
        self.nombre_clase=nombre_clase
    def __str__(self):
        valor=f"{self.indice}"
        for attribute, value in self.__dict__.items():
            if attribute in self.excluded:
                continue
            valor=f"{valor}\t{attribute.capitalize()}: {value}\n"
        return valor

    def serializar(self):
        valor=f"{self.indice}"
        for attribute, value in self.__dict__.items():
            if attribute in self.excluded:
                continue
            valor=f"{valor},{value}"
        return valor
    def update_file(self, array):
        try:
            archivo_escritura = open(self.path, mode='w')
            for registro in array:
                archivo_escritura.write(registro.serializar()+'\n')
            archivo_escritura.close()
        except Exception as error:
            print(f"Error ingreso masivo: {error}")
    def insert(self):
        try:
            registro=self.obtener_indice()
            self.indice=registro
            archivo_escritura = open(self.path, mode='a')
            archivo_escritura.write(self.serializar()+'\n')
            archivo_escritura.close()
        except Exception as error:
            print(f"Error ingreso: {error}")
    def obtener_registros(self):
        try:
            archivo_abierto = open(self.path)
            print(self.path)
            lineas_leidas = archivo_abierto.readlines()
            registros=[]
            for linea in lineas_leidas:
                attributos=linea.replace("\n","").split(',')
                registros.append(attributos)
            return registros
        except Exception as error:
            print(f"Error lectura: {error}")
    def obtener_indice(self):
            registros=self.obtener_registros()
            longitud=len(registros)
            if longitud > 0:
                return int(registros[longitud-1][0])+1
            return 1