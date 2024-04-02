import socket
import win32api
import win32print
from glob import glob

file_name = ""  # Variable global para almacenar el nombre del archivo recibido

def start_server():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creamos un socket TCP/IP
        server_socket.bind(('Tu direccion IPv4', 12345))  # Enlazamos el socket al puerto 12345 (Cualquiera disponible)
        server_socket.listen(1)  # Ponemos el servidor en modo escucha
        print("Servidor escuchando en el puerto 12345...")

        while True:  # Bucle infinito para que el servidor esté siempre escuchando
            client_socket, address = server_socket.accept()  # Esperamos por una conexión
            print(f"Conexión establecida desde {address}")

            handle_client(client_socket, server_socket)  # Manejar la conexión con el cliente

    except Exception as e:
        print("Error en el servidor:", e)
        server_socket.close()  # Cerramos el socket del servidor en caso de error

def handle_client(client_socket, server_socket):
    try:
        data = b''  # Inicializamos una variable para almacenar los datos del archivo
        while True:
            chunk = client_socket.recv(4096)  # Recibimos los datos del archivo en bloques de 4096 bytes
            if not chunk:
                break
            data += chunk

        file_extension = ""
        if data.startswith(b'%PDF'):  # Determinamos el tipo de archivo
            file_extension = ".pdf"
        elif data.startswith(b'\xff\xd8\xff'):
            file_extension = ".jpg"
        # Agregar más comprobaciones de tipo de archivo según sea necesario

        global file_name
        file_name = "received_file" + file_extension  # Construimos el nombre del archivo recibido
        with open(file_name, "wb") as file:
            file.write(data)  # Guardamos el archivo recibido con la extensión correspondiente

        print("Archivo recibido y guardado correctamente.")
        print_file(file_name)  # Llamamos a la función para imprimir el archivo

    except Exception as e:
        print("Error al manejar la conexión:", e)

    finally:
        client_socket.close()  # Cerramos el socket del cliente

def print_file(file_name):
    try:
        all_printers = [printer[2] for printer in win32print.EnumPrinters(2)]  # Obtenemos una lista de todas las impresoras disponibles en el sistema
        win32print.SetDefaultPrinter(all_printers[0])  # Establecemos la impresora predeterminada

        file_dir = "Ruta donde guardaste el archivo.py" + file_name  # Construimos la ruta completa al archivo para imprimir
        for f in glob(file_dir, recursive=True):
            win32api.ShellExecute(0, "print", f, None, ".", 0)  # Imprimimos el archivo

        print("Imprimiendo..")

    except Exception as e:
        print("Error al seleccionar impresora o al imprimir")

start_server()
