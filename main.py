#F3NIX
import tkinter as tk
from tkinter import messagebox

# Mapeo básico de caracteres españoles a runas antiguas
rune_mapping = {
    'a': 'ᚨ', 'b': 'ᛒ', 'c': 'ᚲ', 'd': 'ᛞ', 'e': 'ᛖ',
    'f': 'ᚠ', 'g': 'ᚷ', 'h': 'ᚺ', 'i': 'ᛁ', 'j': 'ᛃ',
    'k': 'ᚲ', 'l': 'ᛚ', 'm': 'ᛗ', 'n': 'ᚾ', 'o': 'ᛟ',
    'p': 'ᛈ', 'q': 'ᛩ', 'r': 'ᚱ', 's': 'ᛋ', 't': 'ᛏ',
    'u': 'ᚢ', 'v': 'ᚡ', 'w': 'ᚹ', 'x': 'ᛪ', 'y': 'ᚣ',
    'z': 'ᛉ', ' ': ' '
}

def translate_to_runes(text):
    return ''.join(rune_mapping.get(char, char) for char in text.lower())

def convert_text():
    input_text = entry.get()
    if not input_text:
        messagebox.showwarning("Advertencia", "Por favor, ingrese un texto para convertir.")
        return
    translated_text = translate_to_runes(input_text)
    output_label.config(text=translated_text)

def copy_to_clipboard():
    translated_text = output_label.cget("text")
    if translated_text:
        root.clipboard_clear()
        root.clipboard_append(translated_text)
        messagebox.showinfo("Información", "Texto copiado al portapapeles.")
    else:
        messagebox.showwarning("Advertencia", "No hay texto traducido para copiar.")

def exit_program():
    root.destroy()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Convertidor de Español a Runas Antiguas")
root.geometry("600x400")
root.configure(bg='#F0F0F0')

# Estilo 3D para botones
button_style = {
    "relief": "raised",
    "bd": 5,
    "bg": "#007BFF",
    "fg": "#FFFFFF",
    "activebackground": "#0056b3",
    "activeforeground": "#FFFFFF",
    "font": ("Helvetica", 12, "bold")
}

# Campo de entrada de texto
entry_label = tk.Label(root, text="Ingrese el texto en español:", font=("Helvetica", 14), bg='#F0F0F0')
entry_label.pack(pady=10)

entry = tk.Entry(root, font=("Helvetica", 14), width=40)
entry.pack(pady=10)

# Botón de conversión
convert_button = tk.Button(root, text="Convertir", command=convert_text, **button_style)
convert_button.pack(pady=10)

# Etiqueta de salida de texto convertido
output_label = tk.Label(root, text="", font=("Helvetica", 14), bg='#F0F0F0')
output_label.pack(pady=10)

# Botón para copiar al portapapeles
copy_button = tk.Button(root, text="Copiar al portapapeles", command=copy_to_clipboard, **button_style)
copy_button.pack(pady=10)

# Botón de salida
exit_button = tk.Button(root, text="Salir", command=exit_program, **button_style)
exit_button.pack(pady=10)

# Ejecución de la aplicación
root.mainloop()
