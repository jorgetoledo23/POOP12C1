class Doctor:
    Rut = ""
    Especialidad = ""
    Nombre = ""
    Apellido = ""
    Telefono = ""
    Correo = ""
    Direccion = ""

    def ObtenerInformacion(self):
        return f"Rut: { self.Rut }, Nombre: {self.Nombre}, Apellido: {self.Apellido}"
        #return "Rut: " + self.Rut + " , Nombre: " + self.Nombre + " , Apellido: " + self.Apellido

    #Metodo Constructor => Se ejecuta cuando se crea la Instancia
    def __init__(self, rut, nombre, apellido):
        self.Rut = rut
        self.Nombre = nombre
        self.Apellido = apellido











class Animal:
    NombreCientifico = ""
    NombreComun = ""
    Habitat = ""
    Especie = ""
    enPeligroExtincion = False

class SmartPhone:
    Marca = ""
    Modelo = ""
    SistemaOperativo = ""
    TamañoPantall = ""
    Procesador = ""
    Ram = ""
    Almacenamiento = ""