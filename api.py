import requests as rq 
import streamlit as st

st.title("Consulta de CEP com o Brasil API")
st.write("Digite um CEP para buscar informações sobre o endereço.")

cep_input = st.text_input("Digite o CEP (somente números)", max_chars=8)

if st.button("Buscar Cep"):
    if len(cep_input) != 8 or not cep_input.isdigit():
        st.error("O CEP deve conter 8 dígitos e apenas números")
    else:
        with st.spinner("Buscando..."):
            url = f"https://brasilapi.com.br/api/cep/v1/{cep_input}"
            response = rq.get(url)

    try:
        response = rq.get(url)
        if response.status_code == 200:
            dados = response.json()
            st.success("CEP encontrado!")
            st.write("---")
            st.subheader("Informações do Endereço")
            st.markdown(f"**CEP:** {dados.get('cep', 'N/A')}")
            st.markdown(f"**Estado:** {dados.get('state', 'N/A')}")
            st.markdown(f"**Cidade:** {dados.get('city', 'N/A')}")
            st.markdown(f"**Bairro:** {dados.get('neighborhood', 'N/A')}")
            st.markdown(f"**Rua:** {dados.get('street', 'N/A')}")
        else:
            print(f"Erro: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro: {e}")
else:
    st.warning("Por favor, digite um CEP para buscar.")

st.title("Consulta de DDD com o Brasil API")
st.write("Digite um DDD para saber quais outros lugares o utilizam")

ddd_input = st.text_input("Digite o DDD (apenas números)", max_chars=2)

if st.button("Buscar DDD"):
    if len(ddd_input) != 2 or not ddd_input.isdigit():
        st.error("O DDD deve conter apenas 2 dígitos e apenas números")
    else:
        with st.spinner("Buscando..."):
            url1 = f"https://brasilapi.com.br/api/ddd/v1/{ddd_input}"
            response = rq.get(url1)
    try:
        if response.status_code == 200:
            dados = response.json()
            st.success("DDD encontrado!")
            st.write("---")
            st.markdown(f"**Estado:** {dados.get('state', 'N/A')}")
            st.markdown(f"**Cidades:**")
            for cidade in dados.get('cities', []):
                st.write(f"- {cidade}")
        else:
            print(f"Erro: {response.status_code}")
    except rq.exceptions.RequestException as e:
        print(f"Ocorreu um erro: {e}")
else:
    st.warning("Por favor, digite um DDD para buscar.")

st.title("Consulta de feriados com o Brasil API")
st.write("Digite um ano para saber quais feriados e os dias dos mesmos")

ano_input = st.text_input("Digite o ano (apenas números)", max_chars=4)

if st.button("Buscar feriados"):
    if len(ano_input) != 4 or not ano_input.isdigit():
        st.error("O ano deve conter só 4 dígitos e apenas númerois")
    else:
        with st.spinner("Buscando..."):
            url2 = f"https://brasilapi.com.br/api/feriados/v1/{ano_input}"
            response = rq.get(url2)

    try:
        if response.status_code == 200:
            dados = response.json()
            st.success("Feriados encontrados!")
            st.write("A data é escrita em AAAA/MM/DD")
            st.write("---")
            for i in dados:
                st.markdown(f"**Data:** {i['date']}")
                st.markdown(f"**Nome:** {i['name']}")
                st.markdown(f"**Tipo:** {i['type']}")
                st.write("---")
        else:
            print(f"Erro: {response.status_code}")
    except rq.exceptions.RequestException as e:
        print(f"Ocorreu um erro: {e}")
else:
    st.warning("Por favor, digite um ano para buscar.")