# App de prediccion de abandono de clientes (Churn) desplegada en Streamlit.

[Pruébala en este link](https://ricardobrein-prediction-churn-streamlit-app-app-3ch0rd.streamlit.app/)

### En resumen, la aplicación ofrece dos formas de realizar las predicciones:

1. Predicción individual: El usuario puede introducir las características de un cliente de forma manual para obtener una predicción de abandono.
2. Predicción en lotes: El usuario puede cargar un archivo CSV que contenga un conjunto de datos de clientes, y la aplicación realizará predicciones de abandono para cada uno de ellos.

Esta aplicación desplegada en Streamlit, es la continuacion de un análisis completo del dataset de abandono de clientes (Churn) en una compañia de telecomunicaciones.

### Features
**Para hacer predicciones sobre un dataframe completo, debe tener el siguiente formato de datos:**

<details>
  <summary>Ver tipos de datos que recibe el modelo</summary>
  
  <ul style="overflow-y: scroll; max-height: 200px;">
    <li>'Gender': str</li>
    <li>'Age': int</li>
    <li>'Married': bool</li>
    <li>'Number of Dependents': int</li>
    <li>'Number of Referrals': int</li>
    <li>'Tenure in Months': int</li>
    <li>'Offer': bool</li>
    <li>'Phone Service': bool</li>
    <li>'Multiple Lines': bool</li>
    <li>'Internet Service': bool</li>
    <li>'Online Security': bool</li>
    <li>'Online Backup': bool</li>
    <li>'Device Protection Plan': bool</li>
    <li>'Premium Tech Support': bool</li>
    <li>'Streaming TV': bool</li>
    <li>'Streaming Movies': bool</li>
    <li>'Streaming Music': bool</li>
    <li>'Unlimited Data': bool</li>
    <li>'Paperless Billing': bool</li>
    <li>'Monthly Charge': float</li>
    <li>'Total Charges': float</li>
    <li>'Total Refunds': float</li>
    <li>'Total Extra Data Charges': float</li>
    <li>'Total Long Distance Charges': float</li>
    <li>'Internet Type_Cable': bool</li>
    <li>'Internet Type_DSL': bool</li>
    <li>'Internet Type_Fiber Optic': bool</li>
    <li>'Contract_Month-to-Month': bool</li>
    <li>'Contract_One Year': bool</li>
    <li>'Contract_Two Year': bool</li>
    <li>'Payment Method_Bank Withdrawal': bool</li>
    <li>'Payment Method_Credit Card': bool</li>
    <li>'Payment Method_Mailed Check': bool</li>
  </ul>
</details>

### Motivación
Esta aplicación es la continuación de un análisis completo sobre el abandono de clientes. [este otro repositorio](https://github.com/ricardobrein/Customer-churn-prediction-models), donde realicé el análisis de los datos y la creación de modelos de clasificación como XGBoost, LinearRegression y Random Forest. Puedes consultar ese repositorio para ver las medidas de rendimiento alcanzadas en cada modelo.

El modelo que utilice para esta aplicación es la implementación de Random Forest con los datos de Churn de Maven Analytics, el cual ha mostrado buenos resultados durante el entrenamiento.

### Funcionalidad de la aplicación

Al utilizar la predicción por lotes, **se creará un dataframe con los datos de los clientes que se consideran propensos a abandonar.** Este dataframe se podrá descargar en formato CSV. 

Esta funcionalidad resulta especialmente útil si deseamos tomar acciones de marketing dirigidas a estos clientes con el fin de retenerlos. Además, la aplicación puede ser utilizada para otras aplicaciones relacionadas con la segmentación de clientes.

**Considero que el despliegue a través de Streamlit** es una opción rápida e interesante para aprender a llevar modelos a producción y ver de manera práctica su desempeño.

![Overview de la App](appgif.gif)

