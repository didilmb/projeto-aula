import streamlit as st
st.write("Alô mundo")

import streamlit as st

st.write("Alô mundo")

nome = st.text_input("Digite o seu nome:")
if nome:
    st.write(nome.upper())

st.write("Vamos brincar de adivinhar fatos!")

time = st.text_input("Qual é o melhor time do Brasil?")

if time.lower() == "flamengo":
    st.write("Parabéns! Você acertou! SRN")
elif time:  
    st.write("Errado!")
