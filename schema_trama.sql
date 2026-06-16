-- 1. Criação do Banco de Dados Central
CREATE DATABASE trama_spatial_db;

-- 2. Ativação da extensão de Geoprocessamento (O motor espacial do PostgreSQL)
CREATE EXTENSION IF NOT EXISTS postgis;

-- 3. Criação da tabela de paradas de transporte
CREATE TABLE estacoes_transporte (
    id_parada SERIAL PRIMARY KEY,
    nome_linha VARCHAR(150) NOT NULL,
    demanda_diaria INT CHECK (demanda_diaria >= 0),
    
    -- Coluna nativa do PostGIS para armazenar geometria. 
    -- SRID 4326 é o padrão mundial (WGS 84) utilizado pelo GPS.
    geometria_localizacao GEOMETRY(Point, 4326)
);

-- 4. Criação de Índice Espacial
-- Essencial para manter a performance quando o TRAMA cruzar grandes volumes de dados de Fortaleza
CREATE INDEX idx_estacoes_geom 
ON estacoes_transporte 
USING GIST (geometria_localizacao);
