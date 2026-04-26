# Tarea 1 - Programación Orientada a Objetos

## Información del Estudiante

- **Nombre completo**: Rubén Mora
- **Carrera**: Ingeniería de Software
- **Semestre**: 4to

## Resumen de la Estructura del Caso de Estudio

Básicamente, desarrollamos un sistema en Python para gestionar el día a día de una biblioteca. Para que todo funcione de manera estructurada, aplicamos los principios de la Programación Orientada a Objetos (POO). El corazón del proyecto es mostrar, de forma práctica, cómo llevar el control de todo lo que pasa en la biblioteca: el inventario de libros, los estudiantes que los solicitan y el seguimiento detallado de cada préstamo.

### Estructura del Proyecto

- **main.py**: Es el punto de entrada del programa, desde donde se ejecuta todo y se puede ver cómo funciona el sistema en la práctica.
- **model/**: agrupa todas las clases que representan los datos del sistema:
  - `persona.py`: define la clase base `Persona`, que tiene los datos más generales de cualquier persona, como su nombre y apellido.
  - `estudiante.py`: Extiende esa clase con la clase `Estudiante`, que agrega información propia de un alumno, como su cédula y la carrera que estudia.
  - `libro.py`: contiene la clase `Libro`, con todo lo necesario para describir un libro: su título, autor, ISBN y si está disponible o no.
  - `prestamo.py`: define la clase `Prestamo`, que se encarga de vincular un libro con el estudiante que lo tiene, registrando tanto la fecha en que se lo llevó como la fecha en que debe devolverlo.
  - `biblioteca.py`: es el corazón del sistema: la clase `Biblioteca` centraliza todas las operaciones, desde registrar nuevos libros y estudiantes hasta gestionar los préstamos y devoluciones.
- **diagrams/**: guarda los diagramas de diseño del proyecto:
  - `diagrama_clases.puml`: un diagrama de clases escrito en formato PlantUML que muestra visualmente cómo se relacionan entre sí todas las clases del sistema.

### Funcionalidades Principales

- Registro de libros y estudiantes en la biblioteca.
- Búsqueda de libros por ISBN y estudiantes por cédula.
- Préstamo de libros con validación de disponibilidad.
- Devolución de libros.
- Gestión de préstamos activos.

Gracias a este diseño, cada parte del sistema tiene una función bien definida, lo que hace que el código sea más ordenado y fácil de entender.
