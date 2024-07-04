import http.server
import socketserver
import webbrowser
import os
import threading

# Directorio del proyecto
PROJECT_DIR = "D:\Empresa\WEB"

# Puerto que quieres abrir
PORT = 8000

# Cambia al directorio del proyecto
os.chdir(PROJECT_DIR)

# Configurar el servidor HTTP
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

# Función para iniciar el servidor
def start_server():
    print(f"Servidor HTTP abierto en el puerto {PORT}.")
    httpd.serve_forever()

# Iniciar el servidor en un hilo separado
server_thread = threading.Thread(target=start_server)
server_thread.daemon = True
server_thread.start()

# Espera un momento para asegurarse de que el servidor esté en funcionamiento
import time
time.sleep(2)

# Abre el navegador predeterminado apuntando al index.html
webbrowser.open(f"http://localhost:{PORT}/index.html")

# Mantener el script en ejecución
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nCerrando el servidor.")
    httpd.shutdown()
