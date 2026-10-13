import tkinter as tk

def mostrartela2():
    frame_tela1.pack_forget()
    frame_tela3.pack_forget()
    frame_tela2.pack(fill="both", expand=True)
def mostrartela1():
    frame_tela2.pack_forget()
    frame_tela3.pack_forget()
    frame_tela1.pack(fill="both", expand=True)
def mostrartela3():
    frame_tela2.pack_forget()
    frame_tela3.pack(fill="both", expand=True)
    frame_tela1.pack_forget()

app = tk.Tk();app.title("Aplicação Multitelas"); app.geometry("300x220")

frame_tela1 = tk.Frame(app)
tk.Label(frame_tela1, text="Tela 1", font=("Arial",14)).pack(pady=20)
tk.Button(frame_tela1, text="Ir para tela 2", command=mostrartela2).pack(pady=10)
tk.Button(frame_tela1, text="Ir para tela 3", command=mostrartela3).pack(pady=10)

frame_tela2 = tk.Frame(app)
tk.Label(frame_tela2, text="Tela 2", font=("Arial",14)).pack(pady=20)
tk.Button(frame_tela2, text="Ir para tela 1", command=mostrartela1).pack(pady=10)
tk.Button(frame_tela2, text="Ir para tela 3", command=mostrartela3).pack(pady=10)

frame_tela3 = tk.Frame(app)
tk.Label(frame_tela3, text="Tela 3", font=("Arial",14)).pack(pady=20)
tk.Button(frame_tela3, text="Ir para tela 2", command=mostrartela2).pack(pady=10)
tk.Button(frame_tela3, text="Ir para tela 1", command=mostrartela1).pack(pady=10)

frame_tela1.pack(fill="both",expand=True);app.mainloop()