# Aplicaciones Distribuidas - RPC
# Calculadora RPC

Esta calculadora se desarrolló en Python utilizando tecnologías RPC:

- XML-RPC
- gRPC

La aplicación permite realizar operaciones matemáticas de forma remota entre cliente y servidor.

---

# Funciones

## Calculadora XML-RPC

Operaciones disponibles:

- Suma
- Resta
- Multiplicación
- División

---

## Calculadora gRPC

Operaciones disponibles:

- Suma
- Resta
- Multiplicación
- División

---

# Requisitos

Instalar dependencias:
pip install grpcio grpcio-tools

# Estructura del proyecto
calculadora-rpc/
│
├── calculadora-grpc/
│   ├── calculadora.proto
│   ├── calculadora_pb2.py
│   ├── calculadora_pb2_grpc.py
│   ├── servidorGrpc.py
│   └── clienteGrpc.py
│
├── calculadora-xmlrpc/
│   ├── servidor_xmlrpc.py
│   └── cliente_xmlrpc.py
└── README.md

## Ejecutar Calculadora XML-RPC
1. Abrir terminal e ingresar a la carpeta:

cd calculadora-xmlrpc
2. Ejecutar servidor
py servidor_xmlrpc.py

3. Ejecutar cliente

Abrir otra terminal y ejecutar:

py cliente_xmlrpc.py

## Ejecutar Calculadora gRPC
1. Abrir terminal e ingresar a la carpeta:

cd calculadora-grpc

2. Ejecutar servidor
py servidorGrpc.py

4. Ejecutar cliente
Abrir otra terminal y ejecutar:
py clienteGrpc.py
