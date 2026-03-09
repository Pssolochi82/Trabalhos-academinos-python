import tkinter as tk
import os
from tkinter import ttk

# -----------------------------
# Funções auxiliares
# -----------------------------

def limpar_frame():
    for widget in frame_conteudo.winfo_children():
        widget.destroy()

# -----------------------------
# Olá Palmira bem-vinda ao curso de Python
# -----------------------------

def exemplo_hello():
    limpar_frame()
    label = tk.Label(frame_conteudo, text="Olá Palmira bem-vinda ao curso de Python!", font=("Arial", 14))
    label.pack(pady=10)

# -----------------------------
# Label simples
# -----------------------------

def exemplo_label():
    limpar_frame()
    label = tk.Label(frame_conteudo, text="Isto é uma Label")
    label.pack(pady=10)

# -----------------------------
# Label com dimensões alteradas
# -----------------------------

def exemplo_label_dimensoes():
    limpar_frame()
    label = tk.Label(
        frame_conteudo,
        text="Label com tamanho fixo",
        width=30,
        height=5,
        bg="lightgray"
    )
    label.pack(pady=10)

# -----------------------------
# Label com imagem
# -----------------------------

def exemplo_label_imagem():
    print("PASTA ATUAL:", os.getcwd())
    print("FICHEIROS AQUI:", os.listdir())

    limpar_frame()
    try:
        imagem = tk.PhotoImage(file="imagem.png")
        label = tk.Label(frame_conteudo, image=imagem)
        label.image = imagem  # manter referência
        label.pack(pady=10)
    except Exception as e:
        label = tk.Label(frame_conteudo, text="Imagem não encontrada (imagem.png)")
        label.pack(pady=10)

# -----------------------------
# Button
# -----------------------------

def exemplo_button():
    limpar_frame()

    def clicar():
        resultado.config(text="Botão clicado!")

    botao = tk.Button(frame_conteudo, text="Clicar", command=clicar)
    botao.pack(pady=10)

    resultado = tk.Label(frame_conteudo, text="")
    resultado.pack(pady=10)

# -----------------------------
# Checkbutton
# -----------------------------

def exemplo_checkbutton():
    limpar_frame()

    def estado():
        resultado.config(text=f"Estado: {var.get()}")

    var = tk.IntVar()

    check = tk.Checkbutton(
        frame_conteudo,
        text="Aceito os termos",
        variable=var,
        command=estado
    )
    check.pack(pady=10)

    resultado = tk.Label(frame_conteudo, text="Estado: 0")
    resultado.pack(pady=10)

# -----------------------------
# Checkbutton Toggle
# -----------------------------

def exemplo_toggle():
    limpar_frame()

    def toggle():
        if var.get() == 1:
            resultado.config(text="Ligado")
        else:
            resultado.config(text="Desligado")

    var = tk.IntVar()

    check = tk.Checkbutton(
        frame_conteudo,
        text="Ativar opção",
        variable=var,
        command=toggle
    )
    check.pack(pady=10)

    resultado = tk.Label(frame_conteudo, text="Desligado")
    resultado.pack(pady=10)

# -----------------------------
# Combobox
# -----------------------------

def exemplo_combobox():
    limpar_frame()

    def mostrar():
        resultado.config(text=f"Selecionado: {combo.get()}")

    opcoes = ["Opção 1", "Opção 2", "Opção 3"]

    combo = ttk.Combobox(frame_conteudo, values=opcoes)
    combo.current(0)
    combo.pack(pady=10)

    botao = tk.Button(frame_conteudo, text="Mostrar", command=mostrar)
    botao.pack(pady=10)

    resultado = tk.Label(frame_conteudo, text="")
    resultado.pack(pady=10)

# -----------------------------
# Radiobutton
# -----------------------------

def exemplo_radiobutton():
    limpar_frame()

    def mostrar():
        resultado.config(text=f"Selecionado: {var.get()}")

    var = tk.StringVar(value="A")

    rb1 = tk.Radiobutton(frame_conteudo, text="Opção A", variable=var, value="A")
    rb2 = tk.Radiobutton(frame_conteudo, text="Opção B", variable=var, value="B")
    rb3 = tk.Radiobutton(frame_conteudo, text="Opção C", variable=var, value="C")

    rb1.pack()
    rb2.pack()
    rb3.pack()

    botao = tk.Button(frame_conteudo, text="Mostrar", command=mostrar)
    botao.pack(pady=10)

    resultado = tk.Label(frame_conteudo, text="")
    resultado.pack(pady=10)

# -----------------------------
# Entry
# -----------------------------

def exemplo_entry():
    limpar_frame()

    def mostrar_texto():
        resultado.config(text=f"Texto digitado: {entrada.get()}")

    entrada = tk.Entry(frame_conteudo)
    entrada.pack(pady=10)

    botao = tk.Button(frame_conteudo, text="Mostrar", command=mostrar_texto)
    botao.pack(pady=10)

    resultado = tk.Label(frame_conteudo, text="")
    resultado.pack(pady=10)

# -----------------------------
# Janela principal
# -----------------------------

root = tk.Tk()
root.title("Demonstração de Widgets Tkinter")
root.geometry("700x400")

frame_menu = tk.Frame(root, bg="#917d7d")
frame_menu.pack(side="left", fill="y")

frame_conteudo = tk.Frame(root)
frame_conteudo.pack(side="right", expand=True, fill="both")

botoes = [
    ("Hello", exemplo_hello),
    ("Label", exemplo_label),
    ("Label Dimensões", exemplo_label_dimensoes),
    ("Label Imagem", exemplo_label_imagem),
    ("Button", exemplo_button),
    ("Checkbutton", exemplo_checkbutton),
    ("Toggle", exemplo_toggle),
    ("Combobox", exemplo_combobox),
    ("Radiobutton", exemplo_radiobutton),
    ("Entry", exemplo_entry),
]

for texto, comando in botoes:
    btn = tk.Button(frame_menu, text=texto, width=18, command=comando)
    btn.pack(pady=4, padx=6)

root.mainloop()
