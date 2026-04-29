# main.py

from model.libro import Libro
from model.estudiante import Estudiante
from model.biblioteca import Biblioteca
from faker import Faker

def main():

    # ─── Crear la biblioteca ───

    print("=" * 60)
    print(" Bienvenido a la Biblioteca Virtual UNEMI")
    print("=" * 60)

    biblioteca = Biblioteca("Biblioteca UNEMI")
    print(f"\n{biblioteca}\n")

    # ─── Inicializar Faker ───
    fake = Faker('es_ES')  # Usar español para nombres y datos

    # ─── Registrar libros aleatorios (RF-01) ───

    print("─── Registro de Libros Aleatorios ───")
    for _ in range(5):  # Generar 5 libros aleatorios
        isbn = fake.isbn13()
        titulo = fake.sentence(nb_words=4).rstrip('.')  # Título corto
        autor = fake.name()
        libro = Libro(isbn, titulo, autor)
        biblioteca.registrar_libro(libro)
        print(f"Registrado: {libro}")

    # ─── Registrar estudiantes aleatorios (RF-02) ───

    print("\n─── Registro de Estudiantes Aleatorios ───")
    carreras = ["Ingeniería en Sistemas", "Ingeniería Industrial", "Medicina", "Derecho", "Arquitectura"]
    for _ in range(3):  # Generar 3 estudiantes aleatorios
        cedula = str(fake.random_number(digits=10, fix_len=True))  # Cédula de 10 dígitos
        nombre = fake.first_name()
        apellido = fake.last_name()
        carrera = fake.random_element(carreras)
        estudiante = Estudiante(cedula, nombre, apellido, carrera)
        biblioteca.registrar_estudiante(estudiante)
        print(f"Registrado: {estudiante}")

    # ─── Estado actual ───

    print(f"\n{biblioteca}\n")

    # ─── Realizar préstamos (RF-03 y RF-04) ───

    print("── Realizando préstamos ──")
    # Obtener listas de libros y estudiantes registrados
    libros = [libro.isbn for libro in biblioteca.libros]
    estudiantes = [est.cedula for est in biblioteca.estudiantes]
    
    if len(libros) >= 2 and len(estudiantes) >= 2:
        resultado = biblioteca.prestar_libro(libros[0], estudiantes[0], "2024-06-01", "2024-06-15")
        print(resultado)
        resultado = biblioteca.prestar_libro(libros[1], estudiantes[1], "2024-06-02", "2024-06-16")
        print(resultado)
        if len(libros) > 2 and len(estudiantes) > 1:
            resultado = biblioteca.prestar_libro(libros[0], estudiantes[1], "2024-06-03", "2024-06-17")
            print(resultado)

    # ─── Intentar prestar un libro ya prestado (RF-04: validación) ───

    print("\n── Intentando prestar un libro ya prestado ──")
    resultado = biblioteca.prestar_libro("978-3-16-148410-0", "0987654321", "2024-06-03", "2024-06-17")
    print(resultado)

    # ─── Consultar préstamos activos (RF-06) ───

    print("\n── Consultando préstamos activos para Juan Pérez ──")
    activos_juan = biblioteca.consultar_prestamos_activos("1234567890")
    for prestamo in activos_juan:
        print(f" → {prestamo} ")


    # ─── Devolver un libro (RF-05) ───

    print("\n── Devolviendo un libro ──")
    resultado = biblioteca.devolver_libro(libros[0], estudiantes[0])
    print(resultado)

    # ─── Verificar que el libro está disponible nuevamente ───

    print("\n── Verificando disponibilidad del libro devuelto ──")
    print(f" {biblioteca.libros[0]}")

    # ─── Consultar préstamos activos después de devolución ───

    print("\n── Consultando préstamos activos para " + biblioteca.estudiantes[0].nombre + " " + biblioteca.estudiantes[0].apellido + " ──")
    prestamos_activos = biblioteca.consultar_prestamos_activos(estudiantes[0])
    if prestamos_activos:
        for prestamo in prestamos_activos:
            print(f" → {prestamo}")
    else:
        print(" No hay préstamos activos.")

    # ─── Ahora el libro puede prestarse de nuevo ───

    print("\n── Intentando prestar el libro nuevamente ──")
    resultado = biblioteca.prestar_libro(libros[0], estudiantes[1], "2024-06-10", "2024-06-24")
    print(resultado)

    # ─── Estado final ───

    print(f"\n{'=' * 60}")
    print(f"  {biblioteca}")
    print(f"{'=' * 60}")

if __name__ == "__main__":
    main()
