import tkinter as tk

janela=tk.Tk()
janela.title("Botões")
janela.geometry("300x300")
janela.configure(bg='#a9a9a9')

btn=tk.Button(janela, text="Botão Fofo",bg='#000000',fg='#00FF00',
              activebackground="#FF69B4",activeforeground="#FFFFFF",
              font=("arial",14,"italic"))

btn2=tk.Button(janela, text="Botão Puto",bg='#000000',fg='#00FF00',
              activebackground="#FF69B4",activeforeground="#FFFFFF",
              font=("arial",14,"italic"))

btn.pack(pady=60,padx=100)
btn2.pack(pady=80, padx=101)

janela.mainloop()
