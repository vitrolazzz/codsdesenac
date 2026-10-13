    import tkinter as tk

    def mostrar_tela1():
        janela1.pack(fill="both", expand=True)
        janela2.pack_forget()

    def mostrar_tela2():    
        janela1.pack_forget()
        janela2.pack(fill="both", expand=True)

    app = tk.Tk()
    app.title("App Resenha")
    app.geometry("400x400")

    janela1 = tk.Frame(app)
    tk.Button(janela1,text="clica pra trocar",command=mostrar_tela2,bg="blue").pack(pady=15)
    label=tk.Label(janela1,text="Janela legal",bg="black",fg='white',font=("arial",10, "bold"))
    janela1.configure(bg="#FFFFFF")

    label.pack(pady=30)

    janela2 = tk.Frame(app)
    tk.Button(janela2,text="clica pra trocar",command=mostrar_tela1,bg="pink").pack(pady=15)
    janela2.configure(bg="green")
    label=tk.Label(janela2,text="Janela feia",bg="blue",fg='grey',font=("arial",10, "bold"))

    label.pack(pady=30)

    janela1.pack(fill="both", expand=True)
    app.mainloop()  