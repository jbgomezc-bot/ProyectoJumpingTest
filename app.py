import streamlit as st
import pandas as pd

# Configuración de página para evitar errores de carga
st.set_page_config(page_title="Gestión Jumping Fitness", layout="wide")

st.title("Sistema Integral de Gestión - Jumping Fitness")

# Menú lateral
menu = st.sidebar.selectbox("Seleccione un Módulo", ["Inicio", "Inventario", "Clientes"])

if menu == "Inicio":
    st.write("Bienvenido al Sistema Integral de Gestión para el centro de Jumping Fitness.")
    st.info("Este prototipo centraliza la operación administrativa")

elif menu == "Inventario":
    st.subheader("Control de Inventario")
    # Datos estructurados simples
    datos = {'Producto': ['Proteína', 'Top Deportivo', 'Bandas'], 'Cantidad': [10, 5, 20]}
    df = pd.DataFrame(datos)
    st.dataframe(df) # st.dataframe es más estable que st.table

elif menu == "Clientes":
    st.subheader("Registro de Clientes")
    nombre = st.text_input("Nombre de la nueva clienta")
    if st.button("Guardar Registro"):
        if nombre:
            st.success(f"La clienta {nombre} ha sido registrada exitosamente.")
        else:
            st.error("Por favor, ingrese un nombre.")