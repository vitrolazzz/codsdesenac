import tkinter as tk
from PIL import ImageTk,Image

app=tk.Tk()
app.geometry("358x250")

img_pil = Image.open(r"C:\Users\VITORLUCASSALVIANOFE\Documents\Execs Vitor\telas imag\makeiko.jpg")
img_pil=img_pil.resize((100,100))

icone_tk=ImageTk.PhotoImage(img_pil)

btn=tk.Button(app,text="vire um makeiko",
image=icone_tk,
compound="top")

btn.imagem=icone_tk
btn.pack(pady=40)

app.mainloop()
