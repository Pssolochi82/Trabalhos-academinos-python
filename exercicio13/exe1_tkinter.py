# Importa a biblioteca Tkinter para criar interfaces gráficas
import tkinter as tk

# Cria a janela principal
janela = tk.Tk()

# Define o título da janela
janela.title("Tkinter")

# Define o tamanho da janela
janela.geometry("300x450")


# ------------------------------
# Texto no topo da janela
# ------------------------------
label = tk.Label(janela, text="Hello, Tkinter!")
label.pack(pady=5)


# ------------------------------
# Botão Click Me
# ------------------------------
botao_click = tk.Button(janela, text="Click Me")
botao_click.pack(pady=5)


# ------------------------------
# Caixa de texto
# ------------------------------
entrada = tk.Entry(janela)
entrada.pack(pady=5)


# ------------------------------
# Botão Submit
# ------------------------------
botao_submit = tk.Button(janela, text="Submit")
botao_submit.pack(pady=5)


# ------------------------------
# CheckBox
# ------------------------------
check_var = tk.IntVar()

checkbox = tk.Checkbutton(janela, text="Check Me", variable=check_var)
checkbox.pack(pady=5)


# ------------------------------
# Radio Buttons
# ------------------------------
radio_var = tk.IntVar()

radio1 = tk.Radiobutton(janela, text="Option 1", variable=radio_var, value=1)
radio1.pack()

radio2 = tk.Radiobutton(janela, text="Option 2", variable=radio_var, value=2)
radio2.pack()


# ------------------------------
# Lista de opções
# ------------------------------
lista = tk.Listbox(janela, height=5)

lista.insert(1, "Option 1")
lista.insert(2, "Option 2")
lista.insert(3, "Option 3")

lista.pack(pady=10)


# ------------------------------
# Botão Select
# ------------------------------
botao_select = tk.Button(janela, text="Select")
botao_select.pack(pady=5)


# Mantém a janela aberta
janela.mainloop()