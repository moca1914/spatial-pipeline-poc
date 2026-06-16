import json

# Simulação de uma base de dados bruta recebida de parceiros (ex: Prefeitura/GPS de ônibus)
# Contém ruídos (ex: valores negativos) e dados desestruturados.
dados_brutos_transporte = [
    {"linha": "029 - Parangaba/Náutico", "id_parada": 101, "lat": -3.7327, "lon": -38.5270, "passageiros_dia": 1200},
    {"linha": "030 - Siqueira/Papicu", "id_parada": 102, "lat": -3.7445, "lon": -38.5358, "passageiros_dia": 2500},
    {"linha": "074 - Antônio Bezerra/Unifor", "id_parada": 103, "lat": -3.7704, "lon": -38.4791, "passageiros_dia": -50}, # Dado inválido 
    {"linha": "075 - Campus do Pici/Unifor", "id_parada": 104, "lat": -3.7412, "lon": -38.5721, "passageiros_dia": 3100}
]

def processar_dados_espaciais(base_bruta):
    """
    Função de limpeza e estruturação.
    Filtra dados inválidos e converte as coordenadas para um formato espacial estruturado.
    """
    dados_limpos = []
    
    for registro in base_bruta:
        # A lógica de limpeza é ignorar registros com erro de contagem de passageiros
        if registro.get("passageiros_dia", 0) > 0:
            
            # Estruturando o dado para um formato pronto para inserção no banco
            dado_estruturado = {
                "linha": registro["linha"].strip().upper(),
                "id_parada": registro["id_parada"],
                "demanda_diaria": registro["passageiros_dia"],
                # Isolando a geometria para facilitar o geoprocessamento
                "geometria": {
                    "tipo": "Ponto",
                    "coordenadas": [registro["lon"], registro["lat"]] # Uso de longitude e latitude
                }
            }
            dados_limpos.append(dado_estruturado)
            
    return dados_limpos

if __name__ == "__main__":
    print("Iniciando pipeline de tratamento de dados espaciais...\n")
    
    base_processada = processar_dados_espaciais(dados_brutos_transporte)
    
    print("=== DADOS ESTRUTURADOS E PRONTOS PARA O BANCO DE DADOS ===")
    print(json.dumps(base_processada, indent=4, ensure_ascii=False))
