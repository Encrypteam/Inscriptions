import streamlit as st
import requests
import pandas as pd

# Create a sidebar for navigation
with st.sidebar:
    # Create a selectbox for switching views
    selected_view = st.radio("Select a view", ["Inscripcion a Examen", "Alumnos inscriptos"])

# Streamlit Title
st.title("Inscripcion a Mesas de Examen")

if selected_view == "Inscripcion a Examen":
    # Create a form to input user details
    st.subheader("Cargue los datos del alumno")
    user_name = st.text_input("Nombre")
    user_lastname = st.text_input("Apellido")
    dni = st.text_input("DNI")
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

        if response.status_code == 200:
            st.success("Inscripción exitosa.")
        else:
            st.error(f"Fallo la inscripción. Status code: {response.status_code}")

if selected_view == "Alumnos inscriptos":
    # Create a Streamlit section to display inscriptions
    st.header("Alumnos inscriptos")

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

        # Create hyperlinks for Transaction ID
        df['Transaction ID'] = df['Transaction ID'].apply(lambda x: f'<a href="https://testnet.algoexplorer.io/tx/{x}" target="_blank">{x}</a>')

        # Display the DataFrame using st.markdown to render hyperlinks as clickable
        st.markdown(df.to_html(escape=False), unsafe_allow_html=True)
    else:
        st.error(f"Failed to fetch inscriptions. Status code: {response.status_code}")
