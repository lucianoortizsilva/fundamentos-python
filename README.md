[![Build & Publish Docker Image](https://github.com/lucianoortizsilva/pokemon-orquestracao-dados/actions/workflows/build-publish-docker.yml/badge.svg)](https://github.com/lucianoortizsilva/pokemon-orquestracao-dados/actions/workflows/build-publish-docker.yml) 

### Tecnologias

- <img src="https://badges.aleen42.com/src/python.svg" alt="badge"/> 
- <img src="https://badges.aleen42.com/src/docker.svg" alt="badge"/> 

### O que é ?
Uma aplicação web em python, que extrai dados de 3 diferentes base de dados (excel, mongoDB, MySQL), transforma esse dados, e insere esses dados transformados em outra base de dados "datalake" (MongoDB).

### Arquitetura
![](https://github.com/lucianoortizsilva/pokemon-extracao-dados/blob/main/.static/img/_arquitetura.png?raw=true)

### Como rodar
- Execute na raiz do projeto o comando `docker-compose up`

- Para extrair, trasformar e carregar os dados:
  - Acesse a API GET: `http://localhost:5000/api/legado/etl`

- Para consultar os dados no "datalake":
  - Acesse a API GET: `http://localhost:5000/api/datalake/pokemons`
