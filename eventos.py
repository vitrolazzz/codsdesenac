import tkinter as tk

def multiplicar():
    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())
        label.config(text=f"O resultado é {n1*n2}")
    except ValueError:
        label.config(text="Digite número válido!")

janela = tk.Tk()
janela.title("Cálculo")
janela.geometry("350x350")
janela.configure(bg="#00F128")

label = tk.Label(
    janela,
    text="Digite dois números para multiplicar",
    bg="#0F172A",
    fg="#38BDF8",
    font=("Arial", 12, "bold")
)
label.pack(pady=50)

entry1=tk.Entry(janela);entry1.pack(pady=5)
mult=tk.Label(janela,text="*");mult.pack(pady=5)
entry2=tk.Entry(janela);entry2.pack(pady=5)

janela.bind('<Return>', multiplicar)

janela.mainloop()

