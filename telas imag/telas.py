import tkinter as tk
from PIL import ImageTk,Image

app=tk.Tk()
app.title("makeiko")
app.geometry("350x350")

img_pil=Image.open("C:/Users/VITORLUCASSALVIANOFE/Documents/Execs Vitor/telas imag/makeiko.jpg")
img_pil=img_pil.resize((150,150))

imagem_tk=ImageTk.PhotoImage(img_pil)

lbl_img=tk.label(app, image=imagem_tk)
lbl_img.image = imagem_tk
lbl.img.pack(pody=20)

app.mainloop