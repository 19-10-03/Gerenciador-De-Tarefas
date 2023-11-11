import tkinter as tk
import db


# Funções CRUD
def calcular_preco_final(preco):
    return preco * 1.1


def cadastrar_produto():
    codigo = codigo_entry.get()
    nome = nome_entry.get()
    preco = float(preco_entry.get())
    preco_final = calcular_preco_final(preco)
    conn = db.get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO Agenda (codigo_produto, nome_produto, preco, preco_final) VALUES (%s, %s, %s, %s)",
        (codigo, nome, preco, preco_final),
    )
    conn.commit()
    cur.close()


def ler_dados():
    conn = db.get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Agenda")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()


def atualizar_produto():
    codigo = codigo_entry.get()
    nome = nome_entry.get()
    preco = float(preco_entry.get())
    preco_final = calcular_preco_final(preco)
    conn = db.get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE Agenda SET nome_produto = %s, preco = %s, preco_final = %s WHERE codigo_produto = %s",
        (nome, preco, preco_final, codigo),
    )
    conn.commit()
    cur.close()


def excluir_produto():
    codigo = codigo_entry.get()
    conn = db.get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Agenda WHERE codigo_produto = %s", (codigo,))
    conn.commit()
    cur.close()


# Interface gráfica com Tkinter
root = tk.Tk()
root.title("Sistema de Cadastro de Produtos")

codigo_label = tk.Label(root, text="Código do Produto")
codigo_label.pack()
codigo_entry = tk.Entry(root)
codigo_entry.pack()

nome_label = tk.Label(root, text="Nome do Produto")
nome_label.pack()
nome_entry = tk.Entry(root)
nome_entry.pack()

preco_label = tk.Label(root, text="Preço")
preco_label.pack()
preco_entry = tk.Entry(root)
preco_entry.pack()

cadastrar_button = tk.Button(root, text="Cadastrar", command=cadastrar_produto)
cadastrar_button.pack()

ler_button = tk.Button(root, text="Ler Dados", command=ler_dados)
ler_button.pack()

atualizar_button = tk.Button(root, text="Atualizar", command=atualizar_produto)
atualizar_button.pack()

excluir_button = tk.Button(root, text="Excluir", command=excluir_produto)
excluir_button.pack()

calculo_label = tk.Label(root, text="Preço com 10% de acréscimo: ")
calculo_label.pack()


def mostrar_preco_final():
    try:
        preco = float(preco_entry.get())
        preco_final = calcular_preco_final(preco)
        calculo_label.config(text=f"Preço com 10% de acréscimo: R${preco_final:.2f}")
    except ValueError:
        calculo_label.config(text="Valor inválido")


mostrar_preco_button = tk.Button(root, text="Calcular", command=mostrar_preco_final)
mostrar_preco_button.pack()

root.mainloop()
