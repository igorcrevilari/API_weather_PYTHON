import requests
from tkinter import *


def pegar_dados():
    API_KEY = "3f8369627fa895e7b28dd84fda5e12dd"  # Acesso da API do site 'OPEN WEATHER'
    cidade = x.get()  # pega o Entry (input) da interface TK
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()
    descricao = requisicao_dic['weather'][0]['description']

    temperatura = requisicao_dic['main']['temp'] - 273.15
    temperatura_minima = requisicao_dic['main']['temp_min'] - 273.15
    temperatura_maxima = requisicao_dic['main']['temp_max'] - 273.15
    umidade = requisicao_dic['main']['humidity']
    texto_resposta['text'] = f'''
        {descricao}\n 
        atual: {temperatura:.1f}º\n 
        max: {temperatura_maxima:.1f}º\n 
        min: {temperatura_minima:.1f}º\n 
        umidade: {umidade}%'''


janela = Tk()

janela.title("Análise Climática")
texto_tk = Label(janela, text="Digite a cidade que você quer analisar...")
texto_tk.grid(column=0, row=0, padx=10, pady=10)

x = Entry(janela)
x.grid(column=0, row=1, padx=10, pady=10)

botao = Button(janela, text="Buscar clima", command=pegar_dados)
botao.grid(column=1, row=1, padx=10, pady=10)

texto_resposta = Label(janela, text="")
texto_resposta.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()
