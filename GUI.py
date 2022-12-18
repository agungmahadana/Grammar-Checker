from tkinter import *
from FP import *

window = Tk()
window.configure(background="white")
window.geometry("500x400")
window.resizable(True, True)
window.title("Cek Kalimat Baku")

input_frame = Frame(window)
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

kalimat = Label(input_frame, text="Masukkan kalimat")
kalimat.pack(padx=10, pady=10, fill="x", expand=True)

kalimat = StringVar()
input_kalimat = Entry(input_frame, textvariable=kalimat)
input_kalimat.pack(padx=10, pady=10, fill="x", expand=True)

def get_value():
    e_text = input_kalimat.get()
    notif = ""
    if cek_kalimat(e_text) == 1:
        notif = "Kalimat merupakan kalimat baku"
    else :
        notif = "Kalimat bukan kalimat baku"
    Label(window, text=notif, font= ('Century 15 bold')).pack(pady=20)

kalimat_cek = Button(input_frame, text="Cek!", command=get_value)
kalimat_cek.pack(padx=10, fill="x", expand=True)

print(input_kalimat.get())
window.mainloop()
