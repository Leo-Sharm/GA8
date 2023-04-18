import streamlit as st
from PIL import Image
import random

st.set_page_config(page_title="Soothsayer", page_icon=":crystal_ball:")

# Define a function to find the maximum of three numbers
def find_maximum(num1, num2, num3):
    return max(num1, num2, num3)

# Define the title and introduction text
st.title("Welcome to the Soothsayer")
st.subheader("Ask a question and I'll give you an answer")
st.write("Enter three numbers to find the maximum value. The maximum value will determine the answer to your question.")

# Define the input fields for the three numbers
num1 = st.number_input("Enter the first number :", value=0.0, step=None, format='%f', key='num1')
num2 = st.number_input("Enter the second number :", value=0.0, step=None, format='%f', key='num2')
num3 = st.number_input("Enter the third number :", value=0.0, step=None, format='%f', key='num3')

# Define a button to trigger the maximum calculation
if st.button("Cast Spell"):
    # Call the function to find the maximum value
    maximum = find_maximum(num1, num2, num3)

    # Define a list of answers for the soothsayer to randomly choose from
    answers = ["It is certain", "Without a doubt", "You may rely on it", "Yes, definitely", "It is decidedly so",
               "As I see it, yes", "Most likely", "Yes", "Outlook good", "Signs point to yes",
               "Reply hazy, try again", "Better not tell you now", "Ask again later", "Cannot predict now",
               "Concentrate and ask again", "Don't count on it", "Outlook not so good", "My sources say no",
               "Very doubtful", "My reply is no"]
    
    # Randomly choose an answer from the list
    answer = random.choice(answers)

    # Display the answer and maximum value
    st.write(f"The answer to your question is **{answer}**.")
    st.write(f"The maximum value is **{maximum}**.", unsafe_allow_html=True)
    
    
    # Load the GIF image
    image = Image.open("robin-hood-fortune-teller.gif")
    # Resize the image to fit alongside the output
    image_width = int(image.width * 0.7)
    image_height = int(image.height * 0.7)
    image = image.resize((image_width, image_height))
    # Display the GIF image next to the output
    st.image(image, use_column_width=False, width=300)

  
