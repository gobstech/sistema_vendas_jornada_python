import streamlit as st
import pandas as pd
import plotly.express as px

tabela_vendas = pd.read_csv("vendas.csv")

st.write("# Sistema de Vendas")

st.sidebar.write("## Cadastrar Vendas")
data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor")
botao_cadastrar = st.sidebar.button("Cadastrar Venda")

if botao_cadastrar:
  nova_venda = [str(data), vendedor, produto, quantidade, valor]
  ultima_linha = len(tabela_vendas)
  tabela_vendas.loc[ultima_linha] = nova_venda
  tabela_vendas.to_csv("vendas.csv", index=False)
  st.success("Venda cadastrada!")

st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas)

st.write("## Dashboard")
faturamento=tabela_vendas["valor"].sum()
st.metric("Faturamento Total", f"R$ {faturamento}")

grafico1=px.bar(tabela_vendas, x="vendedor", y="valor", color="produto")
st.plotly_chart(grafico1)

grafico2=px.pie(tabela_vendas, names="produto", values="valor", hole=0.5)
st.plotly_chart(grafico2)
