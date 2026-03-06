App del Tiempo en Python

Una aplicación de escritorio simple y visualmente atractiva para consultar el tiempo actual en cualquier ciudad del mundo. Hecha con Python, la librería Tkinter para la interfaz gráfica y la API de OpenWeatherMap para obtener los datos en tiempo real.

🌟 Características

Consulta el tiempo actual de cualquier ciudad.
Muestra temperatura, sensación térmica, descripción, humedad y velocidad del viento.
Interfaz gráfica de usuario (GUI) moderna y atractiva con imagen de fondo.
Muestra el icono del clima correspondiente.
Manejo de errores para ciudades no encontradas o problemas de conexión.
📸 Capturas de Pantalla / Demo
🛠️ Stack Tecnológico
Lenguaje: Python 3.11
Librerías:
requests - Para realizar peticiones a la API.
tkinter - Para la interfaz gráfica de usuario.
Pillow - Para el manejo de imágenes (iconos y fondo).
API: OpenWeatherMap
🚀 Cómo Ejecutar el Proyecto
Sigue estos sencillos pasos para tener una copia del proyecto funcionando en tu máquina local.

Clona el repositorio:
git clone https://github.com/TU_USUARIO/tiempo-app-python.gitcd tiempo-app-python
Crea un entorno virtual
python -m venv venv# En Windowsvenv\Scripts\activate# En macOS/Linuxsource venv/bin/activate
Instala las dependencias:
pip install -r requirements.txt
(Nota: Crea un archivo requirements.txt en tu carpeta con el comando pip freeze > requirements.txt antes de subirlo a GitHub para que esto funcione).
Consigue tu API Key:
Regístrate en OpenWeatherMap para obtener una API Key gratuita.
Configura tu API Key:
Abre el archivo main.py.
Reemplaza "TU_API_KEY_AQUI" con tu clave personal.
Añade una imagen de fondo:
Descarga una imagen de un paisaje/clima y guárdala en la carpeta del proyecto con el nombre background.jpg.
Ejecuta la aplicación:
python main.py
🤝 Contribuciones
Las contribuciones son siempre bienvenidas. Si tienes alguna idea para mejorar el proyecto, no dudes en abrir un issue o enviar un pull request.
