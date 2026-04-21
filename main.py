# main.py

from model.libro import Libro
from model.estudiante import Estudiante
from model.biblioteca import Biblioteca

def main():

    # ─── Crear la biblioteca ───

    print("=" * 60)
    print(" Bienvenido a la Biblioteca Virtual UNEMI")
    print("=" * 60)

    biblioteca = Biblioteca("Biblioteca UNEMI")
    print(f"\n{biblioteca}\n")

    # ─── Registrar libros (RF-01) ───

    print("─── Registro de Libros ───")
    libro1 = Libro("978-3-16-148410-0", "El Principito", "Antoine de Saint-Exupéry")
    libro2 = Libro("978-0-14-044913-6", "Don Quijote de la Mancha", "Miguel de Cervantes")
    libro3 = Libro("978-0-452-28423-4", "Cien Años de Soledad", "Gabriel García Márquez")

    biblioteca.registrar_libro(libro1)
    biblioteca.registrar_libro(libro2)
    biblioteca.registrar_libro(libro3)

    # ─── Registrar estudiantes (RF-02) ───

    print("\n─── Registro de Estudiantes ───")
    est1 = Estudiante("1234567890", "Juan", "Pérez", "Ingeniería en Sistemas")
    est2 = Estudiante("0987654321", "María", "Gómez", "Ingeniería Industrial")
    
    biblioteca.registrar_estudiante(est1)
    biblioteca.registrar_estudiante(est2)

    # ─── Estado actual ───

    print(f"\n{biblioteca}\n")

    # ─── Realizar préstamos (RF-03 y RF-04) ───

    print("── Realizando préstamos ──")
    resultado = biblioteca.prestar_libro("978-3-16-148410-0", "1234567890", "2024-06-01", "2024-06-15")
    print(resultado)
    resultado = biblioteca.prestar_libro("978-0-14-044913-6", "0987654321", "2024-06-02", "2024-06-16")
    print(resultado)
    resultado = biblioteca.prestar_libro("978-3-16-148410-0", "0987654321", "2024-06-03", "2024-06-17")
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
    resultado = biblioteca.devolver_libro("978-3-16-148410-0", "1234567890")
    print(resultado)

    # ─── Verificar que el libro está disponible nuevamente ───

    print("\n── Verificando disponibilidad del libro devuelto ──")
    print(f" {libro1}")

    # ─── Consultar préstamos activos después de devolución ───

    print("\n── Consultando préstamos activos para Juan Pérez ──")
    prestamos_juan = biblioteca.consultar_prestamos_activos("1234567890")
    if prestamos_juan:
        for prestamo in prestamos_juan:
            print(f" → {prestamo}")
    else:
        print(" No hay préstamos activos para Juan Pérez.")

    # ─── Ahora el libro puede prestarse de nuevo ───

    print("\n── Intentando prestar el libro nuevamente ──")
    resultado = biblioteca.prestar_libro("978-3-16-148410-0", "0987654321", "2024-06-10", "2024-06-24")
    print(resultado)

    # ─── Estado final ───

    print(f"\n{'=' * 60}")
    print(f"  {biblioteca}")
    print(f"{'=' * 60}")

if __name__ == "__main__":
    main()
