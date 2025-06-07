# FIAP - Faculdade de Inteligência Artificial

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Global solution

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/company/inova-fusca">Guilherme Campos Hermanowski </a>
- <a href="https://www.linkedin.com/company/inova-fusca">Gabriel Viel </a>
- <a href="https://www.linkedin.com/company/inova-fusca"> Matheus Alboredo Soares</a> 
- <a href="https://www.linkedin.com/company/inova-fusca">Jonathan Willian Luft </a>
- <a href="https://www.linkedin.com/company/inova-fusca">Fátima Candal</a>


## 👩‍🏫 Professores:

### Tutor(a) 
- <a href="https://www.linkedin.com/company/inova-fusca">Leonardo Ruiz Orabona</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">ANDRÉ GODOI CHIOVATO</a>


## 📜 Sistema de Previsão de Enchentes

*Desenvolver um sistema de previsão de enchentes utilizando Machine Learning, alimentado por dados de precipitação dos últimos 5 dias. O sistema visa fornecer alertas precoces para subsidiar decisões de mitigação de danos.*

## 📁 Estrutura de pastas

Estrutura do Projeto
1. esp32/ - Coleta de Dados (Hardware)
Função: Coleta de dados de precipitação em tempo real (ou simulados) via microcontrolador ESP32.


Pluviômetro Digital com ESP32 e Sensor HC-SR04
Objetivo do Projeto
Este projeto implementa um pluviômetro digital que mede a quantidade de chuva acumulada em um recipiente usando:

Microcontrolador ESP32

Sensor ultrassônico HC-SR04 para medição de distância

Botão para acionamento manual das medições (versão experimental)

A versão experimental com botão simula o funcionamento de um pluviômetro real que faria medições automáticas uma vez por dia.

Para visualizar a versão completa veja o arquivo, redme em ESP32

3. modelo/ - Modelagem e Treinamento de ML
Função: Processamento de dados e treinamento do modelo preditivo.

Principais Componentes:

Features:
Precip_1d, Precip_3d, Precip_7d, Ratio_1d_7d, Acceleration, Impact_Score (derivadas da série temporal de 7 dias).

Modelo:
Usamos KNN (K-Nearest Neighbors) para treinamento do modelo, como nossa base é sintetica, eliminamos a necessidade de normalização e tratamento.

4. streamlit/ - Dashboard de Visualização
Função: Interface interativa para monitoramento de dados e previsões.
Visualização de dados históricos e previsões do modelo.

5. datasets/ - Gestão de Dados
Conteúdo:
Base de dados sintética feita com numpy, 25% de amostras de dias em enchentes e 75% com enchentes.

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

Análise Exploratória de Dados (EDA) em R - Dados INMET SP

Relatório de Análise Exploratória de Dados (EDA) - Dados INMET SP

1. Introdução

Este relatório apresenta uma Análise Exploratória de Dados (EDA) do dataset Dados_INMET_2022_2024_SP_V2.csv. O objetivo é entender a estrutura dos dados, identificar padrões, anomalias e relações entre as variáveis, fornecendo insights iniciais sobre as condições meteorológicas e ocorrências de inundações em São Paulo entre 2022 e 2024.

2. Preparação e Carregamento dos Dados

O dataset foi carregado utilizando a linguagem R e o pacote readr. A inspeção inicial confirmou que o dataset contém 26.304 linhas e 22 colunas, abrangendo diversas variáveis meteorológicas e um indicador de inundação (flood).

Estrutura Inicial do Dataset:

Plain Text


Rows: 26304 Columns: 22
── Column specification ────────────────────────────────────────────────────────
Delimiter: ","
chr  (1): datahora
dbl (21): precipitacao, pressao_estacao, pressao_nmm, pressao_max_ant, press...

ℹ Use `spec()` to retrieve the full column specification for this data.
ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
Dimensões do dataset:
[1] 26304    22

Primeiras 5 linhas do dataset:
# A tibble: 6 × 22
  datahora      precipitacao pressao_estacao pressao_nmm pressao_max_ant
  <chr>                <dbl>           <dbl>       <dbl>           <dbl>
