import streamlit as st
import requests
import pandas as pd

# Streamlit Title
st.title("Inscription Application")

# Create a form to input user details
st.subheader("Inscription Form")
user_name = st.text_input("Nombre")
user_lastname = st.text_input("Apellido")
dni = st.text_input("dni")
subject = st.text_input("Materia")

# Create a button to submit the form
if st.button("Inscribir"):
    # Prepare the data to send to your Flask API
    data = {
        "user_name": user_name,
        "user_lastname": user_lastname,
        "dni": dni,
        "subject": subject
    }

    # Send a POST request to your Flask API
    response = requests.post('http://localhost:5000/inscribir', json=data)


# Create a Streamlit section to display inscriptions
st.header("Inscriptions")

# Define the backend route URL
backend_url = "http://localhost:5000/inscriptions"  # Replace with the actual URL

# Make a request to the backend API to fetch inscriptions
response = requests.get(backend_url)

# Check if the request was successful
if response.status_code == 200:
    inscriptions = response.json()

    # Convert the list of inscriptions to a Pandas DataFrame
    df = pd.DataFrame(inscriptions)

    # Select and order the specific columns you want to display
    columns_to_display = ['user_name', 'user_lastname', 'dni', 'subject', 'transaction_id']
    df = df[columns_to_display]

    # Rename columns for better display
    df.columns = ['Nombre', 'Apellido', 'DNI', 'Materia', 'Transaction ID']

    # Display the sorted DataFrame using st.table()
    st.table(df)
else:
    st.error(f"Failed to fetch inscriptions. Status code: {response.status_code}")