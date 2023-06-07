import pandas as pd
import streamlit as st
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import joblib
import base64

# Cargar los modelos entrenados
modelo_online = joblib.load('rforest.pkl')
modelo_batch = joblib.load('rforest.pkl')

# Crear instancias del LabelEncoder y MinMaxScaler
label_encoder = LabelEncoder()
scaler = MinMaxScaler()

# Definir los tipos de datos esperados para los parámetros
tipos_datos = {
    'Gender': str,
    'Age': int,
    'Married': bool,
    'Number of Dependents': int,
    'Number of Referrals': int,
    'Tenure in Months': int,
    'Offer': bool,
    'Phone Service': bool,
    'Multiple Lines': bool,
    'Internet Service': bool,
    'Online Security': bool,
    'Online Backup': bool,
    'Device Protection Plan': bool,
    'Premium Tech Support': bool,
    'Streaming TV': bool,
    'Streaming Movies': bool,
    'Streaming Music': bool,
    'Unlimited Data': bool,
    'Paperless Billing': bool,
    'Monthly Charge': float,
    'Total Charges': float,
    'Total Refunds': float,
    'Total Extra Data Charges': float,
    'Total Long Distance Charges': float,
    'Internet Type_Cable': bool,
    'Internet Type_DSL': bool,
    'Internet Type_Fiber Optic': bool,
    'Contract_Month-to-Month': bool,
    'Contract_One Year': bool,
    'Contract_Two Year': bool,
    'Payment Method_Bank Withdrawal': bool,
    'Payment Method_Credit Card': bool,
    'Payment Method_Mailed Check': bool
}

# Crear la interfaz de la aplicación
st.title("Aplicación de Predicción de Abandono de Clientes")

st.markdown("""
     :dart:  Esta aplicación de Streamlit está diseñada para predecir
     la rotación de clientes con los datos ficticios de una empresa de Telecomunicaciones.\n
     """)

# Mostrar la opción seleccionada (en línea o por lotes)
opcion = st.sidebar.selectbox("Seleccione el modo de predicción:", ["Predicción en línea", "Predicción por lotes"])
st.sidebar.info(':dart: Selecciona el modo de prediccion de la aplicacion.\n Funciona tanto Online como por Lotes(mediante un CSV)\n')

if opcion == "Predicción en línea":
    # Crear controles para cada parámetro en línea
    parametros = {}
    for parametro, tipo_dato in tipos_datos.items():
        if tipo_dato == int:
            if parametro == 'Age':
                parametros[parametro] = st.slider(parametro, min_value=18, max_value=85, value=18)
            elif parametro == 'Number of Dependents':
                parametros[parametro] = st.number_input(parametro, min_value=0, value=0, step=1)
            elif parametro == 'Number of Referrals':
                parametros[parametro] = st.number_input(parametro, min_value=0, max_value=10, value=0, step=1)
            else:
                parametros[parametro] = st.slider(parametro, min_value=0, max_value=100, value=0)
        elif tipo_dato == bool:
            opciones = ['No', 'Yes']
            valor = st.radio(parametro, opciones)
            
            parametros[parametro] = 1 if valor == 'Yes' else 0
        elif tipo_dato == float:
            parametros[parametro] = st.number_input(parametro)
        elif tipo_dato == str:
            opciones = ['Male', 'Female']
            valor = st.selectbox(parametro, opciones)
            parametros[parametro] = 1 if valor == 'Male' else 0
        else:
            st.write(f"Tipo de dato no compatible para el parámetro: {parametro}")

    # Crear un DataFrame con los datos ingresados por el usuario
    datos = pd.DataFrame([parametros])

    # Ajustar y transformar las columnas categóricas
    columnas_enc = ['Phone Service', 'Multiple Lines', 'Internet Service', 'Online Security',
                    'Online Backup', 'Device Protection Plan', 'Premium Tech Support', 'Streaming TV',
                    'Streaming Movies', 'Streaming Music', 'Unlimited Data', 'Paperless Billing']

    for columna in columnas_enc:
        datos[columna] = label_encoder.fit_transform(datos[columna])

    # Obtener las columnas categóricas codificadas
    datos = pd.get_dummies(datos)

    # Ajustar y transformar las columnas seleccionadas
    columns_to_scale = ['Total Charges', 'Monthly Charge',
                        'Total Long Distance Charges', 'Total Refunds',
                        'Total Extra Data Charges']
    datos[columns_to_scale] = scaler.fit_transform(datos[columns_to_scale])

    # Obtener la predicción al presionar el botón
    if st.button("Obtener Predicción en linea"):
        prediccion = modelo_online.predict(datos)

        # Mapeo de predicción
        mapeo_prediccion = {0: 'El cliente se quedará en la compañía', 1: 'El cliente es propenso a abandonar la compañía'}

        # Obtener el nombre de la predicción
        nombre_prediccion = mapeo_prediccion.get(prediccion[0], 'Desconocido')

        # Mostrar el resultado de la predicción
        st.subheader("Resultado de la Predicción:")
        st.markdown('<div style="background-color: blue; color: white; padding: 10px;">' + nombre_prediccion + '</div>', unsafe_allow_html=True)

