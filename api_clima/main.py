# aquele link da API = endpoint
# endpoint é o link para os metodo get e post[
# exemplo: https://open-meteo.com/v1/forecast

# sempre que eu uso API em python, devo chamar a biblioteca de requisições
# pip install requests

# sempre que queremos mostrar graficos, podemos usar a biblioteca matplotlib
# matplotlib é uma biblioteca para plotar graficos
# pip install matplotlib

import requests
import matplotlib.pyplot as plt #apelido plt para facilitar

#criar uma função para buscar_clima
def buscar_clima(latitude, longitude): #def criar uma função, que é um bloco de código reutilizável
    # dev informar o endpoint da API
    endpoint_clima = "https://api.open-meteo.com/v1/forecast"
    #informar os parametros pora o sistema da API em formato de dicionario
    #dicionario trabalha com chave: valor
    #chave - buscar_clima e #valor - temperatura
    parametros = { #dicionario de parametros chasve e : valor
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m",
        "timezone": "America/Sao_Paulo" #para ajustar o fuso horario para olugar que você quer e auto é automatico
    }
    
    #fazer a requisição para a API usando o método get
    resposta = requests.get(endpoint_clima, params=parametros)
    #sempre que queremos obter a resposta usamos o comando
    # requests.get para pegar os valores e colocamos os atribuitos request.get(variavel_do_endpoist, parms=dicionario_com_parametros)
    
    # para o sistema usar metodo post - para mostrar as informações
    dados = resposta.json() #transformar a resposta em json (linguagem que a API entende)
    return dados #retornar os dados para quem chamou a função

#o usuario irá informar a latitude e longitude
latitude = float(input("Informe a latitude: ")) #float para numeros com casas decimais
longitude = float(input("Informe a longitude: "))#float para numeros com casas decimais

#vamos começar a exibir a informações para o usuario do clima
dados = buscar_clima(latitude, longitude) #chamando a função buscar_clima e passando os parametros latitude e longitude

horas = dados['hourly']['time'] #chamo a base de dados, informo o parametro e qual a variavel que o parametro vai ver

temperaturas = dados["hourly"]["temperature_2m"] #chamo a base de dados, informo o parametro e qual a variavel que o parametro vai ver

plt.plot(horas, temperaturas) #plotar o grafico com horas e temperaturas
#plt.plot cria um grafico aonde informo como parametro o eixo x e depois o eixo y
#pltplot(eixo_x, eixo_y)
plt.title("TEMPERATURA POR HORA") #titulo do grafico

#para ver o grafico
plt.show() #mostrar o grafico
