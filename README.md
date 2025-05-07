# ➕➖ Calculadora Simples com Streamlit

Um exercício prático para aprender e aplicar os fundamentos da biblioteca Streamlit para Python.

## 🚀 O que é Streamlit?

Streamlit é uma biblioteca Python de código aberto que facilita a criação e o compartilhamento de aplicativos da web personalizados para aprendizado de máquina e ciência de dados. Com uma sintaxe simples e intuitiva, é possível transformar scripts Python em interfaces interativas sem a necessidade de conhecimento prévio em desenvolvimento web.

## 🛠️ Tecnologias e Conceitos Utilizados

Este projeto foi construído utilizando as seguintes tecnologias e conceitos do Streamlit:

### 🧱 Layout com `st.columns`

Utilizamos a função `st.columns` para organizar os botões da calculadora em um formato de grade, criando linhas e colunas para uma interface mais intuitiva.

### 💾 Gerenciamento de Estado com `st.session_state`

O `st.session_state` foi fundamental para manter o estado da calculadora entre as interações do usuário. Através dele, gerenciamos:

* O primeiro número (`firstNumber`).
* O operador selecionado (`operator`).
* O segundo número (`secondNumber`).
* O resultado da operação (`result`).
* A lista de dígitos que o usuário está digitando (`currentDigit`).

### 🖱️ Interação com `st.button`

Os botões (`st.button`) foram usados para capturar a entrada do usuário para os dígitos e as operações da calculadora. Cada clique em um botão aciona uma re-execução do script, permitindo a atualização do estado.

### 🖋️ Exibição com `st.write`

A função `st.write` foi utilizada para exibir o estado atual da calculadora, mostrando os números, o operador e o resultado na interface.

### 🔄 Atualização da Interface com `st.rerun`

Em alguns casos, `st.rerun()` foi utilizado para forçar a atualização imediata da interface após uma interação do usuário, garantindo uma experiência mais responsiva.

## 🧪 Teste a Calculadora Online!

Você pode experimentar esta calculadora simples diretamente no Streamlit Community Cloud:

[https://calculadora-gustavobritto.streamlit.app](https://calculadora-gustavobritto.streamlit.app)

## ⏭️ Próximos Passos (Melhorias Futuras)

Este projeto é um trabalho em andamento e pretende ser aprimorado com as seguintes funcionalidades:

* Adição do botão '0'.
* Implementação de um display para mostrar a entrada e o resultado de forma mais clara.
* Suporte para mais operações matemáticas (multiplicação, divisão, etc.).
* Refinamento da lógica para uma experiência de usuário mais fluida e intuitiva.
* Possível tratamento de erros (divisão por zero, etc.).

## 🎯 Objetivo

O principal objetivo deste repositório é documentar o processo de aprendizado da biblioteca Streamlit e demonstrar a criação de uma aplicação interativa básica.

