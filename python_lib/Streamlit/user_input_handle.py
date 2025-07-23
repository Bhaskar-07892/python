import streamlit as st


# Session State 

if 'count' not in st.session_state:
    st.session_state.count = 0

if st.button("Increase"):
    st.session_state.count += 1

st.write("Count:", st.session_state.count)

# Form

with st.form('Users Form'):
    name = st.text_input('name' , placeholder='Write your name Here')
    submit = st.form_submit_button()

if submit : 
    st.write(f'Hello {name}')


# Call Back 
def greet_user():
    st.session_state.greeting = f"Hello {st.session_state.name}"


if "greeting" not in st.session_state:
    st.session_state.greeting = ""

with st.form("User Form"):
    st.text_input("Name", key="name")
    submitted = st.form_submit_button("Submit", on_click=greet_user)

if submitted:
    st.write(st.session_state.greeting)


