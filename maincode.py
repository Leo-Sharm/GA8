import streamlit as st

def find_largest(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3

st.title("Find the Largest Number")

# create three mandatory input fields for the user to enter numbers
num1 = st.number_input("Enter the first number:", value=0.0, step=None, required=True)
num2 = st.number_input("Enter the second number:", value=0.0, step=None, required=True)
num3 = st.number_input("Enter the third number:", value=0.0, step=None, required=True)

# calculate the largest number
largest = find_largest(num1, num2, num3)

# display the largest number in a big font size
st.write("The largest number is:", largest, "<span style='font-size:72px;'>" + str(largest) + "</span>", unsafe_allow_html=True)
