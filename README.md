# TCP File Printer

El TCP File Printer es un servidor que escucha en un puerto TCP/IP específico para recibir archivos y luego imprimirlos en una impresora predeterminada del sistema. Este servidor está diseñado para ejecutarse en sistemas Windows y utiliza la biblioteca win32print para interactuar con las impresoras.

## Funcionalidades
- Escucha en un puerto TCP/IP específico para conexiones entrantes.
- Recibe archivos a través de la conexión TCP/IP.
- Detecta automáticamente el tipo de archivo recibido (PDF, JPEG u otros).
- Guarda los archivos recibidos en el sistema de archivos.
- Imprime los archivos recibidos en la impresora predeterminada del sistema.

## Requisitos
- Python 3.x instalado en el sistema.
- Biblioteca win32print instalada (disponible a través de PyWin32).
```sh
pip install pywin32
```
- Impresora instalada y configurada en el sistema Windows.

## Uso
1) Clona o descarga este repositorio en tu sistema.
2) Asegúrate de tener Python 3.x y la biblioteca win32print instalados.
3) Coloca tu direccion IPv4 y un puerto disponible en
```sh
server_socket.bind(('Tu direccion IPv4', 12345))  # Enlazamos el socket al puerto 12345 (Cualquiera disponible)
```
4) Coloca la url donde guardaste el archivo printer.py (y donde se guardaran los archivos recibidos)
```sh
file_dir = "Ruta donde guardaste el archivo.py" + file_name
```
5) Ejecuta el script server.py para iniciar el servidor.
6) Envía archivos al servidor utilizando una conexión TCP/IP.
7) El servidor imprimirá automáticamente los archivos recibidos en la impresora predeterminada.

## Opcional: Convertir el script .py a .exe

Si deseas distribuir tu aplicación como un archivo ejecutable de Windows (.exe), puedes utilizar la herramienta `auto-py-to-exe`. Esta herramienta te permite convertir fácilmente un script de Python en un archivo ejecutable independiente.

### Pasos para convertir el script .py a .exe:

1. Instala `auto-py-to-exe` ejecutando el siguiente comando en tu terminal o línea de comandos:

```sh
pip install auto-py-to-exe
```

2. Una vez instalado, ejecuta `auto-py-to-exe` ejecutando el siguiente comando en tu terminal o línea de comandos:

```sh
auto-py-to-exe
```

3. Se abrirá una interfaz gráfica donde podrás configurar las opciones de conversión. Puedes seleccionar el script `.py` que deseas convertir, así como ajustar otras configuraciones según sea necesario.

4. Después de configurar las opciones, haz clic en el botón "Convertir .py a .exe" o similar para iniciar el proceso de conversión.

5. Una vez completada la conversión, encontrarás el archivo ejecutable `.exe` en el directorio de salida especificado.

¡Ahora tienes un archivo ejecutable de Windows que puedes distribuir y ejecutar en otros sistemas sin necesidad de instalar Python!
