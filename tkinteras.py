import tkinter as tk

def somar():
    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())
        lbl_res.config(text=f"Resultado: {n1 + n2}")
    except ValueError:
        lbl_res.config(text="Digite valores válidos")

app =tk.Tk()
app.title("Calculadora de Soma")
app.geometry("300x220")

entry1=tk.Entry(app);entry1.pack(pady=5)
entry2=tk.Entry(app);entry2.pack(pady=5)
bln = tk.Button(app,text="+", command=somar);bln.pack(pady=5)
lbl_res=tk.Label(app,text="Resultado:"); lbl_res.pack(pady=10)

app.mainloop()