else:
    
    mapeo_etiquetas = {
    'Gender': {0: 'Female', 1: 'Male'},
    'Married': bool,
    'Number of Dependents': int,
    'Number of Referrals': int,
    'Tenure in Months': int,
    'Offer': bool,
    'Phone Service': {0: 'No', 1: 'Yes'},
    'Multiple Lines': {0: 'No', 1: 'No phone service', 2: 'Yes'},
    'Internet Service': {0: 'No', 1: 'No internet service', 2: 'Yes'},
    'Online Security': {0: 'No', 1: 'No internet service', 2: 'Yes'},
    'Online Backup': {0: 'No', 1: 'No internet service', 2: 'Yes'},
    'Device Protection Plan': {0: 'No', 1: 'No internet service', 2: 'Yes'},
    'Premium Tech Support': {0: 'No', 1: 'No internet service', 2: 'Yes'},
    'Streaming TV': {0: 'No', 1: 'No internet service', 2: 'Yes'},
    'Streaming Movies': {0: 'No', 1: 'No internet service', 2: 'Yes'},
    'Streaming Music': {0: 'No', 1: 'No internet service', 2: 'Yes'},
    'Unlimited Data': {0: 'No', 1: 'No internet service', 2: 'Yes'},
    'Paperless Billing': {0: 'No', 1: 'Yes'},
    'Monthly Charge': float,
    'Total Charges': float,
    'Total Refunds': float,
    'Total Extra Data Charges': float,
    'Total Long Distance Charges': float,
    'Internet Type_Cable': bool,
    'Internet Type_DSL': bool,
    'Internet Type_Fiber Optic': bool,
    'Contract_Month-to-Month': bool,
    'Contract_One Year': bool,
    'Contract_Two Year': bool,
    'Payment Method_Bank Withdrawal': bool,
    'Payment Method_Credit Card': bool,
    'Payment Method_Mailed Check': bool
}
    # Opción de predicción por lotes
    st.title("Aplicación de Predicción de abandono de clientes por lotes")

# Opción para subir archivos CSV en lotes
    uploaded_file = st.file_uploader("Cargar archivo CSV", type="csv")

    if uploaded_file is not None:
    # Leer el archivo CSV y convertirlo en un DataFrame
        df = pd.read_csv(uploaded_file)
        
        columnas_enc = ['Phone Service', 'Multiple Lines', 'Internet Service', 'Online Security',
                    'Online Backup', 'Device Protection Plan', 'Premium Tech Support', 'Streaming TV',
                    'Streaming Movies', 'Streaming Music', 'Unlimited Data', 'Paperless Billing']

        # Ajustar y transformar las columnas categóricas
        for columna in columnas_enc:
            df[columna] = label_encoder.fit_transform(df[columna])

        # Obtener las columnas categóricas codificadas
        df = pd.get_dummies(df)
        
        columns_to_scale = ['Total Charges', 'Monthly Charge',
                        'Total Long Distance Charges', 'Total Refunds',
                        'Total Extra Data Charges']

        # Ajustar y transformar las columnas seleccionadas
        df[columns_to_scale] = scaler.fit_transform(df[columns_to_scale])

        # Obtener las predicciones del modelo por lotes
        predicciones = modelo_batch.predict(df)

        mapeo_prediccion = {0: 'El cliente es propenso a abandonar la compañía', 1: 'El cliente está contento con la compañía'}

    # Crear un DataFrame con las predicciones y las etiquetas originales
        df_predicciones = pd.DataFrame({'Cliente': range(1, len(df) + 1),
                                        'Predicción': [mapeo_prediccion[p] for p in predicciones]})

    # Volver a ponerle las etiquetas originales a las columnas
        for columna, etiquetas in mapeo_etiquetas.items():
            df_predicciones[columna] = df[columna].map(etiquetas)

    # Filtrar los clientes propensos a abandonar la compañía
        clientes_propensos = df_predicciones[df_predicciones['Predicción'] == 'El cliente es propenso a abandonar la compañía']
    
    # Volver a ponerle las etiquetas originales (recodificar)
        for columna, etiquetas in mapeo_etiquetas.items():
            clientes_propensos.loc[:, columna] = df.loc[:, columna].map(etiquetas)

        """
            Vamos a guardar el DataFrame de clientes propensos en un archivo CSV para uso posterior
            Creando un enlace de descarga para el csv de los clientes propensos a abandonar. 
    
        """
    
        csv = clientes_propensos.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()  # Codificar el archivo CSV en base64
        href = f'<a href="data:file/csv;base64,{b64}" download="clientes_propensos.csv">Descargar archivo CSV de clientes propensos a abandonar</a>'

        # Rresultados de la predicción
        st.subheader("Resultados de la Predicción:")
        st.dataframe(clientes_propensos)

        #Mostrar el enlace de descarga
        st.markdown(href, unsafe_allow_html=True)

        # Me parece conveniente mostrar la sumatoria de los parámetros para las predicciones
        propensos = (predicciones == 0).sum()
        contentos= (predicciones == 1).sum()

        # Mostrar el resumen de los parámetros
        st.subheader("Resumen de los datos:")
        st.write(f"Clientes propensos a abandonar la compañía: {propensos}")
        st.write(f"Clientes contentos con la compañía: {contentos}")

