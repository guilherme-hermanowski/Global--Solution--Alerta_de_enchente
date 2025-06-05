# -*- coding: utf-8 -*-
"""
Algoritmo de Predição de Risco de Alagamento usando K-Nearest Neighbors (KNN).

Este script implementa um modelo KNN para classificar áreas com base no risco
de alagamento, utilizando dados fornecidos pelo usuário. Inclui funcionalidades
para carregar dados, treinar o modelo, fazer predições e alertar o usuário
sobre áreas de alto risco.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np # Adicionado para exemplo de dados

arq = open("dados_pluviometricos.csv", "r")

df = pd.read_csv(arq)

print(df.head)

def carregar_e_preparar_dados(arq):
    """
    Carrega os dados do arquivo csv anexo e realiza o pré-processamento inicial.
    Returns:
        tuple: Uma tupla contendo o DataFrame pré-processado, as features (X) 
               e o target (y).
               Retorna (None, None, None) se o carregamento falhar.
    """
    try:
        # Tenta ler o arquivo CSV fornecido
        try:
            df = pd.read_csv(arq)
            print(f"Arquivo '{arq}' carregado com sucesso.")
        except FileNotFoundError:
            print(f"Aviso: Arquivo '{arq}' não encontrado.")
            df = None # Define df como None se o arquivo não existe
        except Exception as e:
            print(f"Erro ao ler o arquivo '{arq}': {e}")
            return None, None, None, None # Retorna erro se a leitura falhar por outros motivos

        # Define a coluna target esperada
        target_col = 'risco_alagamento'

        # --- Bloco de Verificação e Geração de Exemplo ---
        # Verifica se o df foi carregado ou se a coluna target está ausente
        if df is None or target_col not in df.columns:
            pass
            """if df is None:
                print("Gerando dados de exemplo pois o arquivo não foi encontrado.")
            else: # df não é None, mas target_col está ausente
                print(f"Aviso: Coluna target 	'{target_col}	' não encontrada no arquivo. Gerando dados de exemplo.")
            
            # Gerar dados de exemplo
            num_samples = 100
            df = pd.DataFrame({
                'nivel_chuva_mm': np.random.rand(num_samples) * 100,
                'historico_alagamentos': np.random.randint(0, 5, num_samples),
                'altitude_m': np.random.rand(num_samples) * 50,
                'permeabilidade_solo': np.random.rand(num_samples),
                target_col: np.random.randint(0, 3, num_samples) # 0: Baixo, 1: Médio, 2: Alto
            })
            # Definir features para o caso de exemplo
            features_cols = ['nivel_chuva_mm', 'historico_alagamentos', 'altitude_m', 'permeabilidade_solo']
            print("Dados de exemplo gerados.")"""
        else:
            # Se o df foi carregado e a coluna target existe
            print(f"Coluna target 	'{target_col}	' encontrada. Usando colunas restantes como features.")
            features_cols = [col for col in df.columns if col != target_col]
        # --- Fim Bloco de Verificação e Geração de Exemplo ---

        # Extrair features (X) e target (y) do DataFrame final (seja do arquivo ou exemplo)
        X = df[features_cols]
        y = df[target_col]

        # TODO: Adicionar mais pré-processamento se necessário (tratamento de nulos, etc.)

        # Normalização das features (importante para KNN)
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        X = pd.DataFrame(X_scaled, columns=features_cols)

        print(f"Dados carregados e preparados com sucesso. {len(df)} amostras.")
        return df, X, y, scaler # Retorna o scaler para uso posterior

    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em '{arq}'")
        return None, None, None, None
    except Exception as e:
        print(f"Erro ao carregar ou preparar os dados: {e}")
        return None, None, None, None

def treinar_modelo_knn(X_train, y_train, n_neighbors=5):
    """
    Treina o modelo KNeighborsClassifier.

    Args:
        X_train (pd.DataFrame): DataFrame com as features de treinamento.
        y_train (pd.Series): Series com o target de treinamento.
        n_neighbors (int): Número de vizinhos a considerar no KNN.

    Returns:
        KNeighborsClassifier: O modelo KNN treinado.
    """
    print(f"Treinando modelo KNN com k={n_neighbors}...")
    knn = KNeighborsClassifier(n_neighbors=n_neighbors)
    knn.fit(X_train, y_train)
    print("Modelo treinado.")
    return knn

def avaliar_modelo(modelo, X_test, y_test):
    """
    Avalia o desempenho do modelo treinado usando dados de teste.

    Args:
        modelo (KNeighborsClassifier): O modelo KNN treinado.
        X_test (pd.DataFrame): DataFrame com as features de teste.
        y_test (pd.Series): Series com o target de teste.
    """
    print("\nAvaliando modelo...")
    y_pred = modelo.predict(X_test)
    print("\nMatriz de Confusão:")
    print(confusion_matrix(y_test, y_pred))
    print("\nRelatório de Classificação:")
    print(classification_report(y_test, y_pred))

def fazer_predicoes(modelo, scaler, novos_dados):
    """
    Faz predições para novos dados usando o modelo treinado.

    Args:
        modelo (KNeighborsClassifier): O modelo KNN treinado.
        scaler (StandardScaler): O scaler usado para normalizar os dados de treino.
        novos_dados (pd.DataFrame): DataFrame com os novos dados para predição 
                                   (mesmas colunas de features do treino).

    Returns:
        np.array: Array com as predições de risco.
    """
    print("\nFazendo predições para novos dados...")
    # Normalizar os novos dados com o mesmo scaler do treino
    novos_dados_scaled = scaler.transform(novos_dados)
    predicoes = modelo.predict(novos_dados_scaled)
    return predicoes

def emitir_alerta(predicoes, dados_originais):
    """
    Verifica as predições e emite alertas para áreas de alto risco.

    Args:
        predicoes (np.array): Array com as predições de risco.
        dados_originais (pd.DataFrame): DataFrame original correspondente às predições
                                        para contextualizar o alerta.
    """
    # TODO: Definir o critério de 'alto risco' (ex: classe 2)
    alto_risco_label = 2
    indices_alto_risco = [i for i, pred in enumerate(predicoes) if pred == alto_risco_label]

    if indices_alto_risco:
        print("\n--- ALERTA DE RISCO DE ALAGAMENTO DETECTADO! ---")
        print(f"As seguintes áreas/pontos apresentam alto risco (classe {alto_risco_label}):")
        # Mostrar informações relevantes dos dados originais para as áreas de risco
        # Exemplo: Mostrar as primeiras colunas ou um ID da área
        print(dados_originais.iloc[indices_alto_risco])
        print("--------------------------------------------------")
    else:
        print("\nNenhuma área de alto risco detectada nas novas predições.")

# --- Função Principal ---
def main(caminho_base_dados, caminho_novos_dados=None):
    """
    Função principal que orquestra o fluxo do algoritmo.

    Args:
        caminho_base_dados (str): Caminho para a base de dados de treinamento.
        caminho_novos_dados (str, optional): Caminho para a base de dados com novas
                                             amostras para predição. Se None, usa
                                             o conjunto de teste para demonstração.
    """
    df, X, y, scaler = carregar_e_preparar_dados(caminho_base_dados)

    if df is None:
        print("Não foi possível carregar os dados. Encerrando.")
        return

    # Dividir dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
    print(f"Dados divididos: {len(X_train)} para treino, {len(X_test)} para teste.")

    # Treinar o modelo
    modelo_knn = treinar_modelo_knn(X_train, y_train, n_neighbors=5) # K=5 como exemplo

    # Avaliar o modelo
    avaliar_modelo(modelo_knn, X_test, y_test)

    # Fazer predições e emitir alertas
    if caminho_novos_dados:
        try:
            novos_dados_df = pd.read_csv(caminho_novos_dados)
            # Garantir que as colunas dos novos dados são as mesmas das features de treino
            features_cols = X_train.columns
            if not all(col in novos_dados_df.columns for col in features_cols):
                print(f"Erro: O arquivo de novos dados deve conter as colunas: {list(features_cols)}")
                return
            novos_dados_features = novos_dados_df[features_cols]
            predicoes_novos = fazer_predicoes(modelo_knn, scaler, novos_dados_features)
            emitir_alerta(predicoes_novos, novos_dados_df)
        except FileNotFoundError:
            print(f"Erro: Arquivo de novos dados não encontrado em '{caminho_novos_dados}'")
        except Exception as e:
            print(f"Erro ao processar novos dados: {e}")
    else:
        print("\nDemonstração: Fazendo predições no conjunto de teste e verificando alertas...")
        predicoes_teste = modelo_knn.predict(X_test)
        # Para demonstração, usamos os dados originais correspondentes ao conjunto de teste
        dados_teste_originais = df.loc[X_test.index]
        emitir_alerta(predicoes_teste, dados_teste_originais)

if __name__ == "__main__":
    # --- Configuração --- 
    # Substituir pelo caminho real quando o usuário fornecer
    # Crie um arquivo CSV 'dados_alagamento_exemplo.csv' ou use um existente
    caminho_arquivo_treino = "dados_alagamento_exemplo.csv"
    caminho_arquivo_predicao = None # Ou "novos_dados_alagamento.csv"

    # --- Criação de arquivo de exemplo (se não existir) ---
    import os
    if not os.path.exists(caminho_arquivo_treino):
        print(f"Criando arquivo de exemplo '{caminho_arquivo_treino}'...")
        num_samples = 200
        df_exemplo = pd.DataFrame({
            'nivel_chuva_mm': np.random.rand(num_samples) * 120 + 10, # Chuva entre 10 e 130 mm
            'historico_alagamentos': np.random.randint(0, 6, num_samples), # 0 a 5 eventos passados
            'altitude_m': np.random.rand(num_samples) * 40 + 5, # Altitude entre 5 e 45 m
            'permeabilidade_solo': np.random.rand(num_samples) * 0.8 + 0.1, # Permeabilidade entre 0.1 e 0.9
            'distancia_rio_km': np.random.rand(num_samples) * 5 + 0.1, # Distância do rio entre 0.1 e 5.1 km
            'risco_alagamento': np.random.randint(0, 3, num_samples) # 0: Baixo, 1: Médio, 2: Alto
        })
        df_exemplo.to_csv(caminho_arquivo_treino, index=False)
        print("Arquivo de exemplo criado.")
    # --- Fim Criação de arquivo de exemplo ---

    main(caminho_arquivo_treino, caminho_arquivo_predicao)

