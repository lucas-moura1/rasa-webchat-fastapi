# Rasa webchat fastapi

O objetivo deste respositório é fornecer uma assistente virtual que informe a previsão do tempo, de no máximo 5 dias, para a cidade desejada. O usuário irá abrir um chat que aparece no canto inferior esquerdo da tela e conversará com o bot. A stack back-end é toda desenvolvida em Python e o front-end é apenas um html, CSS e JS puro.

## Tecnologias utilizadas
- Rasa Open Source
- Api Rest em FastAPI

### Rasa Open Source

[Rasa](https://rasa.com/docs/) é um framework de aprendizado de máquina (Machine Learning) de código aberto para conversação em formato de texto e voz. Entende mensagens, mantém conversas e conecta com canais de mensagens, tipo Facebok Messenger e Telegram, e APIs.

#### Assuntos tratados pelo bot

- Saudação
- Despedida
- Quem é vc?
- Previsão do tempo

### FastAPI

[FasAPI](https://fastapi.tiangolo.com/) é um framework web moderno e rápido (alta performance) para construir APIs com Python 3.6+ baseado no padrão Python. Seus principais recursos são velocidade, rápido para "codar", menos bug, intuitivo, fácil, pouco código, robusto e baseado em padrões.

#### Funcionalidades da API

- Obter dados de previsão do tempo

#### Rotas

**Obter dados de previsão do tempo**
```
url: /api/weather?city={city_name}&day={weekday}

params: {
    city: <city_name>,
    day: <weekday>  #optional
}

method: GET
```

## Execução do projeto

Para executar o projeto é preciso ter o `docker` e `docker-compose` instalado na máquina.

### Para executar


- `git clone <url_repositorio>` : clonar o repositório
- `docker-compose up`: rodar a aplicação

Para acessar a API diretamente é preciso acessar http://localhost:8000 + o endPoint. E para acessar o Client de consulta é preciso acessar o arquivo `index.html` dentro da pasta [client](https://github.com/lucas-moura1/rasa-webchat-fastapi/tree/main/client).
