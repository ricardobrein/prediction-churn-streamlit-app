# App de prediccion de abandono de clientes (Churn) 
### La app puede predecir en Batch y Real Time.

Esta aplicación desplegada en Streamlit, es la continuacion de un análisis completo del dataset de abandono de clientes (Churn) en una compañia de telecomunicaciones.

**En la barra lateral debes seleccionar si deseas prediccion en lotes o un prediccion estandar**
**1.Features**
Para hacer predicciones sobre un dataframe completo, debe tener el siguiente formato de datos:

> `'Gender': str, 
> 'Age': int, 
> 'Married': bool, 
> 'Number of Dependents': int,
> 'Number of Referrals': int, 
> 'Tenure in Months': int,
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
'Payment Method_Mailed Check': bool`


Al seleccionar la prediccion por lotes, **la app creara un dataframe con los datos de los clientes que considera propensos a abandonar** la compañia según el modelo que hemos entrenado.

Podemos descargar un archivo CSV con los datos que la app predice como "CLientes propensos a abandonar" **esto es especialmente útil si queremos saber que acciones tomar con dichos clientes para intentar retenelos.**

Esta aplicacion es la continuacion de un análisis completo acerca del abandono de clientes, en [este otro repositorio](https://github.com/ricardobrein/Customer-churn-prediction-models) hice el analisis de los datos y la creacion de modelos de Clasificación como XGBoost, LinearRegression y Random Forest. Puedes ver en ese repositorio las medidas de rendimiento alcanzadas en cada modelo.

El modelo que hemos usado es la implementacion Random Forest con los datos que de Churn de [Maven Analytics](mavenanalytics.io) que me dio muy buenos resultados, 

El despliegue en Streamlit considero que es una opcion rapida e interesante para aprender a hacer despliegues a produccion de modelos simples y que podamos ver de manera práctica su funcionamiento.

![Overview de la App](appgif.gif)

