# App de prediccion de abandono de clientes (Churn) Batch y Real Time.

Esta aplicación desplegada en Streamlit, es la continuacion de un análisis completo acerca del abandono de clientes (Churn) a una compañia de telecomunicaciones.

**Puede predecir en Streaming introduciendo los  parametros o en lotes mediante un CSV**

Al seleccionar la prediccion por lotes, **la app creara un dataframe con los datos de los clientes que considera propensos a abandonar** la compañia según el modelo que hemos entrenado.

Podemos descargar un archivo CSV con los datos que la app predice como "CLientes propensos a abandonar" **esto es especialmente útil si queremos saber que acciones tomar con dichos clientes para intentar retenelos.**

Esta aplicacion es la continuacion de un análisis completo acerca del abandono de clientes, en [este otro repositorio](https://github.com/ricardobrein/Customer-churn-prediction-models) hice el analisis de los datos y la creacion de modelos de Clasificación como XGBoost, LinearRegression y Random Forest. Puedes ver en ese repositorio las medidas de rendimiento alcanzadas en cada modelo.

El modelo que hemos usado es la implementacion Random Forest con los datos que de Churn de [Maven Analytics](mavenanalytics.io) que me dio muy buenos resultados, 

El despliegue en Streamlit considero que es una opcion rapida e interesante para aprender a hacer despliegues a produccion de modelos simples y que podamos ver de manera práctica su funcionamiento.

![Overview de la App](appgif.gif)