1 1/1/2022 0:00          0              922.       1009.            922.
2 1/1/2022 1:00          0              922.       1009.            922 
3 1/1/2022 2:00          0              922.       1009.            922.
4 1/1/2022 3:00          0              922.       1009.            922.
5 1/1/2022 4:00          0.2            921.       1008.            922.
6 1/1/2022 5:00          0              920.       1008.            921.
# ℹ 17 more variables: pressao_min_ant <dbl>, radiacao <dbl>, temp_cpu <dbl>,
#   temp_ar <dbl>, temp_orvalho <dbl>, temp_max_ant <dbl>, temp_min_ant <dbl>,
#   orvalho_max_ant <dbl>, orvalho_min_ant <dbl>, tensao_bateria <dbl>,
#   umidade_max_ant <dbl>, umidade_min_ant <dbl>, umidade_ar <dbl>,
#   vento_direcao <dbl>, vento_rajada <dbl>, vento_velocidade <dbl>,
#   flood <dbl>

Estrutura do dataset:
spc_tbl_ [26,304 × 22] (S3: spec_tbl_df/tbl_df/tbl/data.frame)
 $ datahora        : chr [1:26304] "1/1/2022 0:00" "1/1/2022 1:00" "1/1/2022 2:00" "1/1/2022 3:00" ...


3. Análise Exploratória Inicial

Após o carregamento, foi realizada uma inspeção mais aprofundada dos dados. A coluna datahora foi convertida para o formato de data e hora (POSIXct) para facilitar análises temporais. Também foram verificados os valores ausentes (NA) em cada coluna e geradas estatísticas descritivas para as variáveis numéricas.

Valores Ausentes por Coluna:

Plain Text


        datahora     precipitacao  pressao_estacao      pressao_nmm 
               0              664              181             1157 
 pressao_max_ant  pressao_min_ant         radiacao         temp_cpu 
             181              181              181              179 
         temp_ar     temp_orvalho     temp_max_ant     temp_min_ant 
            1157             1160             1156             1155 
 orvalho_max_ant  orvalho_min_ant   tensao_bateria  umidade_max_ant 
            1155             1155              179             1155 
 umidade_min_ant       umidade_ar    vento_direcao     vento_rajada 
            1155             1160             2760             2781 
vento_velocidade            flood 
            2765                0 


Observa-se a presença de valores ausentes em diversas colunas, sendo vento_direcao, vento_rajada e vento_velocidade as mais afetadas. A coluna flood não possui valores ausentes.

Estatísticas Descritivas para Variáveis Numéricas:

