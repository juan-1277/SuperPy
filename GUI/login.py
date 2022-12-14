import tkinter as tk
from tkinter import ttk, messagebox
from GUI.master import Main

from Login.usuario import Usuario

class LoginVentana(tk.Tk):
    def __init__(self):
        super().__init__()
        # ventana principal
        self.geometry('310x235')
        self.title('Login')
        self.iconbitmap('GUI/iconos/tienda.ico')
        self.resizable(0,0)
        # configuración del grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        
        # Creamos los componentes
        self._crear_componentes()

    # Definir el método crear_componentes
    def _crear_componentes(self):
        
        form_etiqueta = ttk.Label(self, text='SUPERPY', font=("Arial", 15))
        form_etiqueta.grid(row=0, column=0, columnspan=2,padx=10, pady=10)
        
        # usuario
        usuario_etiqueta = ttk.Label(self, text='Usuario:')
        usuario_etiqueta.grid(row=1, column=0, sticky=tk.E, pady=5)
        self.usuario_entrada = ttk.Entry(self)
        self.usuario_entrada.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        # password
        password_etiqueta = ttk.Label(self, text='Password:')
        password_etiqueta.grid(row=2, column=0, sticky=tk.E, pady=5)
        self.password_entrada = ttk.Entry(self, show='*')
        self.password_entrada.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

        # boton Login
        login_boton = ttk.Button(self, text='Login', command = self._login)
        login_boton.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
        
        #Registrarse
        ttk.Style().configure("TButton", padding=6, relief="flat",background="#ccc")
        registrar_boton = ttk.Button(self, text='Registrarse')
        registrar_boton.grid(row=10, column=1,sticky=tk.E, padx=10, pady=10)


    def _login(self):
        usuario = Usuario()
        if (usuario.login(self.usuario_entrada.get(),self.password_entrada.get())):
            """ messagebox.showinfo('Datos Login',
                f'usuario: {self.usuario_entrada.get()}, Password: {self.password_entrada.get()}') """
            
            messagebox.showinfo("Inicio", "Inicio de sesión exitoso")
            self.withdraw()
            app = Main()
            app.mainloop()
        else:
            messagebox.showerror('ERROR',
                f'Usuario o password Incorrecto')