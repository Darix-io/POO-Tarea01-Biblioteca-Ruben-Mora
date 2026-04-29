from model.libro import Libro
from model.estudiante import Estudiante
from model.prestamo import Prestamo

class Biblioteca:
    def __init__(self, nombre: str):
        self._nombre = nombre
        self._libros = []
        self._estudiantes = []
        self._prestamos = []

    def registrar_libro(self, libro: Libro) -> None:
        self._libros.append(libro)
        print(f" Libro registrado: {libro.titulo}")

    def registrar_estudiante(self, estudiante: Estudiante) -> None:
        self._estudiantes.append(estudiante)
        print(f" Estudiante registrado: {estudiante.nombre} {estudiante.apellido}")

    def _buscar_libro(self, isbn: str) -> Libro:
        for libro in self._libros:
            if libro.isbn == isbn:
                return libro
        return None
    
    def _buscar_estudiante(self, cedula: str) -> Estudiante:
        for estudiante in self._estudiantes:
            if estudiante.cedula == cedula:
                return estudiante
        return None  
    
    def prestar_libro(self, isbn: str, cedula: str, fecha_prestamo: str, fecha_devolucion: str) -> str:
        libro = self._buscar_libro(isbn)
        if libro is None:
            return f"Libro no encontrado. {isbn}"
        
        estudiante = self._buscar_estudiante(cedula)
        if estudiante is None:
            return f"Estudiante no encontrado. {cedula}"

        if not libro.disponible:
            return f"Libro no disponible. {libro.titulo} ya está prestado."
        
        libro.prestar()
        prestamo = Prestamo(libro, estudiante, fecha_prestamo, fecha_devolucion)
        self._prestamos.append(prestamo)
        return f"Préstamo registrado; '{libro.titulo}' → {estudiante.nombre}"
    
    def devolver_libro(self, isbn: str, cedula: str) -> str:
        for prestamo in self._prestamos:
            if (prestamo.libro.isbn == isbn and
                prestamo.estudiante.cedula == cedula and
                prestamo.activo):
                prestamo.registrar_devolucion()
                return f"Libro devuelto: '{prestamo.libro.titulo}'"
    
        return "No se encontró un préstamo activo con esos datos."
    
    def consultar_prestamos_activos(self, cedula: str) -> list:
        activos = []
        for prestamo in self._prestamos:
            if prestamo.estudiante.cedula == cedula and prestamo.activo:
                activos.append(prestamo)
        return activos
        
    @property
    def libros(self) -> list:
        return self._libros
    
    @property
    def estudiantes(self) -> list:
        return self._estudiantes