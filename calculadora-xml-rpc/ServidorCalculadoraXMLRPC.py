from xmlrpc.server import SimpleXMLRPCServer

server = SimpleXMLRPCServer(("localhost", 8001))

print("Servidor XML-RPC Calculadora ejecutándose...")


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):

    if b == 0:
        return "No se puede dividir para cero"

    return a / b


server.register_function(sumar, "sumar")
server.register_function(restar, "restar")
server.register_function(multiplicar, "multiplicar")
server.register_function(dividir, "dividir")

server.serve_forever()