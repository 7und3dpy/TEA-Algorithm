import tkinter as tk
from tkinter import ttk
from src.TEAdef import TEA


def create_widgets():
    ttk.Label(root, text="TEA Key:").grid(row=0, column=0, sticky="e")
    ttk.Entry(root, textvariable=tea_key_var, state="readonly").grid(row=0, column=1, padx=5, pady=5)
    ttk.Button(root, text="Generate Key", command=generate_key).grid(row=0, column=2, padx=5, pady=5)

    ttk.Label(root, text="Plain Text:").grid(row=1, column=0, sticky="e")
    ttk.Entry(root, textvariable=plain_text_var).grid(row=1, column=1, padx=5, pady=5)

    ttk.Button(root, text="Encrypt", command=encrypt).grid(row=2, column=1, padx=5, pady=5)
    ttk.Button(root, text="Decrypt", command=decrypt).grid(row=3, column=1, padx=5, pady=5)

    ttk.Label(root, text="Encrypted Text:").grid(row=4, column=0, sticky="e")
    ttk.Entry(root, textvariable=encrypted_text_var, state="readonly").grid(row=4, column=1, padx=5, pady=5)

def generate_key():
    tea_key = TEA.generateTeaKey()
    tea_key_var.set(tea_key)

def encrypt():
    tea_key = tea_key_var.get()
    plain_text = plain_text_var.get()
    encrypted_text = TEA.encrypt(plain_text, tea_key)
    encrypted_text_var.set(encrypted_text)

def decrypt():
    tea_key = tea_key_var.get()
    encrypted_text = encrypted_text_var.get()
    decrypted_text = TEA.decrypt(encrypted_text, tea_key)
    plain_text_var.set(decrypted_text)

root = tk.Tk()
root.title("TEA Cryptography")

tea_key_var = tk.StringVar()
plain_text_var = tk.StringVar()
encrypted_text_var = tk.StringVar()
create_widgets()

tea_key = tea_key_var.get()
plain_text = plain_text_var.get()
encrypted_text = TEA.encrypt(plain_text, tea_key)

root.mainloop()