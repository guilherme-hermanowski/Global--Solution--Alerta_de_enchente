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

6. Análise Exploratória de Dados (EDA) em R - Dados INMET SP

Realizamos uma Análise Exploratória de Dados (EDA) no dataset Dados_INMET_2022_2024_SP_V2.csv para entender a estrutura dos dados, identificar padrões e relações entre as variáveis meteorológicas e a ocorrência de inundações. A análise revelou a presença de valores ausentes em algumas colunas e confirmou que a precipitação é um fator chave para as inundações.

Para mais detalhes sobre a análise, incluindo estatísticas descritivas e visualizações, consulte o arquivo README_R_DETAILED.md.


## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>


