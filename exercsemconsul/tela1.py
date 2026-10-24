import tkinter as tk
from pathlib import Path

def abrir_link():
    with open(arquivopasta,"r",encoding="utf-8") as arquivo:
        conteudo=arquivo.read()
        print(conteudo)


arquivopasta=r"C:\Users\VITORLUCASSALVIANOFE\Documents\Execs Vitor\exercsemconsul\arquivo.txt"

janela=tk.Tk()

janela.title("Atividade sem consulta")  
janela.geometry("500x300")
janela.configure(background="black")
lbl=tk.Label(janela,text="Fala mundão",background="black",fg= "white", font=("times",20)).pack(pady=30)
button = tk.Button(janela,text="Clica bb",
                   bg="green",
                   fg="white",
                   font=("times",18),
                   command=abrir_link).pack(pady=60)


janela.mainloop()