# Convertidor-a-Runas-Antiguas
Convertidor de Español a Runas Antiguas
Este programa, desarrollado con Python y Tkinter, te permite traducir fácilmente cualquier texto en español a las antiguas runas vikingas, las cuales fueron utilizadas por los nórdicos durante la Era Vikinga. Además, hemos incorporado una función para copiar la traducción directamente al portapapeles con solo un clic. ¡Perfecto para aquellos interesados en la cultura y la historia de los vikingos!

![WhatsApp Image 2024-08-05 at 12 22 55](https://github.com/user-attachments/assets/f5c20fcf-b21b-4a73-bb1f-86d9428812ba)

Características del Programa:
Interfaz Amigable: Fácil de usar y entender.
Conversión Precisa: Traduce el texto español a runas vikingas auténticas.
Copiar al Portapapeles: Función para copiar la traducción rápidamente.
Estilo 3D: Botones con un atractivo diseño en 3D.
Breve Historia de los Vikingos y las Runas:
Los vikingos, conocidos por sus audaces incursiones y exploraciones desde finales del siglo VIII hasta el siglo XI, hablaban una lengua germánica llamada nórdico antiguo. Utilizaban un sistema de escritura rúnico, conocido como el futhark, para tallar inscripciones en piedra, madera y metal. Estas runas no solo eran herramientas de comunicación, sino que también tenían un significado mágico y ritual para los vikingos.

Las runas vikingas son parte integral de la rica tradición literaria y poética de los nórdicos, conservada principalmente en las sagas islandesas y las eddas. Hoy en día, estas inscripciones y textos siguen siendo una fuente de fascinación e inspiración, mostrando la duradera influencia de los vikingos en la cultura y la historia.
Aquí tienes una explicación paso a paso del programa que convierte texto en español a runas vikingas usando Tkinter:

### Paso 1: Importar Módulos Necesarios

Primero, importamos los módulos `tkinter` y `messagebox` necesarios para crear la interfaz gráfica y mostrar mensajes de advertencia o información.

```python
import tkinter as tk
from tkinter import messagebox
```

### Paso 2: Definir el Mapeo de Caracteres

Creamos un diccionario llamado `rune_mapping` que contiene el mapeo de cada letra del alfabeto español a su equivalente en runas vikingas. También incluimos un espacio para mantener los espacios en blanco en el texto traducido.

```python
rune_mapping = {
    'a': 'ᚨ', 'b': 'ᛒ', 'c': 'ᚲ', 'd': 'ᛞ', 'e': 'ᛖ',
    'f': 'ᚠ', 'g': 'ᚷ', 'h': 'ᚺ', 'i': 'ᛁ', 'j': 'ᛃ',
    'k': 'ᚲ', 'l': 'ᛚ', 'm': 'ᛗ', 'n': 'ᚾ', 'o': 'ᛟ',
    'p': 'ᛈ', 'q': 'ᛩ', 'r': 'ᚱ', 's': 'ᛋ', 't': 'ᛏ',
    'u': 'ᚢ', 'v': 'ᚡ', 'w': 'ᚹ', 'x': 'ᛪ', 'y': 'ᚣ',
    'z': 'ᛉ', ' ': ' '
}
```

### Paso 3: Definir Funciones del Programa

#### Función `translate_to_runes`

Esta función toma un texto en español como entrada y lo convierte en runas vikingas utilizando el diccionario `rune_mapping`. La función convierte el texto a minúsculas para asegurar que todas las letras coincidan con las claves del diccionario.

```python
def translate_to_runes(text):
    return ''.join(rune_mapping.get(char, char) for char in text.lower())
```

#### Función `convert_text`

Esta función obtiene el texto del campo de entrada, verifica si está vacío, y luego lo traduce a runas. Si el texto está vacío, muestra una advertencia. La traducción se muestra en la etiqueta de salida.

```python
def convert_text():
    input_text = entry.get()
    if not input_text:
        messagebox.showwarning("Advertencia", "Por favor, ingrese un texto para convertir.")
        return
    translated_text = translate_to_runes(input_text)
    output_label.config(text=translated_text)
```

#### Función `copy_to_clipboard`

Esta función copia el texto traducido al portapapeles del sistema. Si no hay texto traducido, muestra una advertencia.

```python
def copy_to_clipboard():
    translated_text = output_label.cget("text")
    if translated_text:
        root.clipboard_clear()
        root.clipboard_append(translated_text)
        messagebox.showinfo("Información", "Texto copiado al portapapeles.")
    else:
        messagebox.showwarning("Advertencia", "No hay texto traducido para copiar.")
```

#### Función `exit_program`

Esta función cierra la aplicación.

```python
def exit_program():
    root.destroy()
```

### Paso 4: Configurar la Ventana Principal

Creamos la ventana principal del programa y configuramos su título, tamaño y color de fondo.

```python
root = tk.Tk()
root.title("Convertidor de Español a Runas Antiguas")
root.geometry("600x400")
root.configure(bg='#F0F0F0')
```

### Paso 5: Estilo de los Botones

Definimos un diccionario `button_style` para aplicar un estilo 3D a los botones, incluyendo colores, fuentes y efectos.

```python
button_style = {
    "relief": "raised",
    "bd": 5,
    "bg": "#007BFF",
    "fg": "#FFFFFF",
    "activebackground": "#0056b3",
    "activeforeground": "#FFFFFF",
    "font": ("Helvetica", 12, "bold")
}
```

### Paso 6: Crear Elementos de la Interfaz

#### Etiqueta de Entrada

Creamos una etiqueta que indica al usuario que ingrese el texto en español.

```python
entry_label = tk.Label(root, text="Ingrese el texto en español:", font=("Helvetica", 14), bg='#F0F0F0')
entry_label.pack(pady=10)
```

#### Campo de Entrada

Creamos un campo de entrada para que el usuario ingrese el texto que desea convertir.

```python
entry = tk.Entry(root, font=("Helvetica", 14), width=40)
entry.pack(pady=10)
```

#### Botón de Conversión

Creamos un botón que, al ser presionado, llamará a la función `convert_text`.

```python
convert_button = tk.Button(root, text="Convertir", command=convert_text, **button_style)
convert_button.pack(pady=10)
```

#### Etiqueta de Salida

Creamos una etiqueta para mostrar el texto traducido.

```python
output_label = tk.Label(root, text="", font=("Helvetica", 14), bg='#F0F0F0')
output_label.pack(pady=10)
```

#### Botón para Copiar al Portapapeles

Creamos un botón que, al ser presionado, llamará a la función `copy_to_clipboard`.

```python
copy_button = tk.Button(root, text="Copiar al portapapeles", command=copy_to_clipboard, **button_style)
copy_button.pack(pady=10)
```

#### Botón de Salida

Creamos un botón que, al ser presionado, llamará a la función `exit_program` para cerrar la aplicación.

```python
exit_button = tk.Button(root, text="Salir", command=exit_program, **button_style)
exit_button.pack(pady=10)
```

### Paso 7: Ejecutar la Aplicación

Finalmente, ejecutamos el bucle principal de la aplicación para que se mantenga abierta y responda a las acciones del usuario.

```python
root.mainloop()
```

Con estos pasos, el programa estará completo y funcional, permitiendo a los usuarios convertir texto en español a runas vikingas, copiar la traducción al portapapeles y salir de la aplicación.
