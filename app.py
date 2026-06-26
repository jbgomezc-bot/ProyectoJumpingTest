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
    
    # 1. Leer el archivo de clientes existente
    try:
        df_clientes = pd.read_csv('clientes.csv')
    except:
        df_clientes = pd.DataFrame(columns=['Nombre'])
    
    # 2. Entrada de datos
    nombre = st.text_input("Nombre de la nueva clienta")
    if st.button("Guardar Registro"):
        if nombre:
            # Agregar al DataFrame y guardar en el CSV
            nuevo_registro = pd.DataFrame({'Nombre': [nombre]})
            df_clientes = pd.concat([df_clientes, nuevo_registro], ignore_index=True)
            df_clientes.to_csv('clientes.csv', index=False)
            st.success(f"La clienta {nombre} ha sido registrada.")
        else:
            st.error("Ingresa un nombre.")
    
    # 3. Mostrar la lista de clientes registrados
    st.write("### Listado de Clientas Registradas")
    st.table(df_clientes)