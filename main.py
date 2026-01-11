
import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import io

# CONFIGURACIÓN 
API_KEY = "124c1c5a0938ea9c2bb157e1102fc70b"  
BACKGROUND_IMAGE_PATH = "imagenProyecto.jpg" 

# FUENTES Y COLORES (para texto sobre imagen) 
FUENTE_TITULO = ("Helvetica", 26, "bold")
FUENTE_PRINCIPAL = ("Helvetica", 14)
FUENTE_SECUNDARIA = ("Helvetica", 11)
COLOR_TEXTO_CLARO = "#000000" # Blanco
COLOR_TEXTO_SUAVE = "#000000" # Blanco grisáceo

def consultar_tiempo(ciudad):
    if not ciudad:
        return None
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es"
    try:
        respuesta = requests.get(URL)
        if respuesta.status_code == 200:
            return respuesta.json()
        else:
            return None
    except requests.exceptions.RequestException:
        return None

# LÓGICA DE LA INTERFAZ GRÁFICA 
def mostrar_resultado():
    ciudad = entrada_ciudad.get()
    datos = consultar_tiempo(ciudad)

    if datos:
        # Actualizar etiquetas
        etiqueta_temp.config(text=f"{datos['main']['temp']}°C")
        etiqueta_sensacion.config(text=f"Sensación: {datos['main']['feels_like']}°C")
        etiqueta_descripcion.config(text=datos['weather'][0]['description'].capitalize())
        etiqueta_humedad.config(text=f"Humedad: {datos['main']['humidity']}%")
        etiqueta_viento.config(text=f"Viento: {datos['wind']['speed']} m/s")

        # Cargar icono
        icono_code = datos['weather'][0]['icon']
        icono_url = f"http://openweathermap.org/img/wn/{icono_code}@4x.png" # Usamos @4x para más calidad
        
        try:
            respuesta_icono = requests.get(icono_url, stream=True)
            respuesta_icono.raw.decode_content = True
            imagen_data = io.BytesIO(respuesta_icono.content)
            imagen = Image.open(imagen_data)
            # Redimensionar el icono para que no sea gigante
            imagen = imagen.resize((120, 120), Image.Resampling.LANCZOS)
            foto = ImageTk.PhotoImage(imagen)
            
            etiqueta_icono.config(image=foto)
            etiqueta_icono.image = foto
        except Exception as e:
            print(f"Error al cargar el icono: {e}")

    else:
        messagebox.showerror("Error", "No se pudo encontrar el tiempo para esa ciudad.")
        # Limpiar etiquetas
        etiqueta_temp.config(text="--°C")
        etiqueta_sensacion.config(text="Sensación: --°C")
        etiqueta_descripcion.config(text="Desconocido")
        etiqueta_humedad.config(text="Humedad: --%")
        etiqueta_viento.config(text="Viento: -- m/s")
        etiqueta_icono.config(image="")

# CREACIÓN DE LA VENTANA Y WIDGETS
ventana_principal = tk.Tk()
ventana_principal.title("App del Tiempo")
ventana_principal.geometry("450x600")
ventana_principal.resizable(False, False)

# CARGAR Y PONER LA IMAGEN DE FONDO
try:
    bg_image_pil = Image.open(BACKGROUND_IMAGE_PATH)
    bg_image = ImageTk.PhotoImage(bg_image_pil)
    
    etiqueta_fondo = tk.Label(ventana_principal, image=bg_image)
    etiqueta_fondo.place(x=0, y=0, relwidth=1, relheight=1) # Cubre toda la ventana
except FileNotFoundError:
    messagebox.showerror("Error de Fondo", f"No se encontró la imagen '{BACKGROUND_IMAGE_PATH}'. Asegúrate de que está en la misma carpeta que el script.")
    ventana_principal.destroy()
    exit()




# Título
etiqueta_titulo = tk.Label(ventana_principal, text="App del Tiempo", font=FUENTE_TITULO, fg=COLOR_TEXTO_CLARO)
etiqueta_titulo.place(relx=0.5, rely=0.08, anchor="center")

# Entrada de ciudad
frame_entrada = tk.Frame(ventana_principal, highlightbackground=COLOR_TEXTO_CLARO, highlightthickness=1)
frame_entrada.place(relx=0.5, rely=0.18, anchor="center", width=300, height=40)

entrada_ciudad = tk.Entry(frame_entrada, font=FUENTE_PRINCIPAL, bd=0, highlightthickness=0)
entrada_ciudad.pack(fill="both", expand=True, padx=2, pady=2)
entrada_ciudad.bind("<Return>", lambda event: mostrar_resultado())

boton_consultar = tk.Button(ventana_principal, text="Consultar", command=mostrar_resultado, font=FUENTE_PRINCIPAL, bg="#3498db", fg="white", bd=0, activebackground="#2980b9")
boton_consultar.place(relx=0.5, rely=0.26, anchor="center", width=150, height=40)

# ÁREA DE RESULTADOS 
frame_resultados = tk.Frame(ventana_principal)
frame_resultados.place(relx=0.5, rely=0.5, anchor="center")

etiqueta_icono = tk.Label(frame_resultados)
etiqueta_icono.grid(row=0, column=0, padx=10)

etiqueta_temp = tk.Label(frame_resultados, text="--°C", font=("Helvetica", 48, "bold"), fg=COLOR_TEXTO_CLARO)
etiqueta_temp.grid(row=0, column=1)

# Resto de información
etiqueta_descripcion = tk.Label(ventana_principal, text="Desconocido", font=FUENTE_PRINCIPAL, fg=COLOR_TEXTO_SUAVE)
etiqueta_descripcion.place(relx=0.5, rely=0.68, anchor="center")

etiqueta_sensacion = tk.Label(ventana_principal, text="Sensación: --°C", font=FUENTE_SECUNDARIA, fg=COLOR_TEXTO_SUAVE)
etiqueta_sensacion.place(relx=0.5, rely=0.75, anchor="center")

etiqueta_humedad = tk.Label(ventana_principal, text="Humedad: --%", font=FUENTE_SECUNDARIA, fg=COLOR_TEXTO_SUAVE)
etiqueta_humedad.place(relx=0.5, rely=0.82, anchor="center")

etiqueta_viento = tk.Label(ventana_principal, text="Viento: -- m/s", font=FUENTE_SECUNDARIA, fg=COLOR_TEXTO_SUAVE)
etiqueta_viento.place(relx=0.5, rely=0.89, anchor="center")


# Iniciar el bucle principal
ventana_principal.mainloop()