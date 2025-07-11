import pickle, sys, os, random

def limpiar_pantalla():
    os.system("cls")

def mostrar_menu():
    print("----- SISTEMA DE TICKETS -----")
    print("1. Alta de Ticket")
    print("2. Leer Ticket")
    print("3. Salir de la app")

def alta_ticket():
    while True:
        limpiar_pantalla()
        print("----- ALTA DE TICKET -----")
        nombre = input("Ingresar nombre: ")
        sector = input("Ingresar sector: ")
        asunto = input("Ingresar el asunto del ticket: ")
        problema = input("Descirbir el problema: ")
        numero_ticket = random.randint(1000, 9999)
        ticket = {
            "num_ticket": numero_ticket,
            "nombre": nombre,
            "sector": sector,
            "asunto": asunto,
            "problema": problema
        }
        print("\n--- TICKET GENERADO ---")
        print(f"Numero de ticket: {numero_ticket}")
        print(f"Nombre: {nombre}")
        print(f"Sector: {sector}")
        print(f"Asunto: {asunto}")
        print(f"Problema: {problema}")
        print("------------------------")
        print("Recordar el numero de ticket para futuras consultas!")
        nombre_archivo = f"{numero_ticket}.pkl"
        with open(nombre_archivo, "wb") as archivo:
            pickle.dump(ticket, archivo)
        opcion = input("\nQueres crearr otro ticket? (s/n): ")
        if opcion.lower() != "s":
            break

def leer_ticket():
    while True:
        limpiar_pantalla()
        print("----- LECTURA DE TICKET -----")
        
        numero = input("Ingresar el numero de ticket: ")

        nombre_archivo = f"{numero}.pkl"

        if os.path.isfile(nombre_archivo):
            with open(nombre_archivo, "rb") as archivo:
                ticket = pickle.load(archivo)

            print("\n--- TICKET ENCONTRADO ---")
            print(f"Numeroo de ticket: {ticket['num_ticket']}")
            print(f"Nombre: {ticket['nombre']}")
            print(f"Sector: {ticket['sector']}")
            print(f"Asunto: {ticket['asunto']}")
            print(f"Problema: {ticket['problema']}")
            print("----------------------------")
        else:
            print("\nNo se encontro un ticket con ese numero")

        opcion = input("\nLeer otro ticket? (s/n): ")
        if opcion.lower() != "s":
            break


def main():
    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input("\nElegir una opcion (1-3): ")

        if opcion == "1":
            alta_ticket()
        elif opcion == "2":
            leer_ticket()  
        elif opcion == "3":
            confirmar = input("Vas a salir de la app? (s/n): ")
            if confirmar.lower() == "s":
                print("Saliendo del sistema...")
                sys.exit()
        else:
            input("Opcion invalida. Presionar Enter para continuar...")

if __name__ == "__main__":
    main()