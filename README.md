
#API LGPD
Esse projeto almeja facilitar a requisição de artigos da Lei Geral de Proteção de Dados Pessoais (Lei nº 13.709/2018)

A chamada GET /artigo com o número do artigo de interesse no final do link, retorna um vetor de objetos JSON contendo os seguintes campos:

* `artigo`: Numero do artigo.
* `capitulo`: Número e descrição resumida do capitulo.
* `texto`: Texto completo do artigo, contendo incisos e paragragos.
* `titulo`: Titulo do artigo.

Ex: 0.0.0.0:8000/artigo1

[
  {
    "artigo": "1", 
    "capitulo": "Capítulo I - DISPOSIÇÕES PRELIMINARES", 
    "texto": "Esta Lei dispõe sobre o tratamento de dados pessoais, inclusive nos meios digitais, por pessoa natural ou por pessoa jurídica de direito público ou privado, com o objetivo de proteger os direitos fundamentais de liberdade e de privacidade e o livre desenvolvimento da personalidade da pessoa natural.", 
    "titulo": "Objeto da Lei"
  }
]


Link da API: https://api-lgpd.protocoloone.repl.co/