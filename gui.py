import tkinter as tk 
from presser import Macro
import threading


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AutoClickerOP")
        self.root.geometry('400x400')
        self.state = True
        
        self.macro = Macro()
        
        # Configuración para el intervalo de tiempo en ms
        tk.Label(self.root, text="Intervalo (ms):").pack()
        self.interval_entry = tk.Entry(self.root)
        self.interval_entry.pack()
        
        # Configuración para el botón del mouse (izquierdo por defecto)
        self.click_type = tk.StringVar(value="left")
        tk.Radiobutton(self.root, text="Izquierdo", variable=self.click_type, value="left").pack()
        tk.Radiobutton(self.root, text="Derecho", variable=self.click_type, value="right").pack()

        # Botón para iniciar el clic automático
        self.start_button = tk.Button(self.root, text="Iniciar", command=self.start_click)
        self.start_button.pack()

        # Botón para detener el clic automático
        self.stop_button = tk.Button(self.root, text="Detener", command=self.stop_click, state=tk.DISABLED)
        self.stop_button.pack()
    
    def start_click(self):
        try:
            interval = max(int(self.interval_entry.get()), 1)  # Asegúrate de tener al menos 1ms de intervalo
        except ValueError:
            interval = 1000  # Valor por defecto si la conversión falla
        click_type = self.click_type.get()
        
        self.stop_button.config(state=tk.NORMAL)
        self.start_button.config(state=tk.DISABLED)
        
    
        
        # Hilo de click
        threading.Thread(target=lambda: self.macro.mouse_click(interval, click_type, self.state)).start()
        print(f"Iniciado: Intervalo {interval} ms, Botón {click_type}")

    def stop_click(self):
        # Aquí se detendría el clic automático adecuadamente
        # NO ESTA TERMINADA
        self.state = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

        print("Detenido")

    def run(self):
        self.root.mainloop()