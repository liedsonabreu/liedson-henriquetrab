from tkinter import *
from dao.ProdutoDao import ProdutoDao
from config.Config import Config
from config.Database import Database

config = Config()
database = Database(config.config)
dao = ProdutoDao(database.conn)

main = Tk()
main.title("Alterar")
main.geometry("1500x1000")

row = Frame(main)
row.pack(side=TOP, fill=X, padx=5, pady=5)

lbl = Label(row, text="ID:", anchor='w')
lbl.pack(side=LEFT)

txt0 = Entry(row)
txt0.pack(side=LEFT, expand=YES, fill=X, padx=5)

lbl = Label(row, text="Nome: ", anchor='w')
lbl.pack(side=LEFT)

txt = Entry(row)
txt.pack(side=LEFT, expand=YES, fill=X, padx=5)

lbl = Label(row, text="Preço: ", anchor='w')
lbl.pack(side=LEFT)

txt2 = Entry(row)
txt2.pack(side=LEFT, expand=YES, fill=X, padx=5)

lbl = Label(row, text="Quantidade:", anchor='w')
lbl.pack(side=LEFT)

txt3 = Entry(row)
txt3.pack(side=LEFT, expand=YES, fill=X, padx=5)

def alterarProduto():

    id = txt0.get()
    nome = txt.get()
    preco = txt2.get()
    quantidade = txt3.get()
    dao.alterarProduto1(id, nome, preco, quantidade)

btn = Button(main, text="Alterar", command=alterarProduto)
btn.pack(side=LEFT, padx=5, pady=5)

btn = Button(main, text="Fechar", command=main.destroy)
btn.pack(side=RIGHT, padx=5, pady=5)

main.mainloop()