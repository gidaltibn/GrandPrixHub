# GrandPrixHub API

Este é o repositório do back-end da aplicação GrandPrixHub. A aplicação foi desenvolvida utilizando Python com Flask e faz uso do banco de dados SQLite. A API permite gerenciar equipes, pilotos, pistas, corridas e resultados de corridas de Fórmula 1. O projeto tem como objetivo ajudar as pessoas que gostam de acompanhar a Fórmula 1 a terem um ambiente virtual para anotarem os pódios das corridas da temporada e além disso registrarem as equipes, pilotos, pistas e corridas do campeonato.

## Requisitos

- Python 3.8+
- Flask
- SQLite

## Instalação

1. Clone o repositório:
   ```
   git clone https://github.com/gidaltibn/GrandPrixHub.git
   ```

2. Crie um ambiente virtual e ative-o:
   ```
   python -m venv venv
   .venv\\Scripts\\activate
   ```

3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

4. Configure o banco de dados:
   ```
   flask db upgrade
   ```

## Executando a Aplicação

1. Inicie o servidor Flask:
   ```
   flask run
   ```

2. Acesse a documentação Swagger da API em [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Endpoints da API

A API possui os seguintes endpoints principais:

- `GET /equipes/`: Lista todas as equipes.
- `POST /equipes/`: Adiciona uma nova equipe.
- `PUT /equipes/<id>`: Atualiza uma equipe existente.
- `DELETE /equipes/<id>`: Exclui uma equipe.

- `GET /pilotos/`: Lista todos os pilotos.
- `POST /pilotos/`: Adiciona um novo piloto.
- `PUT /pilotos/<id>`: Atualiza um piloto existente.
- `DELETE /pilotos/<id>`: Exclui um piloto.

- `GET /pistas/`: Lista todas as pistas.
- `POST /pistas/`: Adiciona uma nova pista.
- `PUT /pistas/<id>`: Atualiza uma pista existente.
- `DELETE /pistas/<id>`: Exclui uma pista.

- `GET /corridas/`: Lista todas as corridas.
- `POST /corridas/`: Adiciona uma nova corrida.
- `PUT /corridas/<id>`: Atualiza uma corrida existente.
- `DELETE /corridas/<id>`: Exclui uma corrida.

- `GET /resultados/`: Lista todos os resultados.
- `POST /resultados/`: Adiciona um novo resultado.
- `PUT /resultados/<id>`: Atualiza um resultado existente.
- `DELETE /resultados/<id>`: Exclui um resultado.

## Relacionamento entre Classes e Entidades
A aplicação utiliza um modelo relacional para gerenciar os dados de Fórmula 1. Aqui está uma visão geral dos relacionamentos entre as principais classes e entidades:

- Equipe: Uma equipe pode ter vários pilotos associados. A relação é representada pela chave estrangeira equipe_id na tabela de pilotos.
- Piloto: Cada piloto pertence a uma equipe. A tabela de pilotos possui uma chave estrangeira equipe_id que referencia a equipe.
- Pista: Uma pista pode ser associada a várias corridas. A relação é representada pela chave estrangeira pista_id na tabela de corridas.
- Corrida: Cada corrida é realizada em uma pista específica e pode ter vários resultados associados. A tabela de corridas possui uma chave estrangeira pista_id que referencia a pista.
- Resultado: Cada resultado está associado a uma corrida específica e aos pilotos que terminaram em primeiro, segundo e terceiro lugares. A tabela de resultados possui chaves estrangeiras corrida_id, primeiro_lugar_id, segundo_lugar_id, e terceiro_lugar_id que referenciam a corrida e os pilotos.
Esses relacionamentos são implementados usando chaves estrangeiras e relacionamentos bidirecionais no SQLAlchemy.

## Autor

- Gidalti Brito Nascimento
- [Github](https://github.com/gidaltibn)
- [Email](mailto:gidaltibn@outlook.com)
