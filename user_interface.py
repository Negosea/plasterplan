import tkinter as tk
from plasterplan import calculate_materials, calculate_profiles

def calculate():
    try:
        wall_area = float(entry_wall_area.get())
        wall_length = float(entry_wall_length.get())
        
        sheets = calculate_materials(wall_area)
        profiles = calculate_profiles(wall_length)
        
        result_label.config(text=f"Chapas: {sheets}, Perfis: {profiles}")
    except ValueError as e:
        result_label.config(text=f"Erro: {str(e)}")

app = tk.Tk()
app.title("Plaster Plan")

tk.Label(app, text="Área da Parede (m²):").pack()
entry_wall_area = tk.Entry(app)
entry_wall_area.pack()

tk.Label(app, text="Comprimento da Parede (m):").pack()
entry_wall_length = tk.Entry(app)
entry_wall_length.pack()

tk.Button(app, text="Calcular", command=calculate).pack()
result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
