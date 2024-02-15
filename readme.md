Desafio: Consumidor de API de Informações Geográficas e Criação de API

Objetivo Geral:

Desenvolver um sistema composto por duas partes principais:

API RESTful: Criar uma API RESTful que forneça informações sobre países, permitindo busca por região e palavra-chave.
Aplicativo Consumidor: Desenvolver um aplicativo em sua linguagem de programação preferida que consuma esta API para buscar informações sobre países com base na região e em uma palavra-chave específica.

Parte 1: Criação da API RESTful
Objetivos da API:

Implementar endpoints que permitam aos usuários buscar países por região e palavra-chave.
A API deve suportar paginação nas respostas, incluindo metadados sobre a paginação nos resultados.
Requisitos Funcionais da API:

A API deve oferecer um endpoint que aceite parâmetros de consulta para região e palavra-chave.
Responder com dados paginados, incluindo: page, per_page, total, total_pages, e data.
O campo data deve retornar um array de objetos, cada um representando um país com atributos como name (nome do país), region (região), e population (população).

Tecnologias Sugeridas:

A API pode ser implementada usando frameworks como Flask ou FastAPI para Python, Spring Boot para Java, ou Echo ou Gin para Go.

Parte 2: Aplicativo Consumidor
Objetivos do Aplicativo:

Consumir a API RESTful criada na Parte 1 para buscar informações sobre países com base na região e palavra-chave fornecidas pelo usuário.
Processar a resposta paginada da API e apresentar uma lista de países e suas respectivas populações.
Requisitos Funcionais do Aplicativo:

Aceitar dois parâmetros de entrada do usuário: região e palavra-chave.
Processar todas as páginas da resposta para coletar informações de todos os países correspondentes.
Apresentar ao usuário uma lista dos países encontrados, incluindo o nome do país e sua população.
