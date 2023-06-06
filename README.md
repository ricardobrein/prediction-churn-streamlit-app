# App de prediccion de abandono de clientes (Churn).

### Una app para predecir el abandono de clientes, introduciendo sus caracteristicas o por lotes con un CSV.

Esta aplicación desplegada en Streamlit, es la continuacion de un análisis completo del dataset de abandono de clientes (Churn) en una compañia de telecomunicaciones.

**En la barra lateral debes seleccionar si deseas prediccion en lotes o un prediccion estandar**


**1. Features**
### Para hacer predicciones sobre un dataframe completo, debe tener el siguiente formato de datos:

<details>
  <summary>Ver tipos de datos que recibe el modelo para predecir</summary>
  
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

Al seleccionar la prediccion por lotes, **la app creara un dataframe con los datos de los clientes que considera propensos a abandonar** según el modelo que hemos entrenado.
Este dataframe lo podemos descargar en formato CSV con datos de "CLientes propensos a abandonar" **esto es especialmente útil si queremos saber tomar acciones de marketing con dichos clientes para intentar retenerlos.**

## Motivación
Esta aplicacion es la continuacion de un análisis completo acerca del abandono de clientes, en [este otro repositorio](https://github.com/ricardobrein/Customer-churn-prediction-models) hice el analisis de los datos y la creacion de modelos de Clasificación como XGBoost, LinearRegression y Random Forest. Puedes ver en ese repositorio las medidas de rendimiento alcanzadas en cada modelo.

> El modelo que hemos usado es la implementacion **Random Forest** con los datos que de Churn de [Maven Analytics](mavenanalytics.io) que me dio muy buenos resultados en el entrenamiento.

**El despliegue a través de Streamlit** considero que es una opcion rapida e interesante para aprender a llevar modelos a produccion  y que podamos ver de manera práctica su desempeño.

![Overview de la App](appgif.gif)

