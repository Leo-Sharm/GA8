import streamlit as st

def find_largest(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3

# Set page configuration
st.set_page_config(
    page_title="Find the Largest Number",
    page_icon=":mag:",
    layout="wide"
)

# Set page layout
st.markdown("""
<style>
    .stButton>button {
        background-color: #008080;
        color: white;
        font-weight: bold;
        font-size: 16px;
        padding: 8px 12px;
        border-radius: 4px;
        box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
    }
    .stTextInput>div>div>input {
        font-size: 16px !important;
        font-weight: bold;
        padding: 8px 12px !important;
        border-radius: 4px !important;
        box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2) !important;
    }
</style>
""", unsafe_allow_html=True)

# Add title and subtitle
st.title("Find the Largest Number")
st.markdown("Enter three numbers to find the largest among them. :memo:")

# create three mandatory input fields for the user to enter numbers
num1 = st.number_input("Enter the first number:", value=0.0, step=None, format='%f', key='num1')
num2 = st.number_input("Enter the second number:", value=0.0, step=None, format='%f', key='num2')
num3 = st.number_input("Enter the third number:", value=0.0, step=None, format='%f', key='num3')

# Add a button to find the largest number
if st.button("Find the Largest Number :mag_right:"):
    if num1 is not None and num2 is not None and num3 is not None:
        # calculate the largest number
        largest = find_largest(num1, num2, num3)

        # display the largest number in a big font size
        st.markdown("<h1 style='text-align:center; color:#008080;'>The largest number is:</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align:center; color:#008080; font-size: 96px;'>{}</h1>".format(largest), unsafe_allow_html=True)

        # add a gif
        st.markdown("![gif](https://media.giphy.com/media/h8HmN0UcEKR0xWnv3R/giphy.gif)")
        st.error("Please enter all three numbers.")
