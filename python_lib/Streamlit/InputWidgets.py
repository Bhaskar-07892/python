import streamlit as st 

st.title("This is my Streamlit App")

# st.text_input(), st.number_input(), st.selectbox(), st.radio(), st.slider()


# Selectbox
selected_lang = st.selectbox("In which language do you want speak ?" , ["Hindi" ,"English" , "Panjabi" , "Telgu" , "Tamil" , "Marathi" , "Urdu" ])
st.success(f"You are comforteble in {selected_lang}.\n ")


# Slider
count_lang = st.slider("How many Indian language do you know ? " , min_value=1 , max_value=22 )
st.success(f"You known {count_lang} language of India. \n")


# Check Box"
hobby = st.write("What do you like " )

st.checkbox("Music")
st.checkbox("Sports")
st.checkbox("Gaming")
st.checkbox("Travelling")


# Radio Box 
fav_color = st.radio("Which is your favriot color" , ['Red' , 'Green', 'Blue' ,'Black'])
st.success(f"Your favriote color is {fav_color}.\n ")

# Text Input
name = st.text_input("What is your name : ")
if name:
    st.success(f"Hi ! {name}. \n")

# Number Input 
num = st.number_input("What number do you have choose : \n")
if num:
    st.success(f"You choose nuber {num}. \n")

bton = st.button ('submit')
if bton:
    st.success(f"From Submited : {bton}. \n")