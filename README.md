# Prova de Conceito (PoC) - Repositório de Dados Espaciais (TRAMA)

Este repositório contém uma arquitetura inicial desenvolvida como estudo de caso para as necessidades de estruturação de dados espaciais e geoprocessamento do grupo de pesquisa TRAMA (UFC).

O objetivo deste mini-projeto é demonstrar o fluxo de extração, limpeza e armazenamento estruturado de grandes volumes de informações de transporte (coordenadas de GPS, rotas, demanda), garantindo integridade e performance na consulta.

## 🛠️ Arquitetura Proposta
A solução foi desenhada utilizando tecnologias de código aberto e foco em eficiência relacional:
*   **Python:** Utilizado para a etapa de ETL (Extract, Transform, Load), realizando a limpeza dos dados brutos e estruturando os objetos em formatos espaciais (ex: GeoJSON estruturado).
*   **PostgreSQL + PostGIS:** O banco de dados relacional foi escolhido por sua robustez. A extensão PostGIS foi implementada para permitir o armazenamento nativo de geometrias (Pontos, Linhas, Polígonos) e indexação espacial (`GIST`), otimizando o cruzamento de grandes bases de transporte.

## 📂 Estrutura dos Arquivos
*   `etl_spatial_pipeline.py`: Script de automação que simula o tratamento de dados brutos de rotas e a validação de atributos.
*   `schema_trama.sql`: Script de modelagem do banco de dados, incluindo a ativação da extensão espacial e a criação de índices de performance.

---
*Desenvolvido por Moisés de Carvalho como estudo prático de estruturação de dados geográficos.*
