import tkinter as tk
from tkinter import messagebox

def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - start + shift) % 26 + start)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def vigenere_encrypt(text, key):
    encrypted = ""
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            start = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - start + shift) % 26 + start)
            key_index += 1
        else:
            encrypted += char
    return encrypted

def vigenere_decrypt(text, key):
    decrypted = ""
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            start = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - start - shift) % 26 + start)
            key_index += 1
        else:
            decrypted += char
    return decrypted

def process_encrypt():
    text = entry_text.get()
    shift = int(entry_shift.get())
    key = entry_key.get()
    result = vigenere_encrypt(caesar_encrypt(text, shift), key)
    entry_result.delete(0, tk.END)
    entry_result.insert(0, result)

def process_decrypt():
    text = entry_result.get()
    shift = int(entry_shift.get())
    key = entry_key.get()
    result = caesar_decrypt(vigenere_decrypt(text, key), shift)
    entry_decryption.delete(0, tk.END)
    entry_decryption.insert(0, result)

def remove_spaces():
    text = entry_result.get().replace(" ", "")
    entry_result.delete(0, tk.END)
    entry_result.insert(0, text)

def split_into_five():
    text = entry_result.get()
    split_text = ' '.join([text[i:i+5] for i in range(0, len(text), 5)])
    entry_result.delete(0, tk.END)
    entry_result.insert(0, split_text)

def clear_fields():
    entry_text.delete(0, tk.END)
    entry_shift.delete(0, tk.END)
    entry_key.delete(0, tk.END)
    entry_result.delete(0, tk.END)
    entry_decryption.delete(0, tk.END)

# GUI menggunakan tkinter
window = tk.Tk()
window.title("Caesar + Vigenère Cipher")

# Layout dan Input
frame_top = tk.Frame(window, padx=10, pady=10)
frame_top.grid(row=0, column=0, columnspan=2)

tk.Label(frame_top, text="Masukkan Teks:").grid(row=0, column=0, sticky='e', padx=5)
entry_text = tk.Entry(frame_top, width=40)
entry_text.grid(row=0, column=1)

tk.Label(frame_top, text="Shift (Caesar):").grid(row=1, column=0, sticky='e', padx=5)
entry_shift = tk.Entry(frame_top, width=5)
entry_shift.grid(row=1, column=1, sticky='w')

tk.Label(frame_top, text="Kunci (Vigenère):").grid(row=2, column=0, sticky='e', padx=5)
entry_key = tk.Entry(frame_top, width=20)
entry_key.grid(row=2, column=1, sticky='w')

# Tombol Enkripsi, Dekripsi, Hapus Spasi, Pisah 5 Huruf (Sejajar)
frame_buttons = tk.Frame(window, padx=10, pady=10)
frame_buttons.grid(row=3, column=0, columnspan=2)

btn_encrypt = tk.Button(frame_buttons, text="Enkripsi", command=process_encrypt)
btn_encrypt.grid(row=0, column=0, padx=5, pady=5)

btn_decrypt = tk.Button(frame_buttons, text="Dekripsi", command=process_decrypt)
btn_decrypt.grid(row=0, column=1, padx=5, pady=5)

btn_remove_spaces = tk.Button(frame_buttons, text="Hapus Spasi", command=remove_spaces)
btn_remove_spaces.grid(row=0, column=2, padx=5, pady=5)

btn_split_five = tk.Button(frame_buttons, text="Pisah per 5 Huruf", command=split_into_five)
btn_split_five.grid(row=0, column=3, padx=5, pady=5)

# Hasil Enkripsi dan Dekripsi
tk.Label(window, text="Hasil Enkripsi:").grid(row=4, column=0, sticky='e', padx=10, pady=5)
entry_result = tk.Entry(window, width=40, bg="light green")
entry_result.grid(row=4, column=1, padx=10, pady=5)

tk.Label(window, text="Hasil Dekripsi:").grid(row=5, column=0, sticky='e', padx=10, pady=5)
entry_decryption = tk.Entry(window, width=40, bg="light yellow")
entry_decryption.grid(row=5, column=1, padx=10, pady=5)

# Tombol Bersihkan
btn_clear = tk.Button(window, text="Bersihkan", command=clear_fields)
btn_clear.grid(row=6, column=0, columnspan=2, pady=10)

# Menjalankan GUI
window.mainloop()
