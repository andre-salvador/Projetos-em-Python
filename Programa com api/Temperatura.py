import requests


api_key = '661c34ce423d394ed21a4facc23bde92'

cidade = str(input('Digite a cidade que você deseja saber a temperatura: '))

link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br"

requisicao = requests.get(link)
requisicao_dicionario = requisicao.json()

descricao = requisicao_dicionario['weather'][0]['description']
temperatura = requisicao_dicionario['main']['temp'] - 273.15

print(f'O tempo está: {descricao} e a temperatura é: {temperatura:.0f}ºC')