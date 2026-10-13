import tkinter as tk

janela = tk.Tk()
janela.title("Eleições 2026 Brasil")
janela.geometry("400x300")

label = tk.Label(janela, text="Tem de bosta de tem de merda. Escolha!")
label.pack(pady=20)

def aoclicar1():
    label.config(text="Parabéns, você escolheu merda")

def aoclicar2():
    label.config(text="Parabéns, você escolheu bosta")

botao1=tk.Button(janela,text="Bosta", command=aoclicar1)
botao1.pack()

botao2=tk.Button(janela,text="Merda", command=aoclicar2)
botao2.pack()

janela.mainloop()