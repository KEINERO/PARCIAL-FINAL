import customtkinter as ctk
from lienzo import PinturaMagica
from ui import crear_interfaz

if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Pintura Mágica")
    root.geometry("800x600")

    canvas, herramientas = crear_interfaz(root)
    app = PinturaMagica(canvas, herramientas)

    root.mainloop()
