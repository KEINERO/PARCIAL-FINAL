import customtkinter as ctk

def crear_interfaz(root):
    canvas = ctk.CTkCanvas(root, bg="white", width=800, height=500)
    canvas.pack(fill="both", expand=True)

    barra_herramientas = ctk.CTkFrame(root, fg_color="lightgray", height=100)
    barra_herramientas.pack(fill="x", side="bottom")

    herramientas = {
        "color": ctk.CTkButton(barra_herramientas, text="Color", fg_color="green"),
        "limpiar": ctk.CTkButton(barra_herramientas, text="Limpiar", fg_color="green"),
        "guardar": ctk.CTkButton(barra_herramientas, text="Guardar", fg_color="green"),
        "fondo": ctk.CTkButton(barra_herramientas, text="Fondo", fg_color="green"),
        "borrador": ctk.CTkButton(barra_herramientas, text="Borrador", fg_color="green"),
        "cargar": ctk.CTkButton(barra_herramientas, text="Cargar Imagen", fg_color="green"),
        "deshacer": ctk.CTkButton(barra_herramientas, text="Deshacer", fg_color="green"),
        "rehacer": ctk.CTkButton(barra_herramientas, text="Rehacer", fg_color="green"),
        "slider": ctk.CTkSlider(barra_herramientas, from_=1, to=20, fg_color="green")
    }

    for boton in herramientas.values():
        boton.pack(side="left", padx=5, pady=10)
    herramientas["slider"].set(5)

    return canvas, herramientas
