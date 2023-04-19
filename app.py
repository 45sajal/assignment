import streamlit as st
st.title('find the largest among the 3 numbers')
num1=st.number_input('Enter number 1')
num2=st.number_input('Enter number 2')
num3=st.number_input('Enter number 3')
calculate=st.button('find lasgest number')
def largest_number(a,b,c):
    if a>c and a>b:
        return a
    if b>a and b>c:
        return b
    else:
        return c
if calculate:
    largest_num=largest_number(num1,num2,num3)
    st.write('the largest number is:', largest_num)
