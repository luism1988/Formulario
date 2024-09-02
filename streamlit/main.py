import streamlit as st
from datetime import datetime
import pandas as pd
import os

# Configuración de la página
st.set_page_config(page_title="App Industry", layout="centered")
with st.sidebar:
    sidebar_selection = st.radio('Navegación', ["Check list diario de proceso","Mantenimiento","Rechazo"])

#page one: 
if sidebar_selection == "Check list diario de proceso":
        # Crear tres columnas y colocar la imagen en la columna del medio
    col1, col2, col3 = st.columns([1, 2, 1])

    ##with col2:
        #st.image('Banner.png')

    # Título principal
    st.markdown("<h1 style='text-align: center; color: black;'>INDUSTRY 4.0</h2>", unsafe_allow_html=True)


   

    # Botones centrados
    col1, col2, col3 = st.columns(3)

    # Definición de variables de estado para saber en qué página estamos
    if 'pagina' not in st.session_state:
        st.session_state.pagina = None

    if col1.button("Check list"):
        st.session_state.pagina = "Check list"

    if col3.button("Visualización data"):
        st.session_state.pagina = "Visualización data"

    # Página de Mantenimiento
    if st.session_state.pagina == "Check list":
        st.subheader("Check list diario de proceso")
    
        # Usamos un formulario para capturar los datos sin refrescar la página
        with st.form(key='form_mantenimiento'):
            col01, col02 = st.columns(2)
            with col01:
                operador = st.selectbox('Tecnico', ['Tecnico 1', 'Tecnico 2','Tecnico 3'])

            with col02:
                maquina = st.selectbox('Máquina', ['Máquina 1', 'Máquina 2','Máquina 3', 'Máquina 4'])

            estado_tarea_1 = st.checkbox("Comprobar temperatura de máquina [20-40ºC]")
            estado_tarea_2 = st.checkbox("Comprobar presión de máquina [5-10 bar]")
            estado_tarea_3 = st.checkbox("Comprobar nivel de aceite en máquina [3-5 litros]")
            estado_tarea_4 = st.checkbox("Limpiar filtro de aire")
            estado_tarea_5 = st.checkbox("Comprobar circulación de agua")
            comentario = st.text_area("Comentario")
            
            # Obtén la fecha y hora actual
            #fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            fecha_actual = datetime.now().strftime("%Y-%m-%d")
            
            # Botón de envío dentro del formulario
            submit_button1 = st.form_submit_button("Enviar")

        # Procesar los datos al enviar
        if submit_button1:
            # Nombre del archivo CSV
            nombre_archivo = 'datos_mantenimiento.csv'
            
            # Crear un DataFrame con los datos ingresados
            nuevo_registro = {
                'Fecha': [fecha_actual],
                'Tecnico': [operador],
                'Máquina': [maquina],
                'Tarea1': [estado_tarea_1],
                'Tarea2': [estado_tarea_2],
                'Tarea3': [estado_tarea_3],
                'Tarea4': [estado_tarea_4],
                'Tarea5': [estado_tarea_5],
                'Comentario': [comentario]
            }
            df_nuevo = pd.DataFrame(nuevo_registro)
            
            # Verificar si el archivo ya existe
            if os.path.exists(nombre_archivo):
                # Si existe, añadir el nuevo registro
                df_existente = pd.read_csv(nombre_archivo)
                df_actualizado = pd.concat([df_existente, df_nuevo], ignore_index=True)
                df_actualizado.to_csv(nombre_archivo, index=False)
            else:
                # Si no existe, crear el archivo con el nuevo registro
                df_nuevo.to_csv(nombre_archivo, index=False)

            # Mostrar mensaje de confirmación y navegar a la página de "Visualización"
            st.success("Datos guardados exitosamente.")
            st.session_state.pagina = "Visualización"

    # Página de Visualización
    if st.session_state.pagina == "Visualización data":
        st.title("Visualización")

        # Verificar si el archivo CSV existe
        nombre_archivo = 'datos_mantenimiento.csv'
        if os.path.exists(nombre_archivo):
            # Cargar los datos desde el archivo CSV
            df = pd.read_csv(nombre_archivo)
            st.dataframe(df)
        else:
            st.write("No hay datos disponibles.")
#page two: 
if sidebar_selection == "Mantenimiento":
    st.write("Pagina en construcción.")
#page 3: 
if sidebar_selection == "Rechazo":
    st.write("Pagina en construcción.")


