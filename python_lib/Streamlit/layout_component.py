import streamlit as st
import pandas as pd 

st.title("Welcome to Streamlit App!")


# sidebar 
st.sidebar.title("Sidebar Control")
menu_option = st.sidebar.selectbox("Menu" , ["Home" , "About" , "Contact"])

st.write(menu_option)

# column

col1  , col2 = st.columns(2)

with col1 :
    st.write("This is in the first column.")

with col2 :
    st.write("This is in the second column.") 


# expander

with st.expander("Got a notifiction expand for check it.") :
    st.write("You got a 1 new notification.")
    st.write("You got a 2 new notification.")
    st.write("You got a 3 new notification.")
    st.write("You got a 4 new notification.")


# table 
tab1, tab2 = st.tabs(["2's table", "3's table"])
with tab1:
    for i in range (1,6) :
        st.write (f"2 * {i} = {2*i}")

with tab2:
    for i in range (1,6) :
        st.write (f"3 * {i} = {3*i}")

# table 

# Sample fruit data
data = {
    "Fruit": ["Apple", "Banana", "Orange", "Mango", "Grapes"],
    "Color": ["Red", "Yellow", "Orange", "Yellow/Red", "Green/Purple"],
    "Price (USD)": [0.5, 0.3, 0.6, 1.0, 2.5]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Display in Streamlit
st.title("Fruit Table")
st.table(df)

