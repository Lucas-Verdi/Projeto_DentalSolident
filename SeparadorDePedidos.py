#Separador de Pedidos
#Autor: Lucas Arnaut Verdi
#Versão: 2.0
#Data: 10/04/2023

import os
import tkinter

import clipboard as pc
from tkinter import *
import os
from tkinter import ttk

def funcao_programa():
    while True:
        string = entrada_pedidos.get()
        global separada
        separada = ""

        for i in range(0, len(string), 7):
            substr = string[i:i + 7]
            separada += substr + ";"

            if (i + 7) % 35 == 0:
                separada += "\n"

        pc.copy(separada)

        saida_pedidos.delete('1.0', END)
        saida_pedidos.insert(END, separada)

        break

def nova_formatacao():
    entrada_pedidos.delete(0, END)
    saida_pedidos.delete('1.0', END)

def abrir_janela():
    janela2 = Tk()
    janela2.title('Formatação de pedidos')
    label_nome = Label(janela2, text = "Insira aqui os pedidos:")
    label_nome.grid(column=0, row=0, padx=5, pady=5)
    botao_voltar = Button(janela2, text = 'Voltar', command = janela2.destroy)
    botao_voltar.grid(column=0, row=1, padx=10, pady=10)
    global entrada_pedidos
    entrada_pedidos = Entry(janela2, width=10)
    entrada_pedidos.grid(column=1, row=0, ipadx=100, padx=50)
    botao_formatar = Button(janela2, text='Formatar')
    botao_formatar.bind("<Button>", lambda e: funcao_programa())
    botao_formatar.grid(column=0, row=2, padx=30, pady=10)
    label_formatados = Label(janela2, text='Os pedidos formatados são copiados automaticamente para a área de transferência !')
    label_formatados.grid(column=0, row=4, padx=10, pady=10)
    global saida_pedidos
    saida_pedidos = Text(janela2, height=10)
    saida_pedidos.pack
    botao_novaf = Button(janela2, text='Nova Formatação')
    botao_novaf.grid(column=0, row=3, padx=30, pady=10)
    botao_novaf.bind("<Button>", lambda e: nova_formatacao())


janela = Tk()
janela.title('Formatação de pedidos')
texto = Label(janela, text='Clique para inserir os pedidos')
texto.grid(column=0, row=0, padx=10, pady=10)
botao = Button(janela, text="Inserir")
botao.bind("<Button>",  lambda e: abrir_janela())
botao.grid(column=0, row=1, padx=10, pady=10)

janela.mainloop()


