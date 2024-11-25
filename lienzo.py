from tkinter import filedialog, colorchooser
from PIL import Image, ImageTk, ImageDraw
import os

class PinturaMagica:
    """
    Clase principal de la aplicación Pintura Mágica.
    Gestiona las herramientas de dibujo y los eventos.
    """
    def __init__(self, canvas, herramientas):
        self.canvas = canvas
        self.herramientas = herramientas
        self.color = "black"
        self.tamaño_pincel = 5
        self.dibujo = []
        self.dibujo_historial = []
        self.dibujo_redo = []
        self.modo_borrador = False

        # Eventos para el lienzo
        self.canvas.bind("<B1-Motion>", self.pintar)

        # Configurar eventos para las herramientas
        self.herramientas["color"].configure(command=self.seleccionar_color)
        self.herramientas["limpiar"].configure(command=self.borrar_todo)
        self.herramientas["guardar"].configure(command=self.guardar_dibujo)
        self.herramientas["fondo"].configure(command=self.cambiar_fondo)
        self.herramientas["borrador"].configure(command=self.activar_borrador)
        self.herramientas["cargar"].configure(command=self.cargar_imagen)
        self.herramientas["deshacer"].configure(command=self.deshacer)
        self.herramientas["rehacer"].configure(command=self.rehacer)
        self.herramientas["slider"].configure(command=self.actualizar_tamaño)

    def seleccionar_color(self):
        color_seleccionado = colorchooser.askcolor(color=self.color)[1]
        if color_seleccionado:
            self.color = color_seleccionado

    def borrar_todo(self):
        self.canvas.delete("all")
        self.dibujo = []
        self.dibujo_historial.clear()
        self.dibujo_redo.clear()

    def guardar_dibujo(self):
        archivo_guardar = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if archivo_guardar:
            img = Image.new("RGB", (800, 500), color=self.canvas.cget("bg"))
            draw = ImageDraw.Draw(img)
            for item in self.dibujo:
                draw.line([item[0], item[1], item[2], item[3]], fill=item[4], width=self.tamaño_pincel)
            img.save(archivo_guardar)

    def cambiar_fondo(self):
        color_fondo = colorchooser.askcolor(color=self.canvas.cget("bg"))[1]
        if color_fondo:
            self.canvas.config(bg=color_fondo)

    def activar_borrador(self):
        self.modo_borrador = not self.modo_borrador
        self.herramientas["borrador"].configure(fg_color="red" if self.modo_borrador else "green")

    def cargar_imagen(self):
        archivo_imagen = filedialog.askopenfilename(filetypes=[("Imágenes", "*.png;*.jpg;*.jpeg")])
        if archivo_imagen:
            img = Image.open(archivo_imagen)
            img = img.resize((800, 500), Image.Resampling.LANCZOS)
            self.imagen_tk = ImageTk.PhotoImage(img)
            self.canvas.create_image(400, 250, image=self.imagen_tk, anchor="center")

    def pintar(self, evento):
        color_actual = self.color if not self.modo_borrador else self.canvas.cget("bg")
        x1, y1 = evento.x - self.tamaño_pincel, evento.y - self.tamaño_pincel
        x2, y2 = evento.x + self.tamaño_pincel, evento.y + self.tamaño_pincel
        self.canvas.create_oval(x1, y1, x2, y2, fill=color_actual, outline=color_actual)
        self.dibujo.append([x1, y1, x2, y2, color_actual])
        self.dibujo_historial.append([x1, y1, x2, y2, color_actual])
        self.dibujo_redo.clear()

    def actualizar_tamaño(self, valor):
        self.tamaño_pincel = int(valor)

    def deshacer(self):
        if self.dibujo_historial:
            item = self.dibujo_historial.pop()
            self.dibujo_redo.append(item)
            self.canvas.delete("all")
            for item in self.dibujo_historial:
                self.canvas.create_oval(item[0], item[1], item[2], item[3], fill=item[4], outline=item[4])

    def rehacer(self):
        if self.dibujo_redo:
            item = self.dibujo_redo.pop()
            self.dibujo_historial.append(item)
            self.canvas.create_oval(item[0], item[1], item[2], item[3], fill=item[4], outline=item[4])
