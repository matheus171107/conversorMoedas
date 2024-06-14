#janela 500x500
#título
#campos para selecionar as moedas de origem e de destino
#botão para converter
#lista de exibição com o nome das moedas

#importar a biblioteca que vai fazer a janela
import customtkinter

#criar e configurar janela
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme("green")
janela = customtkinter.CTk()
janela.geometry("500x600")
janela.title('Conversor de Moedas')
janela.iconbitmap("icon_conversor.ico")

#criar e configurar botões, textos e demais elementos
titulo = customtkinter.CTkLabel(janela, text="Conversor de Moedas", font=("Arial",25))
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de Origem", font=("",14))
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de Destino", font=("",14))
campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=["USD","EUR","BRL","BTC"], font=("",14))
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values=["USD","EUR","BRL","BTC"], font=("",14))           #Lista de Opções
lista_moedas = customtkinter.CTkScrollableFrame(janela)

moedas_disponiveis = ["USD: Dólar Americano", "EUR: Euro", "BRL: Real Brasileiro", "BTC: Biticoin"]

for moeda in moedas_disponiveis:
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=moeda)
    texto_moeda.pack()

def converter_moeda():
    print("Converter Moeda")

btn_converter = customtkinter.CTkButton(janela, text="Converter", command=converter_moeda, font=("",14))

#colocar elementos criados na tela
titulo.pack(padx=10,pady=10)
texto_moeda_origem.pack(padx=10,pady=5)
campo_moeda_origem.pack(padx=10,pady=5)
texto_moeda_destino.pack(padx=10,pady=5)
campo_moeda_destino.pack(padx=10,pady=5)
btn_converter.pack(padx=10,pady=15)
lista_moedas.pack(padx=10,pady=10)

#rodar janela
janela.mainloop()