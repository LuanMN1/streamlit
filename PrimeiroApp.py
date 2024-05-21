#CTRL J abre terminal

#cria o ambiente virtual: python -m venv venv

#pip install:
#streamlit
#pandas
#openpyxl
#matplotlib

#ativa ambiente virtual: .\venv\Scripts\activate.bat
#para rodar o app: python -m streamlit run PrimeiroApp.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt

st.title('Meu primeiro app :sunglasses:')

st.image('https://softgraf.com/icones/logo_softgraf.png', width=200)

st.header('Este é um header (cabeçalho).', divider='red')

st.subheader('Este é um subheader: _Streamlit_ é :red[legal!]')

st.write('Este é um texto comum.')

"Texto Mágico!"
texto="Texto na Variável"
texto

x=10
'X=', x

st.markdown('Markdown: *Streamlit* é **realmente** ***legal***')
st.markdown("""
            :red[Streamlit] :orange[pode] :green[escrever] :blue[texto] :violet[em]
            :gray[muitas] :rainbow[cores] e :blue-background[texto destacado]
            """)

multi= """Se terminar a linha com dois espaços,
uma quebra de linha é usada para a próxima linha.

Dois ou mais ENTER resulta em apenas uma quebra de linha
"""

st.markdown(multi)

#----------------------------------------------------------------------------------------------

st.subheader('Abas', divider='red')

aba1, aba2, aba3 = st.tabs(['Tabelas', 'Gráficos', 'Histogramas'])

with aba1:
    st.write('Exibindo um DataFrame com Streamlit')
    df = pd.read_excel('https://softgraf.com/cursodatascience/produtos.xlsx')
    df

with aba2:
    st.write('Exibindo um Gráfico de Linhas')
    #cria um array de 20 linhas x 3 colunas, com valores randômicos (distribuição padrão)
    arr = np.random.randn(20,3)
    tabela = pd.DataFrame(arr, columns=['a','b','c'])
    st.line_chart(tabela)

with aba3:
    st.write('Exibindo um Histograma')
    #cria uma distribuição normal aleatória de tamanho 50 com média 1 e desvio padrão 1
    arr = np.random.normal(1,1,size=50)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)
    fig

#----------------------------------------------------------------------------------------------

st.subheader('Input Widgets', divider='red')

#cria 3 colunas
col1, col2, col3 = st.columns(3)

with col1:
    st.button('Reset', type='primary')
    aceito = st.checkbox('Aceito os Termos')
    if aceito:
        st.write('Aceitou!') 

with col2:
    if st.button('Salvar'):
        st.write('Você Clicou em Salvar')
    else:
        st.write('Reiniciou')

    on = st.toggle('Ligar Recursos')
    if on:
        st.write('Recurso Ligado')

with col3:
    st.link_button('Ir para Galeria', 'https://streamlit.io/gallery')
    cor = st.color_picker('Escolha uma Cor')
    st.write('A Cor Escolhida Foi:', cor)

cidades = ['Ponta Grossa', 'Curitiba', 'Castro', 'Carambei', 'Pirai do Sul']
padroes = ['Curitiba', 'Castro', 'Carambei']
with st.expander('Expander Cidades'):
    escolhidas = st.multiselect('Selecione as Cidades', cidades, padroes)

st.write('Cidades Escolhidas:', escolhidas)

#==== barra lateral ====
with st.sidebar:
    mensagens = st.container(height=300)
    #novo 'operador morsa' := (a partir do python 3.8)
    if prompt := st.chat_input('Digite Algo'):
        mensagens.chat_message('Usuário').write(prompt)