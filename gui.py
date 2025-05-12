import tkinter as tk
from tkinter import ttk, messagebox

class ParkingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Parqueadero")
        self.root.geometry("700x450")
        
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill="both", padx=10, pady=10)
        
        self.crear_tab_ingreso()
        self.crear_tab_salida()
        self.crear_tab_historial()
    
    def crear_tab_ingreso(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Ingreso")
        
        ttk.Label(tab, text="Placa:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.placa_ingreso = ttk.Entry(tab, width=20)
        self.placa_ingreso.grid(row=0, column=1, padx=10, pady=5)
        
        ttk.Label(tab, text="Hora de ingreso (0-23):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.hora_ingreso = ttk.Entry(tab, width=5)
        self.hora_ingreso.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        
        ttk.Label(tab, text="Tipo:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.tipo_vehiculo = ttk.Combobox(tab, values=["Carro", "Moto"], state="readonly", width=10)
        self.tipo_vehiculo.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        
        ttk.Button(tab, text="Registrar Ingreso").grid(
            row=3, column=0, columnspan=2, pady=15
        )
    
    def crear_tab_salida(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Salida")
        
        ttk.Label(tab, text="Placa:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.placa_salida = ttk.Entry(tab, width=20)
        self.placa_salida.grid(row=0, column=1, padx=10, pady=5)
        
        ttk.Label(tab, text="Hora de salida (0-23):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.hora_salida = ttk.Entry(tab, width=5)
        self.hora_salida.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        
        ttk.Button(tab, text="Registrar Salida").grid(
            row=2, column=0, columnspan=2, pady=15
        )
    
    def crear_tab_historial(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Historial")
        
        frame_tree = ttk.Frame(tab)
        frame_tree.pack(expand=True, fill="both", padx=10, pady=10)
        
        scroll_y = ttk.Scrollbar(frame_tree, orient="vertical")
        scroll_y.pack(side="right", fill="y")
        
        self.tree = ttk.Treeview(
            frame_tree,
            columns=("placa", "tipo", "entrada", "salida", "horas", "valor"),
            show="headings",
            yscrollcommand=scroll_y.set,
            height=15
        )
        
        columnas = [
            ("Placa", 100),
            ("Tipo", 80),
            ("Entrada", 80),
            ("Salida", 80),
            ("Horas", 60),
            ("Valor", 100)
        ]
        
        for col, width in columnas:
            self.tree.heading(col.lower(), text=col)
            self.tree.column(col.lower(), width=width, anchor="center")
        
        self.tree.pack(expand=True, fill="both")
        scroll_y.config(command=self.tree.yview)
        
        frame_botones = ttk.Frame(tab)
        frame_botones.pack(pady=10)
        
        ttk.Button(frame_botones, text="Actualizar").pack(side="left", padx=5)
        ttk.Button(frame_botones, text="Exportar CSV").pack(side="left", padx=5)