Plain Text


  precipitacao     pressao_estacao  pressao_nmm   pressao_max_ant
 Min.   : 0.0000   Min.   :915.3   Min.   :1000   Min.   :915.7  
 1st Qu.: 0.0000   1st Qu.:925.7   1st Qu.:1012   1st Qu.:926.0  
 Median : 0.0000   Median :928.0   Median :1016   Median :928.3  
 Mean   : 0.1698   Mean   :928.2   Mean   :1016   Mean   :928.4  
 3rd Qu.: 0.0000   3rd Qu.:930.6   3rd Qu.:1019   3rd Qu.:930.9  
 Max.   :47.0000   Max.   :940.9   Max.   :1032   Max.   :941.0  
 NA\'s   :664       NA\'s   :181     NA\'s   :1157   NA\'s   :181    
 pressao_min_ant    radiacao         temp_cpu        temp_ar     
 Min.   :915.1   Min.   :  -3.6   Min.   : 6.00   Min.   : 4.90  
 1st Qu.:925.5   1st Qu.:  -2.8   1st Qu.:18.00   1st Qu.:16.60  
 Median :927.8   Median :  22.5   Median :21.00   Median :19.60  
 Mean   :927.9   Mean   : 641.9   Mean   :22.17   Mean   :19.83  
 3rd Qu.:930.4   3rd Qu.:1062.0   3rd Qu.:25.00   3rd Qu.:22.40  
 Max.   :940.8   Max.   :4043.0   Max.   :42.00   Max.   :37.90  
 NA\'s   :181     NA\'s   :181      NA\'s   :179     NA\'s   :1157   
  temp_orvalho    temp_max_ant    temp_min_ant   orvalho_max_ant
 Min.   :-7.50   Min.   : 5.90   Min.   : 4.80   Min.   :-6.1   
 1st Qu.:13.80   1st Qu.:16.90   1st Qu.:16.20   1st Qu.:14.3   
 Median :16.70   Median :20.00   Median :19.10   Median :17.3   
 Mean   :16.22   Mean   :20.39   Mean   :19.31   Mean   :16.8   
 3rd Qu.:19.20   3rd Qu.:23.20   3rd Qu.:21.70   3rd Qu.:19.7   
 Max.   :27.30   Max.   :38.50   Max.   :37.00   Max.   :27.9   
 NA\'s   :1160    NA\'s   :1156    NA\'s   :1155    NA\'s   :1155   
 orvalho_min_ant tensao_bateria  umidade_max_ant  umidade_min_ant 
 Min.   :-8.50   Min.   :11.40   Min.   : 13.00   Min.   : 10.00  
 1st Qu.:13.20   1st Qu.:12.40   1st Qu.: 76.00   1st Qu.: 68.00  
 Median :16.20   Median :12.60   Median : 92.00   Median : 86.00  
 Mean   :15.68   Mean   :13.06   Mean   : 85.23   Mean   :79.75  
 3rd Qu.:18.70   3rd Qu.:14.10   3rd Qu.:100.00   3rd Qu.: 97.00  
 Max.   :25.00   Max.   :14.60   Max.   :100.00   Max.   :100.00  
 NA\'s   :1155    NA\'s   :179     NA\'s   :1155     NA\'s   :1155    
   umidade_ar     vento_direcao    vento_rajada    vento_velocidade
 Min.   : 11.00   Min.   :  1.0   Min.   : 0.400   Min.   :0.100   
 1st Qu.: 72.00   1st Qu.:121.0   1st Qu.: 3.200   1st Qu.:1.100   
 Median : 89.00   Median :148.0   Median : 4.900   Median :1.800   
 Mean   : 82.55   Mean   :180.3   Mean   : 5.162   Mean   :1.969   
 3rd Qu.:100.00   3rd Qu.:294.0   3rd Qu.: 6.900   3rd Qu.:2.700   
 Max.   :100.00   Max.   :360.0   Max.   :29.900   Max.   :8.000   
 NA\'s   :1160     NA\'s   :2760    NA\'s   :2781     NA\'s   :2765    
     flood         
 Min.   :0.000000  
 1st Qu.:0.000000  
 Median :0.000000  
 Mean   :0.002091  
 3rd Qu.:0.000000  
 Max.   :1.000000  
                   


4. Visualizações de Dados

Foram gerados diversos gráficos para visualizar a distribuição das variáveis e identificar possíveis relações:

4.1. Distribuição da Precipitação

Este histograma mostra a frequência dos diferentes níveis de precipitação. A maioria dos registros indica baixa ou nenhuma precipitação, com alguns picos de alta precipitação.


4.2. Temperatura do Ar por Mês

O boxplot da temperatura do ar por mês revela a variação sazonal da temperatura, com meses mais quentes e mais frios, e a dispersão dos dados dentro de cada mês.

4.3. Precipitação vs. Temperatura do Ar

Este gráfico de dispersão explora a relação entre precipitação e temperatura do ar. Não há uma correlação linear óbvia, mas é possível observar que eventos de alta precipitação ocorrem em diversas faixas de temperatura.


4.4. Umidade do Ar Média Diária ao Longo do Tempo

O gráfico de linha da umidade do ar média diária mostra a tendência da umidade ao longo do período, permitindo identificar variações diárias e sazonais.


4.5. Precipitação em Casos de Inundação

Este boxplot compara a distribuição da precipitação em dias com e sem inundação. É evidente que os dias com inundação (flood = 1) apresentam níveis de precipitação significativamente mais altos, como esperado.

5. Conclusão

A análise exploratória inicial revelou a estrutura do dataset, a presença de valores ausentes e as distribuições das principais variáveis meteorológicas. As visualizações confirmaram que a precipitação é um fator chave para a ocorrência de inundações, com eventos de flood = 1 associados a maiores volumes de chuva. A presença de valores ausentes em algumas colunas sugere a necessidade de um tratamento de dados antes de qualquer modelagem preditiva. As tendências sazonais de temperatura e umidade também foram observadas, fornecendo um contexto importante para futuras análises.


