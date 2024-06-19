#janela 500x500
#título
#campos para selecionar as moedas de origem e de destino
#botão para converter
#lista de exibição com o nome das moedas

#importar a biblioteca que vai fazer a janela
import customtkinter
from pegar_moedas import nomes_moedas, convesoes_disponiveis
from pegar_contacao import pegar_contacao_moeda

#criar e configurar janela
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme("green")
janela = customtkinter.CTk()
janela.geometry("500x600")
janela.title('Conversor de Moedas')
janela.iconbitmap("icon_conversor.ico")

dic_conversoes_disponiveis = convesoes_disponiveis()

def carregar_moedas_destino(moeda_selecionada):
    lista_moedas_destino = dic_conversoes_disponiveis[moeda_selecionada]
    campo_moeda_destino.configure(values=lista_moedas_destino)
    campo_moeda_destino.set(lista_moedas_destino[0])

#criar e configurar botões, textos e demais elementos
titulo = customtkinter.CTkLabel(janela, text="Conversor de Moedas", font=("Arial",25))
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de Origem", font=("",14))
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de Destino", font=("",14))
campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=list(dic_conversoes_disponiveis.keys()), command=carregar_moedas_destino, font=("",14))
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values=["Selecione uma moeda de origem"], font=("",14))       #Lista de Opções
lista_moedas = customtkinter.CTkScrollableFrame(janela)

moedas_disponiveis = nomes_moedas()

for codigo_moeda in moedas_disponiveis:
    nome_moeda = moedas_disponiveis[codigo_moeda]
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=f"{codigo_moeda}: {nome_moeda}")
    texto_moeda.pack()

def converter_moeda():
    moeda_origem = campo_moeda_origem.get()     #Valor selecionado no menu de opções
    moeda_destino = campo_moeda_destino.get()
    if moeda_origem and moeda_destino:
        cotacao = pegar_contacao_moeda(moeda_origem, moeda_destino)
        print(cotacao)
        texto_cotacao_moeda.configure(text=f'1 {moeda_origem} = {cotacao} {moeda_destino}')

btn_converter = customtkinter.CTkButton(janela, text="Converter", command=converter_moeda, font=("",14))
texto_cotacao_moeda = customtkinter.CTkLabel(janela, text="")

#colocar elementos criados na tela
titulo.pack(padx=10,pady=10)
texto_moeda_origem.pack(padx=10,pady=5)
campo_moeda_origem.pack(padx=10,pady=5)
texto_moeda_destino.pack(padx=10,pady=5)
campo_moeda_destino.pack(padx=10,pady=5)
btn_converter.pack(padx=10,pady=15)
texto_cotacao_moeda.pack()
lista_moedas.pack(padx=10,pady=10)

#rodar janela
janela.mainloop()