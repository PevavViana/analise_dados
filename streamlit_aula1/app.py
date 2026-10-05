import pandas as pd;
import streamlit as st;

st.title("Meu primeiro dash")
st.subheader("Renan Viana dos Santos")

st.write("Hello World streamlit")

name = st.text_input("Digite seu nome: ")
age = st.number_input("Digite sua idade: ", step=1)


st.write(name, age)

st.divider()

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

st.divider()

compras = {
  "Arroz": {
    "Price": 10,
  },
  "Arroz Doce": {
    "Price": 20,
  }
}

list = []

for key in compras.keys():
    list.append(key)
  
content = st.selectbox("Mercado", list)
qtde = st.slider("Quantidade", 0, 100)

total_preco = sum(compras[content].values()) * qtde

# Não precisa especificar label e value
st.metric("Preço", f"R$ {total_preco}")  

