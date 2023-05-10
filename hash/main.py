import hashlib
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

def dosya_sec():
    dosyayolu = filedialog.askopenfilename()
    dosyayolu_girisi.delete(0, tk.END)
    dosyayolu_girisi.insert(0, dosyayolu)


def hash_hesapla(algorithm):
    dosyayolu = dosyayolu_girisi.get()
    if not dosyayolu:
        dogrulama_sonucu.config(text="Lütfen bir dosya seçin.")
        return

    with open(dosyayolu, 'rb') as f:
        hasher = hashlib.new(algorithm)
        buf = f.read(65536)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(65536)
        hash_degeri = hasher.hexdigest()
        hash_etiketi.config(text=hash_degeri)


def hash_dogrulama(algorithm):
    dosyayolu = dosyayolu_girisi.get()
    beklenen_hash = beklenen_hash_girisi.get()
    if not dosyayolu:
        dogrulama_sonucu.config(text="Lütfen bir dosya seçin.")
        return
    if not beklenen_hash:
        dogrulama_sonucu.config(text="Lütfen bir hash değeri girin.")
        return

    with open(dosyayolu, 'rb') as f:
        hasher = hashlib.new(algorithm)
        buf = f.read(65536)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(65536)
        hash_degeri = hasher.hexdigest()

        if hash_degeri == beklenen_hash:
            dogrulama_sonucu.config(text="Hash değeri eşleşiyor!")
            dogrulama_sonucu.configure(background="lightgreen")
        else:
            dogrulama_sonucu.config(text="Hash değeri eşleşmiyor.")
            dogrulama_sonucu.configure(background="maroon")


pencere = tk.Tk()
pencere.title("Hash Değeri Hesaplama ve Doğrulama")


pencere.resizable(width=0, height=0)
pencere.geometry("400x230")


etiket=tk.Label(pencere,text="Hash değerini hesaplamak veya doğrulamak istediğiniz dosyayı seçiniz.")
etiket.pack()


dosyasecmebutonu = tk.Button(pencere, text="Dosya Seç", command=dosya_sec)
dosyasecmebutonu.pack()


dosyayolu_girisi = tk.Entry(pencere, width=50)
dosyayolu_girisi.pack()


hash_etiketi = tk.Label(pencere, text="")
hash_etiketi.pack()


hash_algoritmasi_combobox = ttk.Combobox(pencere, values=["md5", "sha1", "sha256"], state="readonly")
hash_algoritmasi_combobox.pack()


hesaplama_butonu = tk.Button(pencere, text="Hash Değeri Hesapla", command=lambda: hash_hesapla(hash_algoritmasi_combobox.get()))
hesaplama_butonu.pack()


hash_etiketi = tk.Label(pencere, text="")
hash_etiketi.pack()


beklenen_hash_girisi = tk.Entry(pencere, width=50)
beklenen_hash_girisi.pack()


dogrulama_butonu = tk.Button(pencere, text="Hash Değerini Doğrula", command=lambda: hash_dogrulama(hash_algoritmasi_combobox.get()))
dogrulama_butonu.pack()


dogrulama_sonucu = tk.Label(pencere, text="")
dogrulama_sonucu.pack()


pencere.mainloop()