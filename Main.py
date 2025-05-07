import streamlit as st

st.title("Calculadora simples py+Streamlit")

col0,col1,col2,col3 = st.columns(4,gap="small",border=True)
col4,col5,col6,col7 = st.columns(4,gap="small",border=True)
col8,col9,col10,col11 = st.columns(4,gap="small",border=True)

if 'firstNumber' not in st.session_state:
    st.session_state.firstNumber=0
if 'operator' not in st.session_state:
    st.session_state.operator="_"
if 'secondNumber' not in st.session_state:
    st.session_state.secondNumber=0
if 'result' not in st.session_state:
    st.session_state.result=0

if 'currentDigit' not in st.session_state:
    st.session_state.currentDigit=[]

if 'Cont' not in st.session_state:
    st.session_state.Cont=0

with col0:
    if st.button('7'):
        st.session_state.currentDigit.append("7")
with col1:
    if st.button('8'):
        st.session_state.currentDigit.append("8")
with col2:
    if st.button('9'):
        st.session_state.currentDigit.append("9")
with col3:
    if st.button('Add'):
        st.session_state.operator = " + "

        stringNumber="".join(st.session_state.currentDigit)
        intNumber=int(stringNumber)
        if st.session_state.firstNumber == 0:
            st.session_state.firstNumber=intNumber
        else:
            st.session_state.secondNumber=intNumber

        st.session_state.currentDigit=[]
        st.rerun()
with col4:
    if st.button('4'):
        st.session_state.currentDigit.append("4")
with col5:
    if st.button('5'):
        st.session_state.currentDigit.append("5")
with col6:
    if st.button('6'):
        st.session_state.currentDigit.append("6")
with col7:
    if st.button('Sub'):
        st.session_state.operator = " - "
        stringNumber = "".join(st.session_state.currentDigit)
        intNumber = int(stringNumber)
        if st.session_state.firstNumber == 0:
            st.session_state.firstNumber = intNumber
        else:
            st.session_state.secondNumber = intNumber
            st.session_state.result = st.session_state.firstNumber - st.session_state.secondNumber

        st.session_state.currentDigit = []
        st.rerun()
with col8:
    if st.button('1'):
        st.session_state.currentDigit.append("1")
with col9:
    if st.button('2'):
        st.session_state.currentDigit.append("2")
with col10:
    if st.button('3'):
        st.session_state.currentDigit.append("3")
with col11:
    if st.button('='):
        stringNumber = "".join(st.session_state.currentDigit)
        intNumber = int(stringNumber)
        if st.session_state.firstNumber == 0:
            st.session_state.firstNumber = intNumber
        else:
            st.session_state.secondNumber = intNumber
            if st.session_state.operator==" - ":
                st.session_state.result = st.session_state.firstNumber - st.session_state.secondNumber
            elif st.session_state.operator==" + ":
                st.session_state.result = st.session_state.firstNumber + st.session_state.secondNumber



        st.session_state.currentDigit = []

if st.button("Limpar"):
    if 'currentDigit' in st.session_state:
        st.session_state.currentDigit = []
        st.session_state.firstNumber=0
        st.session_state.secondNumber=0
        st.session_state.result=0
        st.rerun()

st.write(f"{st.session_state.firstNumber} {st.session_state.operator} {st.session_state.secondNumber} = {st.session_state.result}")




