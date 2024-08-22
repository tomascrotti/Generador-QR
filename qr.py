import tkinter as tk
from tkinter import filedialog
import qrcode
from PIL import Image, ImageTk

class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.title("Generador QR")
        self.config(bg='#EFABA3')
        self.qr = None  # Inicializa el atributo self.qr

        # Dimensiones fijas para el QR y el Label
        self.qr_size = 300

        # TOP
        self.frame_url = tk.Frame(self)
        self.frame_url.pack(side=tk.TOP, padx=5, pady=5)
        self.lbl_url = tk.Label(self.frame_url, text="Ingrese la URL de la página")
        self.lbl_url.pack(side=tk.LEFT, padx=5, pady=10)
        self.ety_url = tk.Entry(self.frame_url, width=50)
        self.ety_url.pack(side=tk.LEFT, padx=5, pady=10)
        self.ety_url.bind("<KeyRelease>", self.update_qr)

        # CENTER
        self.frame_qr = tk.Frame(self, bg='#EFABA3')
        self.frame_qr.pack(side=tk.TOP, pady=10)
        self.lbl_qr = tk.Label(self.frame_qr, text="", bg='#EFABA3')
        self.lbl_qr.pack(side=tk.TOP, padx=5, pady=5)

        # BOTTOM
        self.frame_btn = tk.Frame(self)
        self.frame_btn.pack(side=tk.BOTTOM, pady=10)
        self.btn_guardar_qr = tk.Button(self.frame_btn, text="Guardar", command=self.guardar)
        self.btn_guardar_qr.pack(side=tk.RIGHT, padx=5, pady=5)
        self.btn_carpeta = tk.Button(self.frame_btn, text="Carpeta...", command=self.carpeta)
        self.btn_carpeta.pack(side=tk.LEFT, padx=5, pady=5)
        
    def update_qr(self, event=None):
        # Crea el objeto QRCode y lo almacena en self.qr
        self.qr = qrcode.QRCode(
            version=10,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=40,
            border=2
        )
        self.qr.add_data(self.ety_url.get())
        self.qr.make(fit=True)
        img = self.qr.make_image(fill_color='black', back_color='white')

        # Convertimos la imagen para usarla en Tkinter
        img = img.convert('RGB')
        
        # Escalamos la imagen al tamaño del Label usando LANCZOS
        img = img.resize((self.qr_size, self.qr_size), Image.LANCZOS)
        self.img_tk = ImageTk.PhotoImage(img)

        # Establecemos la imagen y fijamos el tamaño del Label
        self.lbl_qr.config(image=self.img_tk, width=self.qr_size, height=self.qr_size)

    def guardar(self):
        if self.qr:
            filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if filepath:
                img = self.qr.make_image(fill_color='black', back_color='white')
                img.save(filepath)

    def carpeta(self):
        self.directorio = filedialog.askdirectory(initialdir=r"C:\Usuarios\Usuario", title="Seleccione la carpeta")
        if not self.directorio:
            self.directorio = "."

if __name__ == '__main__':
    app = Ventana()
    app.mainloop()
