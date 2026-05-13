import xmlrpc.client

proxy = xmlrpc.client.ServerProxy(
    "http://localhost:8001/"
)

while True:

    print("\n--- CALCULADORA XML-RPC ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "5":
        print("Saliendo...")
        break

    if opcion not in ["1", "2", "3", "4"]:
        print("Opción inválida")
        continue

    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))

    if opcion == "1":
        print("Resultado:", proxy.sumar(a, b))

    elif opcion == "2":
        print("Resultado:", proxy.restar(a, b))

    elif opcion == "3":
        print("Resultado:", proxy.multiplicar(a, b))

    elif opcion == "4":
        print("Resultado:", proxy.dividir(a, b))